from Compiler.Tree.BinaryOperators.BinOP import BinOP


class DivOP(BinOP):
    def getvalue(self):
        return self.left.getvalue() / self.right.getvalue()
