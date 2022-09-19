from Compiler.Tree.BinaryOperators.BinOP import BinOP


class MulOP(BinOP):
    def getvalue(self):
        return self.left.getvalue() * self.right.getvalue()
