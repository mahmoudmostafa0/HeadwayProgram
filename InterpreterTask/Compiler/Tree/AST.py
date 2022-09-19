from abc import ABC, abstractmethod


class AST(ABC):
    pass

    @abstractmethod
    def getvalue(self):
        pass
