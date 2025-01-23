# Generated from E:/University/Semester6/Compiler/SLR-Compiler-Project/Grammar/Slr.g4 by ANTLR 4.13.1
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



del SlrParser