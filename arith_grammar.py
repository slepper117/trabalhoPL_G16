import ply.yacc as yacc
from arith_lexer import ArithLexer


class ArithGrammar:
    tokens = ArithLexer.tokens

    # Definição da precedência dos operadores
    precedence = (
        ('left', '+', '-'),  # Precedência dos operadores de adição e subtração
        ('left', '*'),  # Precedência do operador de multiplicação
        ("right", 'simetrico'),  # Precedência do operador unário de negação
    )

    def __init__(self):
        self.tokens = ArithLexer.tokens
        self.lexer = ArithLexer()
        self.parser = None

    def build(self, **kwargs):
        self.lexer.build(**kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.parser.parse(lexer=self.lexer.lexer)

    # Regra de produção para a instrução principal
    def p_s(self, p):
        """S : LstV ';'"""
        p[0] = p[1]

    # Regra de produção para uma lista de variáveis e instruções
    def p_lstv_inst(self, p):
        """LstV : LstV ';' Inst"""
        p[0] = {'op': 'seq', 'args': p[1]['args'] + [p[3]]}

    # Regra de produção para uma única instrução
    def p_lstv_inst_single(self, p):
        """LstV : Inst"""
        p[0] = {'op': 'seq', 'args': [p[1]]}

    # Regra de produção para uma instrução de atribuição
    def p_inst_atr(self, p):
        """Inst : V"""
        p[0] = p[1]

    # Regra de produção para uma instrução de escrita
    def p_inst_esc(self, p):
        """Inst : ESCREVER expression"""
        p[0] = {'op': 'esc', 'args': [p[2]]}

    # Regra de produção para uma variável
    def p_v_atrib(self, p):
        """V : VARID ASSIGN expression"""
        p[0] = {'op': 'atr', 'args': [p[1], p[3]]}

    # Regra de produção para expressões binárias (+, -, *)
    def p_expression_binary(self, p):
        """expression : expression '+' expression
                      | expression '-' expression
                      | expression '*' expression"""
        p[0] = {'op': p[2], 'args': [p[1], p[3]]}

    # Regra de produção para uma expressão unária (-)
    def p_expression_unary(self, p):
        """expression : '-' expression %prec simetrico"""
        p[0] = {'op': p[1], 'args': [p[2]]}

    # Regra de produção para expressões entre parênteses
    def p_expression_parens(self, p):
        """expression : '(' expression ')'"""
        p[0] = p[2]

    # Regra de produção para um número
    def p_expression_number(self, p):
        """expression : NUMBER"""
        p[0] = p[1]

    # Regra de produção para um identificador de variável
    def p_expression_varid(self, p):
        """expression : VARID"""
        p[0] = {'var': p[1]}

    # Tratamento de erros sintáticos
    def p_error(self, p):
        if p:
            print(f'Syntax error at token {p.type}')
            exit(1)
        else:
            print('Syntax error: unexpected end of file')
            exit(1)

