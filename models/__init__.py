#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage
depending on the environment variable HBNB_TYPE_STORAGE.
"""
from os import environ


def switch():
    """
    Determines the storage type based on
    the HBNB_TYPE_STORAGE environment variable.

    If HBNB_TYPE_STORAGE is 'db', it imports and initializes DBStorage.
    Otherwise, it imports and initializes FileStorage.

    Returns:
        An instance of either DBStorage or FileStorage.
    """
    storage_mech = environ.get('HBNB_TYPE_STORAGE')

    if storage_mech == 'db':
        from models.engine.db_storage import DBStorage
        storage = DBStorage()

    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
    return storage


storage = switch()
storage.reload()
