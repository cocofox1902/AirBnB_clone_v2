#!/usr/bin/python3
"""
    comment
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ as env
from os import getenv


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
    'City': City, 'Amenity': Amenity, 'Review': Review
    }


class DBStorage:
    """
        comment
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            comment
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """
            comment
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

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
        else:
            self.__session.query(Base).delete()
        self.save()

    def reload(self):
        """
            comment
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker
                                        (bind=self.__engine,
                                         expire_on_commit=False))

    def close(self):
        """
            comment
        """
        self.__session.remove()
