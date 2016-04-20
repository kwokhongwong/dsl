# Generated from dsl.g4 by ANTLR 4.5.3
from antlr4 import *
from dsl.dslVisitor import dslVisitor
if __name__ is not None and "." in __name__:
    from .dslParser import dslParser
else:
    from dslParser import dslParser

# This class defines a complete generic visitor for a parse tree produced by dslParser.
from constants import Operation
from model.query import DataRequest, QueryDefinition, TimeSeries


class dslVisitorOverride(dslVisitor):

    _symbol_table = {}
    _data_request = None
    _debug = False
    
    def setDebug(self, debug=False):
        self._debug = debug

    # Visit a parse tree produced by dslParser#expression.
    def visitExpression(self, ctx:dslParser.ExpressionContext):
        if self._debug:
            print('visitExpression : %s'%ctx.getText())
        query_definition = QueryDefinition()
        self._symbol_table['query_definition'] = query_definition
        output_format = ctx.output().getText() if ctx.output() else None
        self._symbol_table['output_format'] = output_format
        self._data_request = DataRequest(query_definition=query_definition, output_format=output_format)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#output.
    def visitOutput(self, ctx:dslParser.OutputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#command.
    def visitCommand(self, ctx:dslParser.CommandContext):
        if self._debug:
            print('visitCommand : %s'%ctx.getText())
        title = ctx.TITLE().getText().replace('"','') if ctx.TITLE() else None
        data_id = ctx.TEXT().getText()
        time_series = TimeSeries(database='FRED', data_id=data_id, data_source='quandl', title=title)
        self._symbol_table['query_definition'].add_time_series(time_series_id=data_id, time_series=time_series)
        self._symbol_table['time_series'] = time_series
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#operation.
    def visitOperation(self, ctx:dslParser.OperationContext):
        if self._debug:
            print('visitOperation : %s'%ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#graph.
    def visitGraph(self, ctx:dslParser.GraphContext):
        if self._debug:
            print('visit : %s'%ctx.getText())
        if len(ctx.graph_arg()) == 0:
            self._symbol_table['time_series'].add_operation(operation=Operation.graph, operation_arg=None)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#graph_arg.
    def visitGraph_arg(self, ctx:dslParser.Graph_argContext):
        if self._debug:
            print('visitGraph_arg : %s'%ctx.getText())
        self._symbol_table['time_series'].add_operation(operation=Operation.graph, operation_arg=ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#table.
    def visitTable(self, ctx:dslParser.TableContext):
        if self._debug:
            print('visitTable : %s'%ctx.getText())
        self._symbol_table['time_series'].add_operation(operation=Operation.table, operation_arg=None)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#table_arg.
    def visitTable_arg(self, ctx:dslParser.Table_argContext):
        if self._debug:
            print('visitTable_arg : %s'%ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#stats.
    def visitStats(self, ctx:dslParser.StatsContext):
        if self._debug:
            print('visitStats : %s'%ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dslParser#stats_arg.
    def visitStats_arg(self, ctx:dslParser.Stats_argContext):
        if self._debug:
            print('visitStats_arg : %s'%ctx.getText())
        self._symbol_table['time_series'].add_operation(operation=Operation.stats, operation_arg=ctx.getText())
        return self.visitChildren(ctx)


del dslParser