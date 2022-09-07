#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from sqlalchemy import create_engine
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """"""
    classes = {"City": City, "State": State, "User": User, "Place": Place,
                "Review": Review, "Amenity": Amenity}
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB,
                                              pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        newdict = {}
        for clase in self.classes:
            if cls is None or cls is self.classes[clase] or cls is clase:
                obj = self.__session.query(self.classes[clase]).all()
                for instance in obj:
                    key = instance.__class__.__name__ + '.' + instance.id
                    newdict[key] = instance
        return newdict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
