from interpreter.Compiler.token import TokenType, Token

from interpreter.Compiler.Tree.UnaryOperators.unary_operator import UnaryOP


class PositiveUnary(UnaryOP):
    """
    class that is used to create a positive unary value node
    """
    def __init__(self, value):
        super().__init__(Token(TokenType.PLUS, value), value)

    def getvalue(self):
        """
        +ve value
        Returns:

        """
        return +self.expr.getvalue()
