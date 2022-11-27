#!/usr/bin/python3
"""a unittest for the base class
"""

import unittest
import inspect
import pycodestyle
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    """a class for testing methods used in basemodel
    """

    @classmethod
    def setUpClass(cls):
        """ setting up a test environment for the doc tests
        """
        cls.setup = inspect.getmembers(User, predicate=inspect.ismethod)

    def test_pep8_base(self):
        """to test if file: user_model.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """ to test if file: user_model.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models'
                                        '/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """to test if documentation for module is present
        """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_docstring(self):
        """to test if documentation for class is present
        """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_func_docstring(self):
        """to test if documentation for function is present
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def clear(self):
        """removes the json file"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """test the instance of a class"""
        b = User()
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), User))

    def test_args(self):
        """test the number of arguments passed in"""
        self.clear()
        arg = [i for i in range(20)]
        T = User(*arg)

    def test_to_dict(self):
        """test the keys in the dictionary"""
        b = User()
        b.name = "bill"
        b.my_number = 788
        z = b.to_dict()
        self.assertEqual(z["id"], b.id)
        self.assertEqual(z["__class__"], type(b).__name__)
        self.assertEqual(z["created_at"], b.created_at.isoformat())
        self.assertEqual(z["updated_at"], b.updated_at.isoformat())
        self.assertEqual(z["name"], b.name)
        self.assertEqual(z["my_number"], b.my_number)

    def test_dict(self):
        """test the whole dict"""
        b = User()
        b.name = "bill"
        b.my_number = 788
        z = b.to_dict()
        x = User(**z).to_dict()
        self.assertDictEqual(z, x)

    def test_save(self):
        """test wether the json file is created"""
        self.clear()
        my_model = User()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
