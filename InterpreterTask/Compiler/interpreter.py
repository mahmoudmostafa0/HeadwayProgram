

class Interpreter:
    """
    Interpreter class to calculate the KPI expression
    """
    def __init__(self, parser):
        self.parser = parser

    def reset(self):
        """
        reset the interpreter
        """
        self.parser.reset()

    def interpret(self):
        """
        Calculate the value of parsed abstract syntax tree
        """
        tree = self.parser.parse()
        if tree is None:
            return ''
        return tree.getvalue()
