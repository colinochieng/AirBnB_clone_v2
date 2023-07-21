#!/usr/bin/python3
"""
File for DBStorage
Mages database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {'User': User, 'Place': Place, 'State': State,
           'City': City, 'Amenity': Amenity, 'Review': Review}

class DBStorage:
    """
    Database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        '''
        declares basic requirements
        '''
        url = 'mysql+mysqldb://{}:{}@{}/{}'\
            .format(getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(url, pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """
        query on the current database session
        all objects depending of the class name (argument cls)
        """
        archive = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = obj.id
                archive.update({key: obj})
        else:
            for value in classes.values():
                for obj in self.__session.query(value).all():
                    key = obj.id
                    archive.update({key: obj})
        return archive
    
    def reload(self):
        """
        create all tables in the database
        creates a threaded session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scoped = scoped_session(Session)
        self.__session = Scoped()
    
    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)
    
    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)
