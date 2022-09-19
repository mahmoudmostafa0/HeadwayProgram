

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def reset(self):
        self.parser.reset()

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        return tree.getvalue()
