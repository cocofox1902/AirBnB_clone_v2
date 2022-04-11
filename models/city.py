#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        __tablename__ = 'cities'
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ instantiates a new state """
        super().__init__(*args, **kwargs)
