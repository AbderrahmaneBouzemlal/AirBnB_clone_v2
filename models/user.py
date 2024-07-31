#!/usr/bin/python3
"""This module defines a class User"""
import os
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column
from models.base_model import BaseModel, Base

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'
        email = mapped_column(
            String(128), nullable=False, sort_order=3
        )
        password = mapped_column(
            String(128), nullable=False, sort_order=4
        )
        first_name = mapped_column(
            String(128), nullable=True, sort_order=5
        )
        last_name = mapped_column(
            String(128), nullable=True, sort_order=6
        )
        places = relationship(
            'Place',
            cascade="all, delete, delete-orphan",
            backref='user'
        )
        reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan",
            backref='user'
        )
else:
    class User(BaseModel):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        places = None
        reviews = None
