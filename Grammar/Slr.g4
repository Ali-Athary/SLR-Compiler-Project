grammar Slr;

start: program EOF;

program: 'slr';

WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;
