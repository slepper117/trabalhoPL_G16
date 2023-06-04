# arith_eval

class ArithEval:
    symbols = {}  # Dicionário para armazenar as variáveis e seus valores

    operators = {
        "+": lambda args: args[0] + args[1],  # Operador de adição
        "-": lambda args: args[0] - args[1],  # Operador de subtração
        "*": lambda args: args[0] * args[1],  # Operador de multiplicação
        "seq": lambda args: args[-1],  # Operador de sequência (retorna o último valor)
        "atr": lambda args: ArithEval._attrib(args),  # Operador de atribuição
        "esc": lambda args: print(args[0]),  # Operador de escrita (imprime o valor)
    }

    @staticmethod
    def _attrib(args):
        value = args[1]  # Valor a ser atribuído
        ArithEval.symbols[args[0]] = value  # Atribui o valor à variável
        return None

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:  # Se for um número inteiro, retorna o próprio número
            return ast
        if type(ast) is dict:  # Se for um dicionário, é um operador
            return ArithEval._eval_operator(ast)
        if type(ast) is str:  # Se for uma string, é um identificador de variável
            return ast
        raise Exception(f"Unknown AST type")  # Tipo de AST desconhecido

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast:  # Verifica se o dicionário contém a chave 'op' (operador)
            op = ast["op"]  # Obtém o operador
            args = [ArithEval.evaluate(a) for a in ast['args']]  # Avalia os argumentos do operador
            if op in ArithEval.operators:  # Verifica se o operador está definido
                func = ArithEval.operators[op]  # Obtém a função associada ao operador
                return func(args)  # Executa a função com os argumentos
            else:
                raise Exception(f"Unknown operator {op}")  # Operador desconhecido
        if 'var' in ast:  # Verifica se o dicionário contém a chave 'var' (identificador de variável)
            varid = ast["var"]  # Obtém o identificador de variável
            if varid in ArithEval.symbols:  # Verifica se a variável está definida
                return ArithEval.symbols[varid]  # Retorna o valor da variável
            raise Exception(f"error: '{varid}' undeclared (first use in this function)")  # Variável não declarada
        raise Exception('Undefined AST')  # AST indefinida (caso não corresponda a nenhum caso acima)
