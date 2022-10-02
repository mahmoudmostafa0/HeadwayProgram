# from Compiler.lexer import Lexer
# from Compiler.parser import Parser
from interpreter.Compiler.lexer import Lexer
from interpreter.Compiler.parser import Parser


def interpret_kpi(kpi_eq: str):
    lexer = Lexer(kpi_eq)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    return result


class Interpreter:
    """
    Interpreter class to calculate the KPI expression
    """

    def __init__(self, parser):
        self.parser = parser

    def reset(self):
        """
        reset the interpreter
        """
        self.parser.reset()

    def interpret(self):
        """
        Calculate the value of parsed abstract syntax tree
        """
        tree = self.parser.parse()
        if tree is None:
            return ''
        return tree.getvalue()
