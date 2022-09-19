from abc import ABC

from Compiler.Tree.AST import AST


class BinOP(AST, ABC):
    def __init__(self, left: AST, op, right: AST):
        self.left = left
        self.token = self.op = op
        self.right = right
