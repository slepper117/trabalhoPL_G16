# Arith_lexer.py
import ply.lex as plex

class ArithLexer:
    tokens= ('ESCREVER', 'VAR', 'VARID', 'NUMBER', 'STRING', 'ASSIGN', 'COMMA')
    literals = ['*', '+', '(', ')', '-', ';']
    t_ignore = ' \t\n'

    def __init__(self):
        self.lexer = None

    # Expressão regular para reconhecer a palavra ESCREVER
    def t_ESCREVER(self, t):
        r'ESC(REVER)?' 
        return t

    # Expressão regular para reconhecer a palavra ESCREVER
    def t_VAR(self, t):
        r'VAR' 
        return t
    
    # Expressão regular para reconhecer todas as palavras de A a Z
    def t_VARID(self, t):
        r'[a-z]+' 
        return t

    # Expressão regular para reconhecer numeros inteiros
    def t_NUMBER(self, t):
        r'[0-9]+'
        t.value = int (t.value)
        return t
    
    # Expressão regular para reconhecer caracteres dentro de ""
    def t_STRING(self, t):
        r'"[^"]*"' 
        t.value = t.value[1:-1]
        return t
    
    # Expressão regular para recohecer o simbolo =
    def t_ASSIGN(self, t):
        r'=' 
        return t
    
    # Expressão regular para reconhecer o simbolo ,
    def t_COMMA(self, t):
        r','
        return t
    
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    # Define a entrada do lexer como a string fornecida
    def input(self, string):
        self.lexer.input(string)

    # Retorna o próximo token da entrada fornecida
    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type 

     # Ignora o token não esperado
    def t_error(self, t):
        print(f'Unexpected token: [{t.value[:10]}]')
        exit(1)
