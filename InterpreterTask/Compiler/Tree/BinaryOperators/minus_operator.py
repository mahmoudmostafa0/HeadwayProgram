from Compiler.Tree.BinaryOperators.binary_operator import BinOP


class MinusOP(BinOP):
    """
    class for the minus operator
    """
    def getvalue(self):
        """
        subtract two operators and return the value
        Returns:
        subtraction of two values
        """
        return self.left.getvalue() - self.right.getvalue()
