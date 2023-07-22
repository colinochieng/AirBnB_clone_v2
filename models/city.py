#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        cas_str = 'all, delete, delete-orphan'
        places = relationship('Place', backref='cities', cascade=cas_str)
    else:
        state_id = ""
        name = ""
