#!/usr/bin/python3
"""a unittest for the base class
"""
import sys
import unittest
import inspect
import pycodestyle
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """a class for testing methods used in basemodel
    """

    @classmethod
    def setUpClass(cls):
        """ setting up a test environment for the doc tests
        """
        cls.setup = inspect.getmembers(BaseModel, predicate=inspect.ismethod)

    def test_pep8_base(self):
        """to test if file: base_model.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """ to test if file: test_base_model.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models'
                                        '/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """to test if documentation for module is present
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """to test if documentation for class is present
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstring(self):
        """to test if documentation for function is present
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def clear(self):
        """removes the json file"""
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """test the instance of a class"""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_args(self):
        """test the number of arguments passed in"""
        arg = [i for i in range(20)]
        T = BaseModel(*arg)

    def test_to_dict(self):
        """test the keys in the dictionary"""
        b = BaseModel()
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
        b = BaseModel()
        b.name = "bill"
        b.my_number = 788
        z = b.to_dict()
        x = BaseModel(**z).to_dict()
        self.assertDictEqual(z, x)
