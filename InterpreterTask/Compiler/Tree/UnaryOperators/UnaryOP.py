from abc import ABC

from Compiler.Tree.AST import AST


class UnaryOP(AST, ABC):

    def __init__(self, op, expr: AST):
        self.token = self.op = op
        self.expr = expr
