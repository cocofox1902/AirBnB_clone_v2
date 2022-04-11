#!/usr/bin/python3
"""
    comment
"""
import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from models.base_model import BaseModel
from sqlalchemy.orm import sessionmaker
import MySQLdb
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage():
    """
        comment
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            comment
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                argv[1], argv[2], 'localhost', 'hbnb_dev'), pool_pre_ping=True)

        
    def all(self, cls=None):
        """
            comment
        """
        if cls:
            result = self.__session.query(cls).all()
            new_dict = {}
            for obj in result:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
            return new_dict
        else:
            result = self.__session.query(BaseModel).all()
            new_dict = {}
            for obj in result:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
            return new_dict

    def new(self, obj):
        """
            comment
        """
        self.__session.add(obj)

    def save(self):
        """
            comment
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            comment
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
            comment
        """
        BaseModel.__table__.drop(self.__engine)
        BaseModel.__table__.create(self.__engine)

    def close(self):
        """
            comment
        """
        self.__session.close()