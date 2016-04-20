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
