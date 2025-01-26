from gen.SlrListener import SlrListener
from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree


class SlrCustomListener(SlrListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names

        # بخش مربوط به DSL config (که قبلاً داشتید)
        self.dsl_config = {}
        self.current_search = None
        self.current_filters = None
        self.current_analyze = None
        self.current_summarize = None
        self.current_report = None

        # ساخت یک شیء AST از کلاس AST (در فایل ast.py)
        self.ast = AST()
        # فعلاً در اینجا کاری با root انجام نمی‌دهیم
        # زیرا تابع make_ast_subtree در هر exitXXX به‌صورت خودکار
        # درخت را بر اساس ctx می‌سازد و مقدار root را به‌روزرسانی می‌کند.

    # --------------------- برنامه اصلی ---------------------
    # program: topic search filters analyze report;
    def exitProgram(self, ctx):
        """
        وقتی rule برنامه تمام می‌شود، می‌خواهیم یک زیردرخت با ریشه 'program' بسازیم.
        """
        make_ast_subtree(self.ast, ctx, "program", keep_node=False)

    # --------------------- topic: 'topic ' STRING mandatory_nl; ---------------------
    def exitTopic(self, ctx):
        """
        از روی TOKEN مربوط به STRING متن تاپیک را استخراج می‌کنیم.
        در dsl_config ذخیره می‌شود.
        سپس زیردرخت مربوط به 'topic' را می‌سازیم.
        """
        raw_str = ctx.STRING().getText()
        topic_str = raw_str.strip('"')
        self.dsl_config['topic'] = topic_str

        # ساخت زیردرخت AST برای این rule
        make_ast_subtree(self.ast, ctx, "topic", keep_node=False)

    # --------------------- search ---------------------
    # search: 'search' LCB optional_nl query yearRange maxResults RCB optional_nl;
    def enterSearch(self, ctx):
        self.current_search = {}

    def exitSearch(self, ctx):
        self.dsl_config['search'] = self.current_search
        self.current_search = None

        make_ast_subtree(self.ast, ctx, "search", keep_node=False)

    # query: 'query' LB STRING (',' STRING)* RB mandatory_nl;
    def exitQuery(self, ctx):
        raw_strings = [s.getText() for s in ctx.STRING()]
        queries = [rs.strip('"') for rs in raw_strings]
        self.current_search['queries'] = queries

        make_ast_subtree(self.ast, ctx, "query", keep_node=False)

    # yearRange: 'year_range' NUMBER 'to' NUMBER mandatory_nl;
    def exitYearRange(self, ctx):
        start_year = int(ctx.NUMBER(0).getText())
        end_year = int(ctx.NUMBER(1).getText())
        self.current_search['year_range'] = (start_year, end_year)

        make_ast_subtree(self.ast, ctx, "year_range", keep_node=False)

    # maxResults: 'max_results' NUMBER mandatory_nl;
    def exitMaxResults(self, ctx):
        self.current_search['max_results'] = int(ctx.NUMBER().getText())

        make_ast_subtree(self.ast, ctx, "max_results", keep_node=False)

    # --------------------- filters ---------------------
    # filters: 'filters' LCB optional_nl excludeKeywords minPages languages RCB optional_nl;
    def enterFilters(self, ctx):
        self.current_filters = {}

    def exitFilters(self, ctx):
        self.dsl_config['filters'] = self.current_filters
        self.current_filters = None

        make_ast_subtree(self.ast, ctx, "filters", keep_node=False)

    # excludeKeywords: 'exclude_keywords' LB STRING (',' STRING)* RB mandatory_nl;
    def exitExcludeKeywords(self, ctx):
        raw_strings = [s.getText() for s in ctx.STRING()]
        keywords = [rs.strip('"') for rs in raw_strings]
        self.current_filters['exclude_keywords'] = keywords

        make_ast_subtree(self.ast, ctx, "exclude_keywords", keep_node=False)

    # minPages: 'min_pages' NUMBER mandatory_nl;
    def exitMinPages(self, ctx):
        self.current_filters['min_pages'] = int(ctx.NUMBER().getText())

        make_ast_subtree(self.ast, ctx, "min_pages", keep_node=False)

    # languages: 'languages' LB LN (',' LN)* RB mandatory_nl;
    def exitLanguages(self, ctx):
        raw_lns = [ln.getText() for ln in ctx.LN()]
        languages = [s.strip('"') for s in raw_lns]
        self.current_filters['languages'] = languages

        make_ast_subtree(self.ast, ctx, "languages", keep_node=False)

    # --------------------- analyze ---------------------
    # analyze: 'analyze' LCB optional_nl summarize extractFields keywordCloud RCB optional_nl;
    def enterAnalyze(self, ctx):
        self.current_analyze = {}

    def exitAnalyze(self, ctx):
        self.dsl_config['analyze'] = self.current_analyze
        self.current_analyze = None

        make_ast_subtree(self.ast, ctx, "analyze", keep_node=False)

    # summarize: 'summarize' LCB optional_nl method maxLength RCB mandatory_nl;
    def enterSummarize(self, ctx):
        self.current_summarize = {}

    def exitSummarize(self, ctx):
        self.current_analyze['summarize'] = self.current_summarize
        self.current_summarize = None

        make_ast_subtree(self.ast, ctx, "summarize", keep_node=False)

    # method: 'method' METHID mandatory_nl;
    def exitMethod(self, ctx):
        raw_method = ctx.METHID().getText()
        method_str = raw_method.strip('"')
        self.current_summarize['method'] = method_str

        make_ast_subtree(self.ast, ctx, "method", keep_node=False)

    # maxLength: 'max_length' NUMBER mandatory_nl;
    def exitMaxLength(self, ctx):
        self.current_summarize['max_length'] = int(ctx.NUMBER().getText())

        make_ast_subtree(self.ast, ctx, "max_length", keep_node=False)

    # extractFields: 'extract_fields' LB STRING (',' STRING)* RB mandatory_nl;
    def exitExtractFields(self, ctx):
        raw_strings = [s.getText() for s in ctx.STRING()]
        fields = [rs.strip('"') for rs in raw_strings]
        self.current_analyze['extract_fields'] = fields

        make_ast_subtree(self.ast, ctx, "extract_fields", keep_node=False)

    # keywordCloud: 'keyword_cloud' BOOLEAN mandatory_nl;
    def exitKeywordCloud(self, ctx):
        raw_bool = ctx.BOOLEAN().getText()
        bool_val = (raw_bool == 'true')
        self.current_analyze['keyword_cloud'] = bool_val

        make_ast_subtree(self.ast, ctx, "keyword_cloud", keep_node=False)

    # --------------------- report ---------------------
    # report: 'report' LCB optional_nl format includeMetadata outputPath RCB optional_nl;
    def enterReport(self, ctx):
        self.current_report = {}

    def exitReport(self, ctx):
        self.dsl_config['report'] = self.current_report
        self.current_report = None

        make_ast_subtree(self.ast, ctx, "report", keep_node=False)

    # format: 'format' FORMAT mandatory_nl;
    def exitFormat(self, ctx):
        raw_format = ctx.FORMAT().getText()
        format_str = raw_format.strip('"')
        self.current_report['format'] = format_str

        make_ast_subtree(self.ast, ctx, "format", keep_node=False)

    # includeMetadata: 'include_metadata' BOOLEAN mandatory_nl;
    def exitIncludeMetadata(self, ctx):
        raw_bool = ctx.BOOLEAN().getText()
        bool_val = (raw_bool == 'true')
        self.current_report['include_metadata'] = bool_val

        make_ast_subtree(self.ast, ctx, "include_metadata", keep_node=False)

    # outputPath: 'output_path' STRING mandatory_nl;
    def exitOutputPath(self, ctx):
        raw_str = ctx.STRING().getText()
        path_str = raw_str.strip('"')
        self.current_report['output_path'] = path_str

        make_ast_subtree(self.ast, ctx, "output_path", keep_node=False)
