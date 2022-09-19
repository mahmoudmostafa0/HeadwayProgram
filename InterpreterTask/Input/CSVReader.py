import json

from Input.DataReader import DataReader
from Message import Message


class CSVReader(DataReader):
    def __init__(self, filepath):
        super(CSVReader, self).__init__()
        self.filepath = filepath
        self.__readfile()

    def get_next(self):
        if self.is_data_finished():
            return None
        else:
            line = self.lines[self.__currentindex]
            json_obj = json.loads(line)
            message = Message()
            message.load_from_json(json_obj)
            self.__currentindex = self.__currentindex + 1
            return message

    def is_data_finished(self):
        return self.__currentindex >= self.__totalrows

    def __readfile(self):
        with open(self.filepath, 'r') as f:
            self.lines = f.readlines()
        self.__totalrows = len(self.lines)
        self.__currentindex = 0
