from Compiler.Tree.BinaryOperators.binary_operator import BinOP


class PlusOP(BinOP):
    """
    class that is used to create plus operator
    """
    def getvalue(self):
        """
        add two operators and return the value
        Returns:
        addition of two values
        """
        return self.left.getvalue() + self.right.getvalue()
