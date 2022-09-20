from abc import ABC
from Compiler.Tree.base_node import AST


class BinOP(AST, ABC):
    """
           base class for the binary operators plus,minus,divide...
    """

    def __init__(self, left: AST, op, right: AST):
        self.left = left
        self.token = self.op = op
        self.right = right
