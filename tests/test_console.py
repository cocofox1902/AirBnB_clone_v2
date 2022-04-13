#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import pep8

class TestConsole(unittest.TestCase):
    """Test for console"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['file1.py', 'file2.py'])


    def setUp(self):
        """Set up for test"""
        self.stdout = StringIO()
        self.stderr = StringIO()
        self.stdin = StringIO()
        self.stdin.write('quit')
        self.stdin.seek(0)
        self.stdout.seek(0)
        self.stderr.seek(0)
        self.hbnb = HBNBCommand()
        self.hbnb.stdout = self.stdout
        self.hbnb.stderr = self.stderr
        self.hbnb.stdin = self.stdin
        



    def test_create(self):
        """Test create"""
        self.hbnb.do_create("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_show(self):
        """Test show"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_show("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_destroy(self):
        """Test destroy"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_destroy("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_all(self):
        """Test all"""
        self.hbnb.do_create("BaseModel")
        self.assertEqual(self.stderr.getvalue(), "")
    
    def test_update(self):
        """Test update"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")


    def test_show_id(self):
        """Test show_id"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_show("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_destroy_id(self):
        """Test destroy_id"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_destroy("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id(self):
        """Test update_id"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")
    
    def test_update_id_no_id(self):
        """Test update_id_no_id"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_attr(self):
        """Test update_id_no_attr"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_value(self):
        """Test update_id_no_value"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_attr_value(self):
        """Test update_id_no_attr_value"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_attr_value_2(self):
        """Test update_id_no_attr_value_2"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")
    
    def test_update_id_no_attr_value_3(self):
        """Test update_id_no_attr_value_3"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")
    
    def test_update_id_no_attr_value_4(self):
        """Test update_id_no_attr_value_4"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_attr_value_5(self):
        """Test update_id_no_attr_value_5"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_attr_value_6(self):
        """Test update_id_no_attr_value_6"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_attr_value_7(self):
        """Test update_id_no_attr_value_7"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stdout.getvalue(), "")
        self.assertEqual(self.stderr.getvalue(), "")

    def test_update_id_no_attr_value_8(self):
        """Test update_id_no_attr_value_8"""
        self.hbnb.do_create("BaseModel")
        self.hbnb.do_update("BaseModel")
        self.assertEqual(self.stderr.getvalue(), "")
