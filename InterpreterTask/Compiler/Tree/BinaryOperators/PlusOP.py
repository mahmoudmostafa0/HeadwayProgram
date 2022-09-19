from Compiler.Tree.BinaryOperators.BinOP import BinOP


class PlusOP(BinOP):
    def getvalue(self):
        return self.left.getvalue() + self.right.getvalue()
