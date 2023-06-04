import sys
from pprint import PrettyPrinter
from arith_grammar import ArithGrammar
from arith_eval import ArithEval

pp = PrettyPrinter(sort_dicts=False)  # Instancia PrettyPrinter para exibir resultados formatados
lg = ArithGrammar()  # Instancia ArithGrammar para análise sintática
lg.build()  # Constrói a gramática e o lexer

if len(sys.argv) == 2:  # Verifica se foi fornecido um arquivo de entrada
    with open(sys.argv[1], 'r') as file:
        contents = file.read()
        try:
            ast_tree = lg.parse(contents)  # Realiza o parsing do conteúdo do arquivo
            result = ArithEval().evaluate(ast_tree)  # Avalia a árvore de análise sintática
            pp.pprint(result)  # Exibe o resultado formatado
        except Exception as e:
            print(f'Error: {e}')  # Exibe uma mensagem de erro caso ocorra uma exceção durante o parsing ou avaliação
else:
    while True:
        try:
            string = input('> ')  # Lê uma expressão a partir da entrada do usuário
            ast_tree = lg.parse(string)  # Realiza o parsing da expressão
            result = ArithEval().evaluate(ast_tree)  # Avalia a árvore de análise sintática
            pp.pprint(result)  # Exibe o resultado formatado
        except EOFError:
            break  # Encerra o loop caso o usuário insira o fim de arquivo (Ctrl + D)
        except Exception as e:
            print(f'Error: {e}')  # Exibe uma mensagem de erro caso ocorra uma exceção durante o parsing ou avaliação
