# Generated from /home/themhh/git/SLR-Compiler-Project/Grammar/Slr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SlrParser import SlrParser
else:
    from SlrParser import SlrParser

# This class defines a complete generic visitor for a parse tree produced by SlrParser.

class SlrVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SlrParser#start.
    def visitStart(self, ctx:SlrParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#program.
    def visitProgram(self, ctx:SlrParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#topic.
    def visitTopic(self, ctx:SlrParser.TopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#search.
    def visitSearch(self, ctx:SlrParser.SearchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#query.
    def visitQuery(self, ctx:SlrParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#yearRange.
    def visitYearRange(self, ctx:SlrParser.YearRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#maxResults.
    def visitMaxResults(self, ctx:SlrParser.MaxResultsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#filters.
    def visitFilters(self, ctx:SlrParser.FiltersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#excludeKeywords.
    def visitExcludeKeywords(self, ctx:SlrParser.ExcludeKeywordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#minPages.
    def visitMinPages(self, ctx:SlrParser.MinPagesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#languages.
    def visitLanguages(self, ctx:SlrParser.LanguagesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#analyze.
    def visitAnalyze(self, ctx:SlrParser.AnalyzeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#summarize.
    def visitSummarize(self, ctx:SlrParser.SummarizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#method.
    def visitMethod(self, ctx:SlrParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#maxLength.
    def visitMaxLength(self, ctx:SlrParser.MaxLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#extractFields.
    def visitExtractFields(self, ctx:SlrParser.ExtractFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#keywordCloud.
    def visitKeywordCloud(self, ctx:SlrParser.KeywordCloudContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#report.
    def visitReport(self, ctx:SlrParser.ReportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#format.
    def visitFormat(self, ctx:SlrParser.FormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#includeMetadata.
    def visitIncludeMetadata(self, ctx:SlrParser.IncludeMetadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#outputPath.
    def visitOutputPath(self, ctx:SlrParser.OutputPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#optional_nl.
    def visitOptional_nl(self, ctx:SlrParser.Optional_nlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlrParser#mandatory_nl.
    def visitMandatory_nl(self, ctx:SlrParser.Mandatory_nlContext):
        return self.visitChildren(ctx)



del SlrParser