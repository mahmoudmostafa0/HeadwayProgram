from Compiler.Tables.Functions import Functions
from Compiler.Tree.base_node import AST


class FuncCallNode(AST):
    """
    class for the node to call a new function
    """
    def __init__(self, funcname, params: []):
        self.funcname = funcname
        self.params = params

    def getvalue(self):
        """
        calls a function
        Returns:
            the value returned from the called function
        """
        if not Functions.isfunction(self.funcname):
            raise Exception('Cannot find function. Note that the functions are case sensetive')
        return Functions.callfunction(self.funcname, [par.getvalue() for par in self.params])
