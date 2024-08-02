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
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1'
        }
        email = mapped_column(
            String(128), nullable=False
        )
        password = mapped_column(
            String(128), nullable=False
        )
        first_name = mapped_column(
            String(128), nullable=True
        )
        last_name = mapped_column(
            String(128), nullable=True
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
        email=""
        password=""
        first_name=""
        last_name=""
        places=None
        reviews=None
