from Compiler.Tables.Functions import Functions
from Compiler.Tree.AST import AST


class FuncCallNode(AST):
    def __init__(self, funcname, params: []):
        self.funcname = funcname
        self.params = params

    def getvalue(self):
        if not Functions.isfunction(self.funcname):
            raise Exception('Cannot find function. Note that the functions are case sensetive')
        return Functions.callfunction(self.funcname, [par.getvalue() for par in self.params])
