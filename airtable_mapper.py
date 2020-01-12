from airtable import Airtable
from collections import UserDict, _VT


class MappedRecord(UserDict):
    map: dict

    def __init__(self,  map_=None, **kwargs: _VT):
        super().__init__(**kwargs)
        self.map = map_


class MappedAirtable(Airtable):
    map: dict

    def __init__(self, base_key, table_name, map_: dict = None):
        super().__init__(base_key, table_name)
        self.map = map_ or {}

    def mget(self):
        pass
