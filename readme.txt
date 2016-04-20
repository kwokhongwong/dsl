[Package Info]

Tested against CPython '3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 19:28:18) [MSC v.1600 32 bit (Intel)]'

Packages used during development
- https://pypi.python.org/pypi/antlr4-python3-runtime/4.5.2.1/ (antlr4-python3-runtime-4.5.2.1.tar.gz)
- https://pypi.python.org/pypi/Quandl/2.8.9 (Quandl-2.8.9.tar.gz)
- https://pypi.python.org/pypi/pandas/0.17.1/
- https://pypi.python.org/pypi/numpy/1.10.4
- https://pypi.python.org/pypi/matplotlib/1.5.1

Linuxbrew packages:
- http://braumeister.org/search/antlr


[To Run]

See unit tests held in the tests folder e.g. tests.test_dsl.py
- Example outputs in /tests/tmp i.e. outputs are saved to file
- The Quandl authtoken is currently hard-coded in lib.adapters.py (as it's a toy :)


[Notes]

1. Approach taken was to build a toy model, with a thin DSL facade on top. This decouples the DSL considerations/movement from the core model.
- So there are separate unittests i.e. tests.test_dsl.py, tests.test_formatters.py and tests.test_model.py.
- Allows freedom of evolution/testing by each of these separate components
- As the DSL layer is separate, it would be trivial to build other interfaces into the core model e.g. microservice, access from Excel (e.g. using XLLoop)
- Not within the toy demo scope, but it would be fun to look at Jupyter/plotly integration

2. I used http://www.antlr.org/ (Recursive Descent Parser) to generate a lexer and parser (visitor) file after hand-crafting a dsl.g4 grammar file (see antlr4 generated files in dsl folder). The antlr4 grammer file looks like this:
- Note the original EBNF spec looked incomplete, so I've taken the liberty to define the table rule and fix what appeared to be a bug on the stats rule i.e. see stats and stats_arg
- See dsl.dslVisitorOverride.py to see how the model is populated i.e. I opted for the Visitor pattern implementation over the Listener.
- Generation of dslLexer.py and dslVisitor.py requires the antlr Java package, the antlr homepage 'Quick Start' instructions defines what to do
- The various antlr test tools (ANTLRWorks and TestRig) are pretty cool e.g. visual graphs of DSL
- I used a symbol map within the Parser to support construction of the model as the stream of tokens are processed

grammar dsl;
options {
        language=Python3;
}
expression : (output)? command (';' command)* ;
output : 'html'|'pdf' ;
command : TITLE operation (',' operation)* TEXT;
TITLE 	: '"' ( '\\' [\\"] | ~[\\"\r\n] )* '"';
operation 	:	graph|table|stats;
graph : 'g'('?'graph_arg ('|' graph_arg)*)? ;
graph_arg : 'scale_log' | 'monthly' ;
table : 't'('?'table_arg ('|' table_arg)*)? ;
table_arg : 'scale_log' | 'monthly' ;
stats : 's'('?'stats_arg)? ;
stats_arg : 'count' | 'sum' | 'mean' | 'median' | 'min' | 'max' | 'std' ;
TEXT : ('a'..'z'|'A'..'Z'|'0'..'9')+ ;	
WS 	:	[ ] -> skip ;

3. The core OM, see model.query.py, is simple and is comprised of the following objects
- TimeSeries i.e. defines quandl query parameters along with operations, an operation is defined as operation and operation_arg e.g. operation=g and operation_arg=scale_log
- QueryDefinition is a container for multiple TimeSeries
- DataRequest holds a single QueryDefinition along with the required output format i.e. html or pdf.
- Data adapters (currently only quandl) are defined in lib.adapters.py. Implementations are hidden behind a factory.
- Formatters (for the various permuations of html/pdf for each time series operations) is defined in lib.formatters.py. Implementations are hidden behind a factory.

4. I used pandas as the core data library to provide all the required data operations, coupled with matplotlib this also gives the required plot permutations.
- The outputs are basic but okay for a toy model, although pdf output of tables needs to be looked at.
- Any data aggregation/calculation is handled during the format phase, this could be extended should we need operations beyond the capabilities of pandas
- The operations are essentially modelled as an internal DSL

5. If I had more time...
- Currently the model is stateless, explore usage patterns to assess need for memoization/IO threading etc
- Validation in the model
- Extend DSL specification to allow date ranges etc
- Debuggability between the external DSL and model
- Look at providing integration with plotly