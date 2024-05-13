#!/usr/bin/python3
import unittest
import datetime
import uuid

import sys
sys.path.append(models/base_model.py)
import base_model

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str(self):
        expected_str = "[{}] ({}) {}".format(
        self.base_model.__class__.__name__,
        self.base_model.id,
        self.base_model.__dict__
)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)

    def test_to_dict(self):
        result_dict = self.base_model.to_dict()
        self.assertIsInstance(result_dict, dict)
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, result_dict)
        self.assertEqual(result_dict['__class__'], self.base_model.__class__.__name__)
        self.assertEqual(result_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(result_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        new_id = str(uuid.uuid4())
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        kwargs = {
            'id': new_id,
            'created_at': created_at.isoformat(),
            'updated_at': updated_at.isoformat()
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, new_id)
        self.assertEqual(base_model.created_at, created_at)
        self.assertEqual(base_model.updated_at, updated_at)

if __name__ == '__main__':
    unittest.main()

