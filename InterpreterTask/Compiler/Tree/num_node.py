from Compiler.Tree.base_node import AST


class Num(AST):
    """
    class that is used to create a number node
    """
    def getvalue(self):
        return self.value

    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __eq__(self, other):
        """
        when using == operator with token
        """
        if type(self) == type(other):
            return self.value == other.value and self.token == other.token
        else:
            raise TypeError