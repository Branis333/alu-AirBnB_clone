#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
import io
import os
import sys
# Get the absolute path to the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path to the root directory of the project
root_dir = os.path.dirname(current_dir)

# Add the root directory to the system path
sys.path.append(root_dir)

# Now you can import console.py
try:
    from console import HBNBCommand
except ModuleNotFoundError as e:
    print(f"Error: {e}")
    print(f"Current directory: {current_dir}")
    print(f"Root directory: {root_dir}")
    print(f"sys.path: {sys.path}")

class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand class"""

    def setUp(self):
        """Set up a common patcher """
        # Patch the models module's dict_classes and storage
        self.dict_classes_patcher = patch('models.storage.all')
        self.storage_patcher = patch('sys.stdout', new_callable=io.StringIO)

        # Start the patches
        self.mock_dict_classes = self.dict_classes_patcher.start()
        self.mock_stdout = self.storage_patcher.start()

        # Create an instance of the HBNBCommand for testing
        self.console = HBNBCommand()

    def tearDown(self):
        """Stop the patches"""
        self.dict_classes_patcher.stop()
        self.storage_patcher.stop()

    def test_do_quit(self):
        """Test the do_quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_do_EOF(self):
        """Test the do_EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test the emptyline method"""
        self.assertFalse(self.console.onecmd(""))

    # Add other test methods...

if __name__ == '__main__':
    unittest.main()
