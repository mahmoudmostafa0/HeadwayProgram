class Message:
    """
    message class
    """
    def __init__(self, asset_id=None, attribute_id=None, timestamp=None, value=None):
        self.asset_id = asset_id
        self.attribute_id = attribute_id
        self.timestamp = timestamp
        self.value = value

    def load_from_json(self, json_object):
        """
        load message from json file
        Args:
            json_object: json object to load the class from

        """
        self.__dict__ = json_object
