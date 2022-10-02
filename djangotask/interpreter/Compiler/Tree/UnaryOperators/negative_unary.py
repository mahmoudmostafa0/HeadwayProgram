from interpreter.Compiler.Tree.UnaryOperators.unary_operator import UnaryOP
from interpreter.Compiler.token import Token, TokenType


class NegativeUnary(UnaryOP):
    """class that is used to add a negative unary number"""

    def __init__(self, value):
        super().__init__(Token(TokenType.PLUS, value), value)

    def getvalue(self):
        """
        negation of the current value
        Returns:
        -ve value of the node
        """
        return -self.expr.getvalue()
