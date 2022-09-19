from Compiler.Tree.AST import AST


class Num(AST):
    def getvalue(self):
        return self.value

    def __init__(self, token):
        self.token = token
        self.value = token.value
