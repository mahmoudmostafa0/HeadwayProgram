from interpreter.Compiler.Tree.base_node import AST
from interpreter.Compiler.Tables.variables import Variables


class Var(AST):
    """The Var node is constructed out of ID token."""

    def __init__(self, token):
        self.token = token
        self.value = token.value

    def getvalue(self):  # search for the variable in the stored variables
        variable_value = Variables.get_value(self.value)
        if variable_value is None:
            raise Exception('Undefined Variable')
        return variable_value
