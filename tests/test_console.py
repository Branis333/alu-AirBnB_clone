#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
import io
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand class"""

    def setUp(self):
        """Set up a common patcher """
        # Patch the models module's dict_classes and storage
        self.dict_classes_patcher = patch('models.dict_classes', {
            'BaseModel': MagicMock(),
            'User': MagicMock(),
            # Add other classes as needed
        })
        self.storage_patcher = patch('models.storage', MagicMock())

        # Start the patches
        self.mock_dict_classes = self.dict_classes_patcher.start()
        self.mock_storage = self.storage_patcher.start()

        # Create an instance of the HBNBCommand for testing
        self.console = HBNBCommand()

    def tearDown(self):
        """Stop the patches"""
        self.dict_classes_patcher.stop()
        self.storage_patcher.stop()

    def test_do_quit(self):
        """Test the do_quit command"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.assertTrue(self.console.onecmd("quit"))

    def test_do_EOF(self):
        """Test the do_EOF command"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test the emptyline method"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.assertFalse(self.console.onecmd(""))

    def test_do_create_missing_class_name(self):
        """Test do_create with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("create")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_create_invalid_class_name(self):
        """Test do_create with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_create_valid_class_name(self):
        """Test do_create with valid class name"""
        mock_instance = MagicMock()
        mock_instance.save = MagicMock()
        mock_instance.id = "1234"
        self.mock_dict_classes['BaseModel'].return_value = mock_instance
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("create BaseModel")
            self.assertEqual(fake_output.getvalue().strip(), "1234")
            mock_instance.save.assert_called_once()

    def test_do_show_missing_class_name(self):
        """Test do_show with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("show")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_show_invalid_class_name(self):
        """Test do_show with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("show InvalidClass")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_show_missing_instance_id(self):
        """Test do_show with missing instance id"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("show BaseModel")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_show_no_instance_found(self):
        """Test do_show with no instance found"""
        self.mock_storage.all.return_value = {}
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("show BaseModel 1234")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_show_instance_found(self):
        """Test do_show with instance found"""
        mock_instance = MagicMock()
        self.mock_storage.all.return_value = {"BaseModel.1234": mock_instance}
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("show BaseModel 1234")
            self.assertIn(str(mock_instance), fake_output.getvalue().strip())

    def test_do_destroy_missing_class_name(self):
        """Test do_destroy with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("destroy")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_destroy_invalid_class_name(self):
        """Test do_destroy with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("destroy InvalidClass")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_destroy_missing_instance_id(self):
        """Test do_destroy with missing instance id"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_destroy_no_instance_found(self):
        """Test do_destroy with no instance found"""
        self.mock_storage.all.return_value = {}
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("destroy BaseModel 1234")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_destroy_instance_found(self):
        """Test do_destroy with instance found"""
        mock_instance = MagicMock()
        self.mock_storage.all.return_value = {"BaseModel.1234": mock_instance}
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("destroy BaseModel 1234")
            self.assertNotIn("BaseModel.1234", self.mock_storage.all())
            self.mock_storage.save.assert_called_once()

    def test_do_all_no_class_name(self):
        """Test do_all with no class name"""
        self.mock_storage.all.return_value = {"BaseModel.1234": MagicMock()}
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("all")
            self.assertIn(str(self.mock_storage.all()["BaseModel.1234"]),
            fake_output.getvalue().strip())

    def test_do_all_invalid_class_name(self):
        """Test do_all with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("all InvalidClass")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_all_valid_class_name(self):
        """Test do_all with valid class name"""
        mock_instance = MagicMock()
        self.mock_storage.all.return_value = {"BaseModel.1234": mock_instance}
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("all BaseModel")
            self.assertIn(str(mock_instance), fake_output.getvalue().strip())

    def test_do_update_missing_class_name(self):
        """Test do_update with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("update")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_update_invalid_class_name(self):
        """Test do_update with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("update InvalidClass")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_update_missing_instance_id(self):
        """Test do_update with missing instance id"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("update BaseModel")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_update_missing_attribute_name(self):
        """Test do_update with missing attribute name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.console.onecmd("update BaseModel 1234")
            self.assertEqual(fake_output.getvalue().strip(),)

    def test_do_update_missing_value(self):
        """Test do_update with missing value"""
        with patch('sys.stdout', new=io.String)