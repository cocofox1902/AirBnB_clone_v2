#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
            email = Column(String(128), nullable=False)
            password = Column(String(128), nullable=False)
            first_name = Column(String(128), nullable=False)
            last_name =  Column(String(128), nullable=False)
            __tablename__ = 'users'
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """ instantiates a new state """
        super().__init__(*args, **kwargs)
