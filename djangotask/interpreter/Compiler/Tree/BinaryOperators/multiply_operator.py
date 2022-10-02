from interpreter.Compiler.Tree.BinaryOperators.binary_operator import BinOP


class MulOP(BinOP):
    """
    class for the multiply operator
    """
    def getvalue(self):
        """
        multiply two operators and return the value
        Returns:
        multiplication of two values
        """
        return self.left.getvalue() * self.right.getvalue()
