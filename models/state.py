#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', backref='state',cascade=True)
    elif os.environ.get("HBNB_TYPE_STORAGE") == 'file':
        @property
        def cities(self):
            """
            getter attribute cities that returns
            the list of City instances with state_id
            equals to the current State.id =>
            It will be the FileStorage relationship between State and City
            """
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values() if city.state_id == self.id]