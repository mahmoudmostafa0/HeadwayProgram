from abc import ABC, abstractmethod


class DataSink(ABC):

    @abstractmethod
    def add_new_entry(self):
        pass

    @abstractmethod
    def update_entry(self):
        pass

    @abstractmethod
    def close(self):
        pass