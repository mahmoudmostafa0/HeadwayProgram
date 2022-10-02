from interpreter.Compiler.Tree.BinaryOperators.binary_operator import BinOP


class DivOP(BinOP):
    """
    class that is used for the divide node
    """
    def getvalue(self) -> float:
        """
        divide two operators and return the value
        Returns:
        division of two values
        """
        return self.left.getvalue() / self.right.getvalue()
