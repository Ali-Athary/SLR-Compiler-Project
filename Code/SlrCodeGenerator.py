# Code/SlrCodeGenerator.py

import textwrap


class SlrCodeGenerator:
    def __init__(self):
        pass
    """
    این کلاس یک اسکریپت پایتون خروجی می‌سازد که با استفاده از dsl_config
    تمامی مراحل جستجوی Arxiv، فیلتر، خلاصه‌سازی و تولید گزارش را انجام می‌دهد.
    """

    def generate_code(self, dsl_config: dict) -> str:
        """
        با گرفتن dsl_config از SlrCustomListener،
        کد پایتون نهایی را به صورت یک رشته تولید می‌کند.
        """

        # 1) داده‌های DSL را از دیکشنری استخراج می‌کنیم
        topic = dsl_config.get('topic', '')

        # بخش search
        search_cfg = dsl_config.get('search', {})
        search_queries = search_cfg.get('queries', [])
        year_range = search_cfg.get('year_range', (None, None))
        max_results = search_cfg.get('max_results', 10)

        # بخش filters
        filters_cfg = dsl_config.get('filters', {})
        exclude_keywords = filters_cfg.get('exclude_keywords', [])
        min_pages = filters_cfg.get('min_pages', 0)
        languages = filters_cfg.get('languages', ['en'])

        # بخش analyze
        analyze_cfg = dsl_config.get('analyze', {})
        summarize_cfg = analyze_cfg.get('summarize', {})
        method = summarize_cfg.get('method', 'gpt-4')
        max_length = summarize_cfg.get('max_length', 300)
        extract_fields = analyze_cfg.get('extract_fields', [])
        keyword_cloud = analyze_cfg.get('keyword_cloud', False)

        # بخش report
        report_cfg = dsl_config.get('report', {})
        report_format = report_cfg.get('format', 'markdown')
        include_metadata = report_cfg.get('include_metadata', True)
        output_path = report_cfg.get('output_path', 'report.md')

        # 2) حالا با رشته‌سازی (String Formatting) یک کد پایتون نهایی می‌سازیم
        #    این کد شامل کلاس‌ها یا متدهایی است که جستجو در arxiv، فیلتر و گزارش را انجام می‌دهند.
        #    شما می‌توانید از الگوی زیر استفاده کنید یا با توجه به ساختار پروژه، تغییر دهید.

        code = textwrap.dedent(f'''
        """
        این فایل پایتونی به صورت خودکار توسط SLR DSL ساخته شده است.
        با اجرای این فایل، یک مرور ادبیات خودکار انجام می‌شود.
        """

        import requests
        import feedparser
        import openai
        from PyPDF2 import PdfReader
        import os
        import markdown2
        import pdfkit
        import urllib.parse
        from langdetect import detect

        # در صورت نیاز، اینجا می‌توانید کلید OpenAI را ست کنید
        # یا از متغیر محیطی استفاده نمایید
        openai.api_key = "YOUR_OPENAI_API_KEY"

        class Paper:
            def __init__(self, title=None, authors=None, published=None, summary=None, link=None, pdf_link=None):
                self.title = title
                self.authors = authors
                self.published = published
                self.summary = summary
                self.link = link
                self.pdf_link = pdf_link

        class ArxivSearcher:
            def __init__(self, query_terms=None, year_range=(None, None), max_results=10):
                self.query_terms = query_terms or []
                self.year_range = year_range
                self.max_results = max_results

            def search(self):
                if not self.query_terms:
                    return []

                base_url = 'http://export.arxiv.org/api/query?'
                query_parts = []
                for term in self.query_terms:
                    term = term.replace('"', '')  # حذف نقل قول‌ها
                    # در عنوان یا چکیده جستجو می‌کنیم
                    query_parts.append(f'ti:"{{{{term}}}}" OR abs:"{{{{term}}}}"')

                query = ' AND '.join(query_parts)

                # بازه سال
                if self.year_range[0] and self.year_range[1]:
                    date_from = f"{{{{self.year_range[0]}}}}0101000000"
                    date_to = f"{{{{self.year_range[1]}}}}1231235959"
                    date_query = f"submittedDate:[{{{{date_from}}}} TO {{{{date_to}}}}]"
                    query = f"({{{{query}}}}) AND {{{{date_query}}}}"

                params = {{{{
                    'search_query': query,
                    'start': 0,
                    'max_results': self.max_results,
                    'sortBy': 'submittedDate',
                    'sortOrder': 'descending'
                }}}}
                search_url = base_url + urllib.parse.urlencode(params)
                feed = feedparser.parse(search_url)

                papers = []
                for entry in feed.entries:
                    pdf_link = entry.id.replace('abs', 'pdf') + '.pdf'
                    p = Paper(
                        title=entry.title,
                        authors=', '.join([a.name for a in entry.authors]),
                        published=entry.published,
                        summary=entry.summary,
                        link=entry.link,
                        pdf_link=pdf_link
                    )
                    papers.append(p)
                return papers

        class PaperFilter:
            def __init__(self, exclude_keywords=None, min_pages=0, languages=None):
                self.exclude_keywords = exclude_keywords or []
                self.min_pages = min_pages
                self.languages = languages or ['en']

            def filter(self, papers):
                filtered = []
                for paper in papers:
                    # 1) بررسی کلمات ممنوع در چکیده یا متن
                    if not self._exclude_keywords_check(paper):
                        continue
                    # 2) بررسی زبان (چکیده)
                    if not self._language_check(paper):
                        continue
                    # 3) بررسی تعداد صفحات (در صورت نیاز باید PDF دانلود و صفحات شمرده شوند)
                    #   در این مرحله پیاده‌سازی نشده ولی می‌توانید اضافه کنید.
                    filtered.append(paper)
                return filtered

            def _exclude_keywords_check(self, paper):
                text = (paper.summary or "").lower()
                for kw in self.exclude_keywords:
                    if kw.lower() in text:
                        return False
                return True

            def _language_check(self, paper):
                try:
                    lang = detect(paper.summary or "")
                    return lang in self.languages
                except:
                    return False

        class PDFOperations:
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
            def __init__(self, method="gpt-4", max_length=300):
                self.method = method
                self.max_length = max_length

            def summarize_text(self, text):
                truncated_text = text[:4000]  # جلوگیری از طول بیش از حد
                if self.method == "gpt-4":
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {{{{"role": "system", "content": "You are an academic paper summarizer."}}}},
                            {{{{"role": "user", "content": f"Summarize the following text:\\n\\n{{{{truncated_text}}}}" }}}}
                        ],
                        max_tokens=self.max_length
                    )
                    return response["choices"][0]["message"]["content"].strip()
                elif self.method == "textrank":
                    from gensim.summarization.summarizer import summarize
                    try:
                        summary = summarize(text, word_count=self.max_length)
                        return summary.strip()
                    except:
                        return "Could not generate summary with TextRank."
                else:
                    return "Invalid summarization method specified."

        class ArxivAnalysis:
            def __init__(self, searcher, filterer, summarizer, pdf_ops, report_config):
                self.searcher = searcher
                self.filterer = filterer
                self.summarizer = summarizer
                self.pdf_ops = pdf_ops
                self.report_config = report_config

            def analyze(self):
                papers = self.searcher.search()
                filtered_papers = self.filterer.filter(papers)

                markdown_content = []
                # عنوان کلی
                markdown_content.append(f"# SLR for: {topic}\\n\\n")

                for idx, paper in enumerate(filtered_papers, start=1):
                    markdown_content.append(f"## Paper {{{{idx}}}}\\n")
                    markdown_content.append(f"**Title:** {{{{paper.title}}}}\\n")
                    if self.report_config.get("include_metadata", True):
                        markdown_content.append(f"**Authors:** {{{{paper.authors}}}}\\n")
                        markdown_content.append(f"**Published:** {{{{paper.published}}}}\\n")
                        markdown_content.append(f"**Link:** {{{{paper.link}}}}\\n")

                    markdown_content.append(f"**Abstract:** {{{{paper.summary}}}}\\n")

                    # دانلود PDF و خلاصه کردن
                    pdf_file = f"paper_{{{{idx}}}}.pdf"
                    try:
                        self.pdf_ops.download_pdf(paper.pdf_link, pdf_file)
                        text = self.pdf_ops.extract_text_from_pdf(pdf_file)
                        overview = self.summarizer.summarize_text(text)
                    except Exception as e:
                        overview = f"Error in PDF processing: {{{{str(e)}}}}"
                    finally:
                        # پاک کردن فایل PDF (دلخواه)
                        if os.path.exists(pdf_file):
                            os.remove(pdf_file)

                    markdown_content.append(f"**Overview:** {{{{overview}}}}\\n")
                    markdown_content.append("\\n---\\n")

                # تولید خروجی نهایی
                out_format = self.report_config.get("format", "markdown").lower()
                out_path = self.report_config.get("output_path", "report.md")

                with open(out_path, "w", encoding="utf-8") as md_file:
                    md_file.writelines(markdown_content)

                if out_format == "pdf":
                    html_content = markdown2.markdown("".join(markdown_content))
                    out_pdf = out_path if out_path.endswith(".pdf") else out_path.replace(".md", ".pdf")
                    pdfkit.from_string(html_content, out_pdf)
                    # در صورت تمایل فایل MD موقت را پاک کنید
                    if out_pdf != out_path:
                        pass

        def main():
            print("=== Auto-Generated SLR Pipeline ===")
            print("Topic:", "{topic}")
            # مقداردهی اجزای تحلیل
            searcher = ArxivSearcher(
                query_terms={search_queries},
                year_range={year_range},
                max_results={max_results}
            )
            filterer = PaperFilter(
                exclude_keywords={exclude_keywords},
                min_pages={min_pages},
                languages={languages}
            )
            summarizer = OpenAISummarizer(method="{method}", max_length={max_length})
            pdf_ops = PDFOperations()

            report_config = {{{{
                "format": "{report_format}",
                "include_metadata": {include_metadata},
                "output_path": "{output_path}"
            }}}}

            analysis = ArxivAnalysis(searcher, filterer, summarizer, pdf_ops, report_config)
            analysis.analyze()

        if __name__ == "__main__":
            main()
        ''')

        # 3) در بخش بالا، برای قرار دادن لیست‌ها یا تاپل‌ها در فرمت رشته، باید حواسمان باشد پایتون آن‌ها را درست بفهمد:
        #    با استفاده از فرمت هایلایت شده (مثلا {search_queries} -> ['AI','ML'])
        #    textwrap.dedent کمک می‌کند تورفتگی‌های غیرضروری حذف شوند

        # ساخت یک فرمت امن‌تر (برای لیست‌ها و غیره):
        # مثلاً با استفاده از repr() جهت تبدیل ساختار پایتونی به رشته قابل قبول
        final_code = code.format(
            topic=topic,
            search_queries=repr(search_queries),  # اطمینان حاصل کنید این مقدار درست مقداردهی شده است
            year_range=repr(year_range),
            max_results=repr(max_results),
            exclude_keywords=repr(exclude_keywords),
            min_pages=repr(min_pages),
            languages=repr(languages),
            method=method,
            max_length=max_length,
            report_format=report_format,
            include_metadata=repr(include_metadata),
            output_path=output_path
        )

        return final_code

