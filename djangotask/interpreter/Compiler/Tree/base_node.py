from abc import ABC, abstractmethod


class AST(ABC):
    """
       Base class for abstract syntax trees
    """
    @abstractmethod
    def getvalue(self):
        """
               Get the value of the tree/node
        """
        pass
