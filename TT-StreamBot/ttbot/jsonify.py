#!/usr/bin/python3
import json

class JSONify(object):
    """Base class for save and loading class data using JSON files

    Any attributtes added to a subclass will be included in the JSON file.
    """

    def __init__(self,json_path=None):
        """Init with file path"""

        self._json_path = None

        if json_path is not None:
            self.json_path = json_path
            self.json_read()


    def json_write(self, file_path=None):
        """Write all class attributtes to JSON file"""
        if file_path is None:
            file_path = self.json_path

        with open(file_path, 'w') as f:
            json.dump(vars(self), f, sort_keys=True)


    def json_read(self, file_path=None):
        """Read data from JSON file and add it as attributtes to self"""
        if file_path is None:
            file_path = self.json_path

        with open(file_path, 'r') as f:
            data = json.load(f)
            for attr, value in data.items():
                setattr(self,attr, value)


    @property
    def json_path(self):
        return self._json_path

    @json_path.setter
    def json_path(self, value):
        self._json_path = value

