# arith_lexer.py
import ply.lex as lex

class ArithLexer:
    tokens = ('NUMBER', 'VARID', 'ESCREVER', 'ASSIGN')
    literals = ['*', '+', '-', '(', ')', ';']

    def __init__(self):
        self.lexer = None

    def t_NUMBER(self, t):
        r'\d+'  # Expressão regular para números inteiros
        t.value = int(t.value)  # Converte o valor para um inteiro
        return t
    
    def t_ESCREVER(self, t):
        r"ESC(REVER)?" 
        return t

    def t_VARID(self, t):# Expressão para reconhecer variáveis (sequência de letras maiúsculas)
        r'[A-Z]+'
        return t
    
    def t_ASSIGN(self, t):
        r":=" 
        return t

    t_ignore = ' \t'  # Caracteres a serem ignorados pelo lexer

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)  # Constrói o lexer usando as definições e as opções fornecidas

    def input(self, string):
        self.lexer.input(string)  # Define a entrada do lexer como a string fornecida

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type  # Retorna o próximo token da entrada fornecida
    
    def t_error(self, t):
        print(f'Unexpected token: {t.value[:10]}')
        t.lexer.skip(1)  # Ignora o token não esperado

