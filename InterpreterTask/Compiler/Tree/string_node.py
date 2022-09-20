from Compiler.Tree.base_node import AST


class String(AST):
    """
    class that is used to create a node for string
    """
    def getvalue(self):
        return self.value

    def __init__(self, token):
        self.token = token
        self.value = token.value
