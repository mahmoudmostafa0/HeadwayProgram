from abc import ABC, abstractmethod


class DataReader(ABC):
    """
               data reader base class that is used to read data
    """

    def __init__(self):
        self.__currentindex = -1
        self.__totalrows = -1

    @abstractmethod
    def get_next(self):
        """
                   Get the value of the next message from the data reader
                   Returns:
                       returns the next message of the class
        """
        pass

    @abstractmethod
    def is_data_finished(self) -> bool:
        """
                          checks if the data is finished
                          Returns:
                              returns bool which indicates the status of the data
                   """
        pass
