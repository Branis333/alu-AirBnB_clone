#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        # Test if all returns the dictionary __objects
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        # Test if new sets the object correctly in __objects
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save_reload(self):
        # Test if save and reload serialize and deserialize correctly
        obj = BaseModel()
        obj.save()
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

if __name__ == '__main__':
    unittest.main()
