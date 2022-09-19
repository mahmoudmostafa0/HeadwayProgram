class Message:
    def __init__(self, asset_id=None, attribute_id=None, timestamp=None, value=None):
        self.asset_id = asset_id
        self.attribute_id = attribute_id
        self.timestamp = timestamp
        self.value = value

    def load_from_json(self, json_object):
        self.__dict__ = json_object
