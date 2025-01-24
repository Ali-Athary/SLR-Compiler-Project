import requests
import feedparser
import openai
from PyPDF2 import PdfReader
import os

openai.api_key = 'your-openai-api-key'


def search_arxiv(topic, max_results=10):
    base_url = 'http://export.arxiv.org/api/query?'
    query = f"search_query=all:{topic}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    search_url = base_url + query
    feed = feedparser.parse(search_url)

    papers = []
    for entry in feed.entries:
        paper = {
            'title': entry.title,
            'authors': ', '.join(author.name for author in entry.authors),
            'published': entry.published,
            'summary': entry.summary,
            'link': entry.link,
            'pdf_link': entry.id.replace('abs', 'pdf') + '.pdf'
        }
        papers.append(paper)

    return papers


def download_pdf(pdf_url, save_path):
    response = requests.get(pdf_url)
    with open(save_path, 'wb') as f:
        f.write(response.content)


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def summarize_with_openai(text, max_chars=3000):
    # Adjusting the token limit for practical usage
    truncated_text = text[:max_chars]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following academic paper:\n\n{truncated_text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


def main(topic):
    # Step 1: Fetch papers from arXiv
    papers = search_arxiv(topic)

    for index, paper in enumerate(papers):
        print(f"\nFetching and summarizing paper {index + 1} of {len(papers)}...")
        print(f"Title: {paper['title']}")
        print(f"Authors: {paper['authors']}")
        print(f"Published: {paper['published']}")
        print(f"Abstract: {paper['summary']}")
        print(f"Link: {paper['link']}")

        # Step 2: Download PDF
        pdf_file = f"paper_{index + 1}.pdf"
        download_pdf(paper['pdf_link'], pdf_file)

        # Step 3: Extract and summarize text
        try:
            text = extract_text_from_pdf(pdf_file)
            overview = summarize_with_openai(text)
        except Exception as e:
            overview = "An error occurred in processing this PDF."

        print(f"Overview: {overview}\n")
        os.remove(pdf_file)


if __name__ == '__main__':
    topic = input("Enter a topic to search on arXiv: ")
    main(topic)