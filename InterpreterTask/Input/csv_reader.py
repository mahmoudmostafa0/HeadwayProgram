import json
from Input.data_reader import DataReader
from Message import Message


class CSVReader(DataReader):
    """
               class that is used to read txt file
    """
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.__readfile()

    def get_next(self):
        if self.is_data_finished():
            return None

        line = self.lines[self.__currentindex]
        json_obj = json.loads(line)
        message = Message()
        message.load_from_json(json_obj)
        self.__currentindex = self.__currentindex + 1
        return message

    def is_data_finished(self):
        return self.__currentindex >= self.__totalrows

    def __readfile(self):
        with open(self.filepath, 'r') as file:
            self.lines = file.readlines()
        self.__totalrows = len(self.lines)
        self.__currentindex = 0
