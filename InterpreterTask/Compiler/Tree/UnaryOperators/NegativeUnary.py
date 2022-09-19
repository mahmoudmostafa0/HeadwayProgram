from Compiler.Lexer import TokenType
from Compiler.Tree.UnaryOperators.UnaryOP import UnaryOP


class NegativeUnary(UnaryOP):
    def __int__(self, value):
        super().__int__(TokenType.PLUS, value)

    def getvalue(self):
        return -self.expr.getvalue()
