# Generated from dsl.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dslParser import dslParser
else:
    from dslParser import dslParser

# This class defines a complete generic visitor for a parse tree produced by dslParser.

class dslVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by dslParser#expression.
    def visitExpression(self, ctx:dslParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#output.
    def visitOutput(self, ctx:dslParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#command.
    def visitCommand(self, ctx:dslParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#operation.
    def visitOperation(self, ctx:dslParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#graph.
    def visitGraph(self, ctx:dslParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#graph_arg.
    def visitGraph_arg(self, ctx:dslParser.Graph_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#table.
    def visitTable(self, ctx:dslParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#table_arg.
    def visitTable_arg(self, ctx:dslParser.Table_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#stats.
    def visitStats(self, ctx:dslParser.StatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#stats_arg.
    def visitStats_arg(self, ctx:dslParser.Stats_argContext):
        return self.visitChildren(ctx)



del dslParser