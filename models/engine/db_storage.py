#!/usr/bin/python3
""" Database storage engine module
"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage():
    """ Database engine class for interacting with the msql database"""
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor method to create engine for database storage"""
        # environment variables
        env = getenv('HBNB_ENV')
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        if all(var is not None for var in [user, pwd, host, db]):
            self.__engine = create_engine("{}://{}:{}@{}/{}".format(
                            "mysql+mysqldb", user, pwd, host, db),
                            pool_pre_ping=True)
            if env == 'test':
                # delete all tables
                Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Queries current database session for all objects """
        objs = {}
        class_list = [User, State, City, Place, Amenity, Review]
        if cls is not None:
            # query for all records in particular table
            # Add them to dictionary 'objs'
            for obj in self.__session.query(cls).all():
                key = ".".join([obj.__class__.__name__, obj.id])
                objs.update({key: obj})
        else:
            # query for all objects in all tables
            # Add them to dictionary 'objs'
            for cl in class_list:
                for obj in self.__session.query(cl).all():
                    key = ".".join([obj.__class__.__name__, obj.id])
                    objs.update({key: obj})
        return objs

    def new(self, obj):
        """ Adds item to current database session """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete objects from current database """
        if obj is not None:
            # check if object exists in table before deleting it
            obj_query = self.__session.query(obj.__class__).filter_by(
                    id=obj.id).one_or_none()
            if obj_query is not None:
                self.__session.delete(obj_query)
                self.save()

    def reload(self):
        """ Create all tables in the database """
        # create all tables
        Base.metadata.create_all(self.__engine)

        # create session
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.close()
