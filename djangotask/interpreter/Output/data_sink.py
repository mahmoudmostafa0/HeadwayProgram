from abc import ABC, abstractmethod


class DataSink(ABC):
    """
    data sink class that is used for the output of the data
    """
    @abstractmethod
    def add_new_entry(self, entry):
        """
        add new entry to the data
        Args:
            entry:the entry to be added to the data
        """
        pass

    @abstractmethod
    def update_entry(self, entry):
        """
        update an entry that already exists in the data
        Args:
            entry:the entry to be updated

        """
        pass

    @abstractmethod
    def close(self):
        """
        close the current opened file/connection

        """
        pass
