#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models


if models.storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class City(BaseModel):
    """ The city class, contains state ID and name """
    if models.storage_t == 'db':
        state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
        name = Column(String(60), nullable=False)
        __tablename__ = "cities"
    else:
        state_id = ""
        name = ""
