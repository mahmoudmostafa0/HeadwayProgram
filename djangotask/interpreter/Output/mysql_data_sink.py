import mysql.connector
from message import Message
from Output.data_sink import DataSink


class MySqlDataSink(DataSink):
    """
    data sink that is used to save the data into mysql database
    """
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

    def add_new_entry(self, entry: Message):
        query = "INSERT INTO data (asset_id,attribute_id,timestamp,value) VALUES (%(asset_id)s, %(attribute_id)s, " \
                "%(timestamp)s, %(value)s); "
        self.__cursor.execute(query, entry.__dict__)
        self.__conn.commit()

    def update_entry(self, entry):
        pass

    def close(self):
        self.__conn.close()
