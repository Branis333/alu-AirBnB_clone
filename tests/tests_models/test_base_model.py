#!/usr/bin/python3

import unittest
from datetime import datetime
import time
import uuid
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()
        self.file_path = "base_model_1.py"
        self.file_path = "base_model_2.py"
        self.file_path = "base_model_3.py"
        self.file_path = "base_model_4.py"

        # Create base_model_2.py
        with open(self.file_path, "w") as f:
            # Write some content to the file
            f.write("# This is base_model_2.py\n")
            f.write("print('base_model_2.py created successfully')\n")

        # Create base_model_3.py
        with open(self.file_path, "w") as f:
            # Write some content to the file
            f.write("# This is base_model_3.py\n")
            f.write("print('base_model_3.py created successfully')\n")

        # Create base_model_4.py
        with open(self.file_path, "w") as f:
            # Write some content to the file
            f.write("# This is base_model_4.py\n")
            f.write("print('base_model_4.py created successfully')\n")

    def test_file_exists(self):
        """Test if the file exists."""
        file_exists = os.path.exists(self.file_path)
        try:
            print("Attempting to perform some operation...")
        except Exception as e:
                              print("An error occurred:", e)
        if file_exists:
            self.assertEqual(2, len(open(self.file_path).readlines()))
        else:
             print("File {} does not exist.".format(self.file_path))
        with open(self.file_path, "r") as f:
            lines = f.readlines()
            self.assertEqual(2, len(lines))
        pass

    def tearDown(self):
        """Clean up after the test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_init(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        expected_str = "[{}] ({}) {}".format(
         self.base_model.__class__.__name__,
         self.base_model.id,
         self.base_model.__dict__
         )
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        time.sleep(1)
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict(self):
        result_dict = self.base_model.to_dict()
        self.assertIsInstance(result_dict, dict)
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, result_dict)
        self.assertEqual(result_dict['__class__'],
                         self.base_model.__class__.__name__)
        self.assertEqual(result_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(result_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        new_id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        kwargs = {
            'id': new_id,
            'created_at': created_at.isoformat(),
            'updated_at': updated_at.isoformat()
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, new_id)
        self.assertEqual(base_model.created_at, created_at)
        self.assertEqual(base_model.updated_at, updated_at)
        pass
if __name__ == '__main__':
    unittest.main()
