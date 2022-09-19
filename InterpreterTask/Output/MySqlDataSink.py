from Message import Message
from Output.DataSink import DataSink
import mysql.connector


class MySqlDataSink(DataSink):

    def __init__(self, host: str, user: str, password: str, database: str):
        self.__conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.__cursor = self.__conn.cursor()
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()

    def add_new_entry(self, msg: Message):
        query = "INSERT INTO data (asset_id,attribute_id,timestamp,value) VALUES (%(asset_id)s, %(attribute_id)s, " \
                "%(timestamp)s, %(value)s); "
        self.__cursor.execute(query, msg.__dict__)
        self.__conn.commit()
        pass

    def update_entry(self):
        pass

    def close(self):
        self.__conn.close()
