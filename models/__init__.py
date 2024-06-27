#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
and the DBStorage depending on an environement variable"""
from os import environ


def switch():
    storage_mech = environ.get('HBNB_TYPE_STORAGE')

    if storage_mech == 'db':
        from models.engine.db_storage import DBStorage
        storage = DBStorage()

    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
    return storage


storage = switch()
