#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cas_str = 'all, delete, delete-orphan'
        cities = relationship('City', backref='state', cascade=cas_str)
    else:
        name = ""
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
            query = storage.all(City).values()
            return [city for city in query if city.state_id == self.id]
