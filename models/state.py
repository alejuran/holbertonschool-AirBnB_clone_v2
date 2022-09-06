#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
class State(BaseModel, Base):
    """ State class """
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    def init(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
    
    if HBNB_TYPE_STORAGE != 'db':
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            cities = storage.all(City)
            return [city for city in cities.values() if city.state_id == self.id]
