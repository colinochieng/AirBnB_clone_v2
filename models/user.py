#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        cas_str = 'all, delete, delete-orphan'
        places = relationship('Place', backref='user', cascade=cas_str)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
