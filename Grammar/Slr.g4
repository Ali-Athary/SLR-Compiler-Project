grammar Slr;

start: program EOF;

program: topic search filters analyze report;

topic: 'topic ' STRING mandatory_nl;

search: 'search' LCB optional_nl query yearRange maxResults RCB optional_nl;
query: 'query' LB STRING (',' STRING)* RB mandatory_nl;
yearRange: 'year_range' NUMBER 'to' NUMBER mandatory_nl;
maxResults: 'max_results' NUMBER mandatory_nl;

filters: 'filters' LCB optional_nl excludeKeywords minPages languages RCB optional_nl;
excludeKeywords: 'exclude_keywords' LB STRING (',' STRING)* RB mandatory_nl;
minPages: 'min_pages' NUMBER mandatory_nl;
languages: 'languages' LB LN (',' LN)* RB mandatory_nl;

analyze: 'analyze' LCB optional_nl summarize extractFields keywordCloud RCB optional_nl;
summarize: 'summarize' LCB optional_nl method maxLength RCB mandatory_nl;
method: 'method' METHID mandatory_nl;
maxLength: 'max_length' NUMBER mandatory_nl;
extractFields: 'extract_fields' LB STRING (',' STRING)* RB  mandatory_nl;
keywordCloud: 'keyword_cloud' BOOLEAN mandatory_nl;

report: 'report' LCB optional_nl format includeMetadata outputPath RCB optional_nl;
format: 'format' FORMAT mandatory_nl;
includeMetadata: 'include_metadata' BOOLEAN mandatory_nl;
outputPath: 'output_path' STRING mandatory_nl;

optional_nl : NEWLINE* ;
mandatory_nl : NEWLINE+ ;

METHID: '"gpt-4"' | '"textrank"';
FORMAT: '"markdown"' | '"pdf"';
LN: '"en"' | '"fa"';

BOOLEAN: 'true' | 'false';
NUMBER: DIGIT+;
DIGIT: [0-9];
STRING: '"' (~["] | '\\"')* '"';

LB: '[';
RB: ']';

LCB: '{';
RCB: '}';

COMMENT: '//' (~'\n')* -> skip;
NEWLINE : '\n' | '\r\n' ;
WS: [ \t\r]+ -> skip;
