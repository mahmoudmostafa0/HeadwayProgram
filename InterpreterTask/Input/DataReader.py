from abc import ABC, abstractmethod


class DataReader(ABC):
    def __init__(self):
        self.__currentindex = -1
        self.__totalrows = -1

    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def is_data_finished(self):
        pass
