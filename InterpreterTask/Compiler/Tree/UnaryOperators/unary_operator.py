from abc import ABC

from Compiler.Tree.base_node import AST
from Compiler.token import Token


class UnaryOP(AST, ABC):
    """
    class that is used as a base class for unary operators
    """
    def __init__(self, operator:Token, expr: AST):
        self.token = self.operator = operator
        self.expr = expr
