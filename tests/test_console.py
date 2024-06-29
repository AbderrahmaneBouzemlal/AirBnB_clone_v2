#!/usr/bin/python3
"""
Tests the Console module
"""
from console import HBNBCommand
import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
import json


class TestHBNBCommand(unittest.TestCase):
    """
    In this class we are going to test the HBNBCommand
    """
    def setUp(self):
        """Setup test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after each test"""
        storage._FileStorage__objects = {}

    def test_create(self):
        """Test the create method"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create User email='test@example.com' password='password'")
            user_id = fake_out.getvalue().strip()
            self.assertTrue(user_id in storage._FileStorage__objects)

    def test_show(slef):
    	"""Test the show method"""
    	with patch('sys.stdout', new=StringIO()) as fake_out:
            user = User(email='test@example.com', password='password')
            user.save()
            self.console.onecmd(f"show User {user.id}")
            output = fake_out.getvalue().strip()
            self.asserIn(user.id, output)

    def test_destroy(self):
        """Test the destroy method"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            user = User(email='Abderrahmane@Bouzemlal.com', password='password')
            user.save()
            self.console.onecmd(f"destroy User {user.id}")
            slef.assertNotIn(f"User.{user_id}", _FileStorage__objects)

    def test_all(self):
        """Test the all method"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all User")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "[]")

            user = User(email='test@example.com', password='password')
            user.save()
            self.console.onecmd("all User")
            output = fake_out.getvalue().strip()
            self.assertIn(user.id, output)

    def test_count(self):
        """Test the count method"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("count User")
            self.assertEqual(fake_out.getvalue().strip(), "0")

            user = User(email='test@example.com', password='password')
            user.save()
            self.console.onecmd("count User")
            self.assertEqual(fake_out.getvalue().strip(), "1")

    def test_update(self):
        """Test the update command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            user = User(email='test@example.com', password='password')
            user.save()
            self.console.onecmd(f"update User {user.id} email 'new@example.com'")
            self.assertEqual(storage._FileStorage__objects[f"User.{user.id}"].email, 'new@example.com')

    def test_create_invalid_class(self):
        """The test of create an invalid class"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(fake_out.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Testing if the show command line is working properly"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show User")
            self.assertEqual(fake_out.getvalue().strip(), "** instance id missing **")

    def test_destroy_missing_id(self):
        """destroying a missing id"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy User")
            self.assertEqual(fake_out.getvalue().strip(), "** instance id missing **")

    def test_update_missing_id(self):
        """update an none existing object"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update User")
            self.assertEqual(fake_out.getvalue().strip(), "** instance id missing **")


if __name__ == '__main__':
    unittest.main()

