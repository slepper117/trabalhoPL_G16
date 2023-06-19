# arith_grammar.py
import ply.yacc as pyacc
from arith_lexer import ArithLexer

class ArithGrammar:
    precedence = (
        # Precedência dos operadores de adição e subtração
        ('left' , '+', '-'),
        # Precedência do operador de multiplicação
        ("left", '*'),
        # Precedência do operador unário de negação
        ("right", 'simetrico' ),
        )
    
    def __init__(self):
        self.tokens = ArithLexer.tokens
        self.lexer = ArithLexer()
        self.parser = None

    def build(self, **kwargs):
        self.lexer.build(**kwargs)
        self.parser = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.parser.parse(lexer=self.lexer.lexer)

    # Regra de produção para a instrução principal
    def p_s(self, p):
        """ S : expressions ';' """
        p[0] = p[1]

    # Regra de produção de varias expressoes
    def p_expr_tail(self, p):
        """ expressions :  expressions ';' expression """
        lstArgs = p[1]['args']
        lstArgs.append(p[3])
        p[0] = dict(op='seq', args = lstArgs)

    # Regra de produção de uma unica expressao
    def p_expr_head(self, p):  
        """ expressions :  expression """
        p[0] = dict(op='seq', args= [ p[1] ])
    
    # Regra para expressão ESCREVER
    def p_expr_escrever(self, p):
        """ expression : ESCREVER arguments """
        p[0] = dict(op='esc', args = [ p[2] ])

    # Regra para varios argumentos
    def p_expr_escrever_args_multiple(self, p):
        """ arguments : arguments COMMA argument """
        lstArgs = p[1]['args']
        lstArgs.append(p[3])
        p[0] = dict(op='esc', args = lstArgs)

    # Regra para um argumento
    def p_expr_escrever_args_single(self, p):
        """ arguments : argument """
        p[0] = dict(op='esc', args = [ p[1] ])

    # Reconhecer numeros no argumento
    def p_expr_escrever_args_number(self, p):
        """ argument : NUMBER """
        p[0] = p[1]

    # Reconhecer strings no argumento
    def p_expr_escrever_args_string(self, p):
        """ argument : STRING """
        p[0] = p[1]

    # Regra para expressão ESCREVER
    def p_expr_varid(self, p):
        """ expression : ESCREVER x """
        p[0] = dict(op='esc', args = [ p[2] ])

    # Regra de produção para uma variável
    def p_expr_varid_assign(self, p):
        """ expression : VAR VARID ASSIGN x """
        p[0] = dict(op='atr', args = [ p[2] , p[4]] )

    # Regra de produção para operações
    def p_expr_varid_op(self, p):
        """ x : x '+' x 
              | x '-' x 
              | x '*' x """ 
        p[0] = dict(op=p[2], args= [ p[1] , p[3] ])

    # Regra de produção para uma expressão unária (-)
    def p_expr_varid_neg(self, p): 
        """ x : '-' x %prec simetrico """
        p[0] = dict(op='-', args=[ p[2] ]) 

    # Regra de produção para expressões entre parênteses
    def p_expr_varid_parens(self, p):
        """ x : '(' x ')' """
        p[0] = p[2]

    # Regra de produção para um número
    def p_expr_varid_num(self, p):      
        """ x : NUMBER """
        p[0] = p[1] 
    # Regra de produção para um identificador de variável
    def p_expr_varid_var(self, p):
        """ x : VARID """
        p[0] = {'var': p[1] }

    # Tratamento de erros sintáticos
    def p_error(self, p):
        if p:
            print(f'Syntax error at token {p.type}')
            exit(1)
        else:
            print('Syntax error: unexpected end of file')
            exit(1)
