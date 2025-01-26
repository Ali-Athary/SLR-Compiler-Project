from gen.SlrListener import SlrListener
from Repository.ast import AST


class SlrCustomListener(SlrListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names  # ممکن است بعداً جهت دیباگ استفاده شود
        # دیکشنری نهایی که تمام مقادیر DSL در آن نگهداری خواهند شد:
        self.dsl_config = {}

        # این متغیرها برای نگهداری مقادیر موقت داخل بلاک‌های مختلف استفاده می‌شوند:
        self.current_search = None
        self.current_filters = None
        self.current_analyze = None
        self.current_summarize = None
        self.current_report = None

    # ------------------------------------------------------------------------
    # برنامه اصلی: program: topic search filters analyze report;
    # ------------------------------------------------------------------------
    def exitProgram(self, ctx):
        """
        این متد پس از خواندن کل 'program' (topic, search, filters, analyze, report) فراخوانی می‌شود.
        در اینجا نیاز خاصی به کد نداریم، چراکه همه چیز در دیکشنری self.dsl_config قرار گرفته است.
        """
        pass

    # ------------------------------------------------------------------------
    # topic: 'topic ' STRING mandatory_nl;
    # ------------------------------------------------------------------------
    def exitTopic(self, ctx):
        """
        از روی TOKEN مربوط به STRING متن تاپیک را استخراج می‌کنیم و در dsl_config ذخیره می‌کنیم.
        """
        raw_str = ctx.STRING().getText()   # مثلاً "My Research"
        topic_str = raw_str.strip('"')     # حذف علامت نقل‌قول
        self.dsl_config['topic'] = topic_str

    # ------------------------------------------------------------------------
    # search: 'search' LCB optional_nl query yearRange maxResults RCB optional_nl;
    #   query: 'query' LB STRING (',' STRING)* RB mandatory_nl;
    #   yearRange: 'year_range' NUMBER 'to' NUMBER mandatory_nl;
    #   maxResults: 'max_results' NUMBER mandatory_nl;
    # ------------------------------------------------------------------------
    def enterSearch(self, ctx):
        """
        ابتدای ورود به بلاک search
        یک دیکشنری خالی برای آن می‌سازیم تا مقادیر فرزند (query, yearRange, maxResults) را داخلش نگهداری کنیم.
        """
        self.current_search = {}

    def exitSearch(self, ctx):
        """
        وقتی از بلاک search خارج شدیم، دیکشنری ساخته‌شده را در dsl_config ذخیره می‌کنیم.
        """
        self.dsl_config['search'] = self.current_search
        self.current_search = None

    def exitQuery(self, ctx):
        """
        query: 'query' LB STRING (',' STRING)* RB mandatory_nl;
        تمام STRING ها را (بدون نقل قول) در قالب یک لیست ذخیره می‌کنیم.
        """
        raw_strings = [s.getText() for s in ctx.STRING()]
        queries = [rs.strip('"') for rs in raw_strings]
        self.current_search['queries'] = queries

    def exitYearRange(self, ctx):
        """
        yearRange: 'year_range' NUMBER 'to' NUMBER mandatory_nl;
        دو عدد (سال شروع و سال پایان) را خوانده و در یک تاپل قرار می‌دهیم.
        """
        start_year = int(ctx.NUMBER(0).getText())
        end_year = int(ctx.NUMBER(1).getText())
        self.current_search['year_range'] = (start_year, end_year)

    def exitMaxResults(self, ctx):
        """
        maxResults: 'max_results' NUMBER mandatory_nl;
        تعداد حداکثر مقالات را می‌گیریم.
        """
        self.current_search['max_results'] = int(ctx.NUMBER().getText())

    # ------------------------------------------------------------------------
    # filters: 'filters' LCB optional_nl excludeKeywords minPages languages RCB optional_nl;
    #   excludeKeywords: 'exclude_keywords' LB STRING (',' STRING)* RB mandatory_nl;
    #   minPages: 'min_pages' NUMBER mandatory_nl;
    #   languages: 'languages' LB LN (',' LN)* RB mandatory_nl;
    # ------------------------------------------------------------------------
    def enterFilters(self, ctx):
        self.current_filters = {}

    def exitFilters(self, ctx):
        self.dsl_config['filters'] = self.current_filters
        self.current_filters = None

    def exitExcludeKeywords(self, ctx):
        """
        excludeKeywords: 'exclude_keywords' LB STRING (',' STRING)* RB mandatory_nl;
        """
        raw_strings = [s.getText() for s in ctx.STRING()]
        keywords = [rs.strip('"') for rs in raw_strings]
        self.current_filters['exclude_keywords'] = keywords

    def exitMinPages(self, ctx):
        """
        minPages: 'min_pages' NUMBER mandatory_nl;
        """
        self.current_filters['min_pages'] = int(ctx.NUMBER().getText())

    def exitLanguages(self, ctx):
        """
        languages: 'languages' LB LN (',' LN)* RB mandatory_nl;
        LN: '"en"' | '"fa"';
        """
        raw_lns = [ln.getText() for ln in ctx.LN()]
        # هر LN شبیه "en" یا "fa" است و باید نقل‌قول آن حذف شود:
        languages = [s.strip('"') for s in raw_lns]
        self.current_filters['languages'] = languages

    # ------------------------------------------------------------------------
    # analyze: 'analyze' LCB optional_nl summarize extractFields keywordCloud RCB optional_nl;
    #   summarize: 'summarize' LCB optional_nl method maxLength RCB mandatory_nl;
    #   extractFields: 'extract_fields' LB STRING (',' STRING)* RB mandatory_nl;
    #   keywordCloud: 'keyword_cloud' BOOLEAN mandatory_nl;
    # ------------------------------------------------------------------------
    def enterAnalyze(self, ctx):
        self.current_analyze = {}

    def exitAnalyze(self, ctx):
        self.dsl_config['analyze'] = self.current_analyze
        self.current_analyze = None

    def enterSummarize(self, ctx):
        self.current_summarize = {}

    def exitSummarize(self, ctx):
        """
        پس از اتمام بلاک summarize، دیکشنری داخل current_summarize را در داخل self.current_analyze می‌گذاریم.
        """
        self.current_analyze['summarize'] = self.current_summarize
        self.current_summarize = None

    def exitMethod(self, ctx):
        """
        method: 'method' METHID mandatory_nl;
        METHID: '"gpt-4"' | '"textrank"';
        """
        raw_method = ctx.METHID().getText()  # مثلا "gpt-4" همراه با نقل‌قول
        method_str = raw_method.strip('"')
        self.current_summarize['method'] = method_str

    def exitMaxLength(self, ctx):
        """
        maxLength: 'max_length' NUMBER mandatory_nl;
        """
        self.current_summarize['max_length'] = int(ctx.NUMBER().getText())

    def exitExtractFields(self, ctx):
        """
        extractFields: 'extract_fields' LB STRING (',' STRING)* RB mandatory_nl;
        """
        raw_strings = [s.getText() for s in ctx.STRING()]
        fields = [rs.strip('"') for rs in raw_strings]
        self.current_analyze['extract_fields'] = fields

    def exitKeywordCloud(self, ctx):
        """
        keywordCloud: 'keyword_cloud' BOOLEAN mandatory_nl;
        BOOLEAN: 'true' | 'false';
        """
        raw_bool = ctx.BOOLEAN().getText()
        bool_val = (raw_bool == 'true')
        self.current_analyze['keyword_cloud'] = bool_val

    # ------------------------------------------------------------------------
    # report: 'report' LCB optional_nl format includeMetadata outputPath RCB optional_nl;
    #   format: 'format' FORMAT mandatory_nl;
    #   includeMetadata: 'include_metadata' BOOLEAN mandatory_nl;
    #   outputPath: 'output_path' STRING mandatory_nl;
    # ------------------------------------------------------------------------
    def enterReport(self, ctx):
        self.current_report = {}

    def exitReport(self, ctx):
        self.dsl_config['report'] = self.current_report
        self.current_report = None

    def exitFormat(self, ctx):
        """
        format: 'format' FORMAT mandatory_nl;
        FORMAT: '"markdown"' | '"pdf"';
        """
        raw_format = ctx.FORMAT().getText()  # مثلا "markdown"
        format_str = raw_format.strip('"')
        self.current_report['format'] = format_str

    def exitIncludeMetadata(self, ctx):
        """
        includeMetadata: 'include_metadata' BOOLEAN mandatory_nl;
        """
        raw_bool = ctx.BOOLEAN().getText()
        bool_val = (raw_bool == 'true')
        self.current_report['include_metadata'] = bool_val

    def exitOutputPath(self, ctx):
        """
        outputPath: 'output_path' STRING mandatory_nl;
        """
        raw_str = ctx.STRING().getText()
        path_str = raw_str.strip('"')
        self.current_report['output_path'] = path_str
