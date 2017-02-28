%token_type int

expr(C) ::= SYM(A) PLUS SYM(B). { C = A + B; }
