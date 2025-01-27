# Generated from /home/themhh/git/SLR-Compiler-Project/Grammar/Slr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SlrParser import SlrParser
else:
    from SlrParser import SlrParser

# This class defines a complete listener for a parse tree produced by SlrParser.
class SlrListener(ParseTreeListener):

    # Enter a parse tree produced by SlrParser#start.
    def enterStart(self, ctx:SlrParser.StartContext):
        pass

    # Exit a parse tree produced by SlrParser#start.
    def exitStart(self, ctx:SlrParser.StartContext):
        pass


    # Enter a parse tree produced by SlrParser#program.
    def enterProgram(self, ctx:SlrParser.ProgramContext):
        pass

    # Exit a parse tree produced by SlrParser#program.
    def exitProgram(self, ctx:SlrParser.ProgramContext):
        pass


    # Enter a parse tree produced by SlrParser#topic.
    def enterTopic(self, ctx:SlrParser.TopicContext):
        pass

    # Exit a parse tree produced by SlrParser#topic.
    def exitTopic(self, ctx:SlrParser.TopicContext):
        pass


    # Enter a parse tree produced by SlrParser#search.
    def enterSearch(self, ctx:SlrParser.SearchContext):
        pass

    # Exit a parse tree produced by SlrParser#search.
    def exitSearch(self, ctx:SlrParser.SearchContext):
        pass


    # Enter a parse tree produced by SlrParser#query.
    def enterQuery(self, ctx:SlrParser.QueryContext):
        pass

    # Exit a parse tree produced by SlrParser#query.
    def exitQuery(self, ctx:SlrParser.QueryContext):
        pass


    # Enter a parse tree produced by SlrParser#yearRange.
    def enterYearRange(self, ctx:SlrParser.YearRangeContext):
        pass

    # Exit a parse tree produced by SlrParser#yearRange.
    def exitYearRange(self, ctx:SlrParser.YearRangeContext):
        pass


    # Enter a parse tree produced by SlrParser#maxResults.
    def enterMaxResults(self, ctx:SlrParser.MaxResultsContext):
        pass

    # Exit a parse tree produced by SlrParser#maxResults.
    def exitMaxResults(self, ctx:SlrParser.MaxResultsContext):
        pass


    # Enter a parse tree produced by SlrParser#filters.
    def enterFilters(self, ctx:SlrParser.FiltersContext):
        pass

    # Exit a parse tree produced by SlrParser#filters.
    def exitFilters(self, ctx:SlrParser.FiltersContext):
        pass


    # Enter a parse tree produced by SlrParser#excludeKeywords.
    def enterExcludeKeywords(self, ctx:SlrParser.ExcludeKeywordsContext):
        pass

    # Exit a parse tree produced by SlrParser#excludeKeywords.
    def exitExcludeKeywords(self, ctx:SlrParser.ExcludeKeywordsContext):
        pass


    # Enter a parse tree produced by SlrParser#minPages.
    def enterMinPages(self, ctx:SlrParser.MinPagesContext):
        pass

    # Exit a parse tree produced by SlrParser#minPages.
    def exitMinPages(self, ctx:SlrParser.MinPagesContext):
        pass


    # Enter a parse tree produced by SlrParser#languages.
    def enterLanguages(self, ctx:SlrParser.LanguagesContext):
        pass

    # Exit a parse tree produced by SlrParser#languages.
    def exitLanguages(self, ctx:SlrParser.LanguagesContext):
        pass


    # Enter a parse tree produced by SlrParser#analyze.
    def enterAnalyze(self, ctx:SlrParser.AnalyzeContext):
        pass

    # Exit a parse tree produced by SlrParser#analyze.
    def exitAnalyze(self, ctx:SlrParser.AnalyzeContext):
        pass


    # Enter a parse tree produced by SlrParser#summarize.
    def enterSummarize(self, ctx:SlrParser.SummarizeContext):
        pass

    # Exit a parse tree produced by SlrParser#summarize.
    def exitSummarize(self, ctx:SlrParser.SummarizeContext):
        pass


    # Enter a parse tree produced by SlrParser#method.
    def enterMethod(self, ctx:SlrParser.MethodContext):
        pass

    # Exit a parse tree produced by SlrParser#method.
    def exitMethod(self, ctx:SlrParser.MethodContext):
        pass


    # Enter a parse tree produced by SlrParser#maxLength.
    def enterMaxLength(self, ctx:SlrParser.MaxLengthContext):
        pass

    # Exit a parse tree produced by SlrParser#maxLength.
    def exitMaxLength(self, ctx:SlrParser.MaxLengthContext):
        pass


    # Enter a parse tree produced by SlrParser#extractFields.
    def enterExtractFields(self, ctx:SlrParser.ExtractFieldsContext):
        pass

    # Exit a parse tree produced by SlrParser#extractFields.
    def exitExtractFields(self, ctx:SlrParser.ExtractFieldsContext):
        pass


    # Enter a parse tree produced by SlrParser#keywordCloud.
    def enterKeywordCloud(self, ctx:SlrParser.KeywordCloudContext):
        pass

    # Exit a parse tree produced by SlrParser#keywordCloud.
    def exitKeywordCloud(self, ctx:SlrParser.KeywordCloudContext):
        pass


    # Enter a parse tree produced by SlrParser#report.
    def enterReport(self, ctx:SlrParser.ReportContext):
        pass

    # Exit a parse tree produced by SlrParser#report.
    def exitReport(self, ctx:SlrParser.ReportContext):
        pass


    # Enter a parse tree produced by SlrParser#format.
    def enterFormat(self, ctx:SlrParser.FormatContext):
        pass

    # Exit a parse tree produced by SlrParser#format.
    def exitFormat(self, ctx:SlrParser.FormatContext):
        pass


    # Enter a parse tree produced by SlrParser#includeMetadata.
    def enterIncludeMetadata(self, ctx:SlrParser.IncludeMetadataContext):
        pass

    # Exit a parse tree produced by SlrParser#includeMetadata.
    def exitIncludeMetadata(self, ctx:SlrParser.IncludeMetadataContext):
        pass


    # Enter a parse tree produced by SlrParser#outputPath.
    def enterOutputPath(self, ctx:SlrParser.OutputPathContext):
        pass

    # Exit a parse tree produced by SlrParser#outputPath.
    def exitOutputPath(self, ctx:SlrParser.OutputPathContext):
        pass


    # Enter a parse tree produced by SlrParser#optional_nl.
    def enterOptional_nl(self, ctx:SlrParser.Optional_nlContext):
        pass

    # Exit a parse tree produced by SlrParser#optional_nl.
    def exitOptional_nl(self, ctx:SlrParser.Optional_nlContext):
        pass


    # Enter a parse tree produced by SlrParser#mandatory_nl.
    def enterMandatory_nl(self, ctx:SlrParser.Mandatory_nlContext):
        pass

    # Exit a parse tree produced by SlrParser#mandatory_nl.
    def exitMandatory_nl(self, ctx:SlrParser.Mandatory_nlContext):
        pass



del SlrParser