from abc import ABC

from Compiler.Tree.base_node import AST


class UnaryOP(AST, ABC):
    """
    class that is used as a base class for unary operators
    """
    def __init__(self, operator, expr: AST):
        self.token = self.operator = operator
        self.expr = expr
