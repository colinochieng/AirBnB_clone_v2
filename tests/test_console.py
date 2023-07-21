#!/usr/bin/python3
"""
modeule that tests validity of methods in HBNBCommand
"""
from console import HBNBCommand
import unittest
from models.engine.file_storage import FileStorage
import os


class TestHBNBCommand(unittest.TestCase):
    """
    class for testing functionality of console
    """
    def setUp(self):
        """creates an Instance of HBNBCommand"""
        self.console = HBNBCommand()
        self.storage = FileStorage()

    def tearDown(self):
        """deletes and Instance of HBNBCommand class"""
        del self.console
        del self.storage

    # @unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] == 'db')
    # def test_do_all(self):
    #     """Test the do all function"""
    #     self.console.onecmd('')

    @unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] == 'db', "For Json file")
    def test_create(self):
        """Test create from console"""
        length = len(self.storage.all())
        self.console.onecmd('create State name="California"')
        self.assertGreater(len(self.storage.all()), length)
        


if __name__ == "__main__":
    unittest.main()