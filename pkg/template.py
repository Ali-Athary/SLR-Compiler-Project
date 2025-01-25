import requests
import feedparser
import openai
from PyPDF2 import PdfReader
import os
import markdown2
import pdfkit
import urllib.parse
from langdetect import detect

openai.api_key = 'your-openai-api-key'

class Paper:
    def __init__(self, title=None, authors=None, published=None, summary=None, link=None, pdf_link=None):
        self.title = title
        self.authors = authors
        self.published = published
        self.summary = summary
        self.link = link
        self.pdf_link = pdf_link


class ArxivSearcher:
    def __init__(self, query_terms=None, year_range=None, max_results=None):
        self.query_terms = query_terms or []
        self.year_range = year_range or (None, None)
        self.max_results = max_results or 10

    def search(self):
        if not self.query_terms:
            return []

        base_url = 'http://export.arxiv.org/api/query?'

        # Build the query string
        query_parts = []
        for term in self.query_terms:
            term = term.replace('"', '')  # Remove quotes if any
            query_parts.append(f'ti:"{term}" OR abs:"{term}"')

        query = ' AND '.join(query_parts)

        # Include year range if specified
        if all(self.year_range):
            date_from = f"{self.year_range[0]}0101000000"
            date_to = f"{self.year_range[1]}1231235959"
            date_query = f"submittedDate:[{date_from} TO {date_to}]"
            query = f"({query}) AND {date_query}"

        # Encode the query parameters
        params = {
            'search_query': query,
            'start': 0,
            'max_results': self.max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        search_url = base_url + urllib.parse.urlencode(params)

        feed = feedparser.parse(search_url)

        papers = []
        for entry in feed.entries:
            paper = Paper(
                title=entry.title,
                authors=', '.join(author.name for author in entry.authors),
                published=entry.published,
                summary=entry.summary,
                link=entry.link,
                pdf_link=entry.id.replace('abs', 'pdf') + '.pdf'
            )
            papers.append(paper)

        return papers


class PaperFilter:
    def __init__(self, exclude_keywords=None, min_pages=None, languages=None):
        self.exclude_keywords = exclude_keywords or []
        self.min_pages = min_pages or 0
        self.languages = languages or ['en']

    def filter(self, papers):
        return [paper for paper in papers if self.filter_paper(paper)]

    def filter_paper(self, paper):
        if any(keyword.lower() in paper.summary.lower() for keyword in self.exclude_keywords):
            return False
        if not self.language_supported(paper.summary):
            return False
        # The page count functionality would require downloading the PDF,
        # which is not practical at this filtering stage.
        return True

    def language_supported(self, summary):
        try:
            detected_lang = detect(summary)
            return detected_lang in self.languages
        except:
            return False


class PDFOperations:
    def __init__(self):
        pass

    def download_pdf(self, pdf_url, save_path):
        response = requests.get(pdf_url)
        with open(save_path, 'wb') as f:
            f.write(response.content)

    def extract_text_from_pdf(self, file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text


class OpenAISummarizer:
    def __init__(self, method=None, max_length=None):
        self.method = method or 'gpt-4'
        self.max_length = max_length or 300

    def summarize_text(self, text):
        truncated_text = text[:3000]  # Ensure the text is within token limits
        if self.method == 'gpt-4':
            response = openai.ChatCompletion.create(
                model='gpt-4',
                messages=[
                    {"role": "system", "content": "You are an academic paper summarizer."},
                    {"role": "user", "content": f"Summarize the following academic paper:\n\n{truncated_text}"}
                ],
                max_tokens=self.max_length
            )
            return response['choices'][0]['message']['content'].strip()
        elif self.method == 'textrank':
            # Using gensim's summarize function
            from gensim.summarization.summarizer import summarize
            try:
                summary = summarize(text, word_count=self.max_length)
                return summary.strip()
            except Exception:
                return "Could not generate summary with TextRank."
        else:
            return "Invalid summarization method specified."


class ArxivAnalysis:
    def __init__(self, searcher=None, filterer=None, summarizer=None, pdf_ops=None, report_config=None):
        self.searcher = searcher or ArxivSearcher()
        self.filterer = filterer or PaperFilter()
        self.summarizer = summarizer or OpenAISummarizer()
        self.pdf_ops = pdf_ops or PDFOperations()
        self.report_config = report_config or {
            'format': 'markdown',
            'include_metadata': True,
            'output_path': 'report.md'
        }

    def analyze(self):
        papers = self.searcher.search()
        filtered_papers = self.filterer.filter(papers)

        markdown_content = []
        for index, paper in enumerate(filtered_papers):
            markdown_content.append(f"## Paper {index + 1}\n")
            markdown_content.append(f"**Title:** {paper.title}\n")
            if self.report_config.get('include_metadata', True):
                markdown_content.append(f"**Authors:** {paper.authors}\n")
                markdown_content.append(f"**Published:** {paper.published}\n")
                markdown_content.append(f"**Link:** {paper.link}\n")
            markdown_content.append(f"**Abstract:** {paper.summary}\n")

            # Step 2: Download PDF and generate overview
            pdf_file = f"paper_{index + 1}.pdf"
            try:
                self.pdf_ops.download_pdf(paper.pdf_link, pdf_file)
                text = self.pdf_ops.extract_text_from_pdf(pdf_file)
                overview = self.summarizer.summarize_text(text)
            except Exception as e:
                overview = "An error occurred in processing this PDF."

            markdown_content.append(f"**Overview:** {overview}\n")
            os.remove(pdf_file)
            markdown_content.append("\n---\n")

        # Write Markdown file
        output_format = self.report_config.get('format', 'markdown').lower()
        output_path = self.report_config.get('output_path', 'report.md')

        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.writelines(markdown_content)

        # Convert to PDF if required
        if output_format == 'pdf':
            self.markdown_to_pdf(output_path)
            # Remove the intermediate Markdown file if not needed
            if not output_path.endswith('.pdf'):
                os.remove(output_path)

    def markdown_to_pdf(self, markdown_file):
        # Ensure the output PDF file has the correct extension
        if markdown_file.endswith('.md'):
            pdf_file = markdown_file[:-3] + '.pdf'
        else:
            pdf_file = markdown_file + '.pdf'

        html_content = markdown2.markdown_path(markdown_file)
        pdfkit.from_string(html_content, pdf_file)


# Example usage
if __name__ == '__main__':
    query_terms = ["AI", "machine learning"]
    year_range = (2000, 2023)
    max_results = 10
    exclude_keywords = ["beginner"]
    min_pages = 5
    languages = ['en', 'fa']

    # Report configuration
    report_config = {
        'format': 'pdf',  # Options: 'markdown', 'pdf'
        'include_metadata': True,
        'output_path': 'analysis_report.pdf'
    }

    searcher = ArxivSearcher(query_terms, year_range, max_results)
    filterer = PaperFilter(exclude_keywords, min_pages, languages)
    summarizer = OpenAISummarizer(method='gpt-4', max_length=300)
    pdf_ops = PDFOperations()

    analysis = ArxivAnalysis(searcher, filterer, summarizer, pdf_ops, report_config)
    analysis.analyze()