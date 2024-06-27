#!/usr/bin/python3
"""this module hava a class that handle the Database"""
from os import environ
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base


class DBStorage:
    """
    A class that acts as a handler for the database server.
    Attributes:
        __engine (sqlalchemy.Engine): The SQLAlchemy engine instance.
        __session (sqlalchemy.orm.scoping.scoped_session):
                    The SQLAlchemy session instance.
        objects (list): List of class names to handle in the database.
    """
    __engine = None
    __session = None
    objects = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self) -> None:
        """
        Initializes the DBStorage instance.
        Sets up the database engine and session.
        Drops all tables if the environment
        variable HBNB_ENV is set to 'test'.
        """
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        database = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}:3306/{database}',
            pool_pre_ping=True
            )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        self.reload()

    def all(self, cls=None):
        """
        Queries the current database session
        for all objects of a given class.
        Args:
            cls (type, optional): The class type to query for.
            If None, queries all types.
        Returns:
            dict: A dictionary of queried objects
            with keys in the format <class-name>.<object-id>.
        """
        results = []
        dictionary = {}

        if cls:
            results = self.__session.query(cls).all()
        else:
            for obj_name in DBStorage.objects:
                cls = globals().get(obj_name)
                if cls:
                    results = self.__session.query(cls).all()
        for obj in results:
            key = f'{obj.__class__.__name__}.{obj.id}'
            dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """
        Adds a new object to the current database session.

        Args:
            obj (BaseModel): The object to add to the session.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
            DBStorage.save()

    def reload(self):
        """
        Creates all tables in the database and initializes the session.
        Ensures that all models are correctly imported.
        """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
