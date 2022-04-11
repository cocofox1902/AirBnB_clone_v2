#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == 'db':
        name = Column(String(60), nullable=False)
        __tablename__ = "cities"
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ instantiates a new state """
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def cities(self):
            """ returns list all cities"""
            list_city = []
            list_cities_complete = models.storage.all(City)
            for city in list_cities_complete.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
