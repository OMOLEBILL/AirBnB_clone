#!/usr/bin/python3
"""a unittest for the base class
"""

import unittest
import inspect
import pycodestyle
from models.state import State
from models.engine.file_storage import FileStorage
import os


class TestState(unittest.TestCase):
    """a class for testing methods used state
    """

    @classmethod
    def setUpClass(cls):
        """ setting up a test environment for the doc tests
        """
        cls.setup = inspect.getmembers(State, predicate=inspect.ismethod)

    def test_pep8_base(self):
        """to test if file: state.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """ to test if file: test_state.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models'
                                        '/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """to test if documentation for module is present
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstring(self):
        """to test if documentation for class is present
        """
        self.assertTrue(len(State.__doc__) >= 1)

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
        b = State()
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), State))

    def test_args(self):
        """test the number of arguments passed in"""
        self.clear()
        arg = [i for i in range(20)]
        T = State(*arg)

    def test_to_dict(self):
        """test the keys in the dictionary"""
        b = State()
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
        b = State()
        b.name = "bill"
        b.my_number = 788
        z = b.to_dict()
        x = State(**z).to_dict()
        self.assertDictEqual(z, x)

    def test_no_args(self):
        """test basemodel with no args"""
        self.clear()
        with self.assertRaises(TypeError) as error:
            State.__init__()
        err = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), err)

    def test_save(self):
        """test wether the json file is created"""
        self.clear()
        my_model = State()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

    def test_save_more_args(self):
        """ tests method save with more than one arg"""
        self.clear()
        with self.assertRaises(TypeError) as error:
            State.save(self, 777)
        err = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), err)


if __name__ == "__main__":
    unittest.main()
