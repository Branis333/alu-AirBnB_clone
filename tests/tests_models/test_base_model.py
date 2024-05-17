#!/usr/bin/python3

import unittest
import os
from datetime import datetime
import time
import uuid
import sys
import subprocess

# Add pycodestyle directory to sys.path
pycodestyle_path = os.path.abspath("path_to_pycodestyle")
sys.path.append(pycodestyle_path)

# Add parent directory to sys.path to import BaseModel
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Initialize the base_model attribute
        self.base_model = BaseModel()

        # Assign file paths
        self.file_path_1 = "base_model_1.py"
        self.file_path_2 = "base_model_2.py"
        self.file_path_3 = "base_model_3.py"
        self.file_path_4 = "base_model_4.py"

        # Create base_model_1.py
        with open(self.file_path_1, "w") as f:
            f.write("# This is base_model_1.py\n")
            f.write("print('base_model_1.py created successfully')\n")

        # Create base_model_2.py
        with open(self.file_path_2, "w") as f:
            f.write("# This is base_model_2.py\n")
            f.write("print('base_model_2.py created successfully')\n")

        # Create base_model_3.py
        with open(self.file_path_3, "w") as f:
            f.write("# This is base_model_3.py\n")
            f.write("print('base_model_3.py created successfully')\n")

        # Create base_model_4.py
        with open(self.file_path_4, "w") as f:
            f.write("# This is base_model_4.py\n")
            f.write("print('base_model_4.py created successfully')\n")

    def test_style_guide(self):
        """Test compliance with PEP 8 style guide."""
        result = subprocess.run(['flake8', 'models/base_model.py', 'tests/test_base_model.py'], stdout=subprocess.PIPE)
        self.assertEqual(result.returncode, 0, msg="PEP 8 style violations found.")

    def test_file_exists(self):
        """Test if the files exist."""
        # Check if each file exists
        self.assertTrue(os.path.exists(self.file_path_1))
        self.assertTrue(os.path.exists(self.file_path_2))
        self.assertTrue(os.path.exists(self.file_path_3))
        self.assertTrue(os.path.exists(self.file_path_4))

    def tearDown(self):
        """Clean up after the test."""
        # Remove created files
        for file_path in [self.file_path_1, self.file_path_2, self.file_path_3, self.file_path_4]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_init(self):
        """Test initialization of BaseModel attributes."""
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        expected_str = "[{}] ({}) {}".format(
            self.base_model.__class__.__name__,
            self.base_model.id,
            self.base_model.__dict__
        )
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Test the save method of BaseModel."""
        old_updated_at = self.base_model.updated_at
        time.sleep(1)
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        result_dict = self.base_model.to_dict()
        self.assertIsInstance(result_dict, dict)
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, result_dict)
        self.assertEqual(result_dict['__class__'], self.base_model.__class__.__name__)
        self.assertEqual(result_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(result_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        """Test initialization of BaseModel with keyword arguments."""
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

    def test_documentation(self):
        """Test if BaseModel and its methods have documentation strings."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_style_guide(self):
        """Test compliance with PEP 8 style guide."""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
