#!/usr/bin/python3
"""a unittest for the base class
"""

import unittest
import inspect
import pycodestyle
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """a class for testing methods used in basemodel
    """

    @classmethod
    def setUpClass(cls):
        """ setting up a test environment for the doc tests
        """
        cls.setup = inspect.getmembers(FileStorage, predicate=inspect.ismethod)

    def test_pep8_base(self):
        """to test if file: base_model.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """ to test if file: test_base_model.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models'
                                        '/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """to test if documentation for module is present
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_class_docstring(self):
        """to test if documentation for class is present
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

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


if __name__ == "__main__":
    unittest.main()
