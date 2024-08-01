#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        name = Column(
            String(128), nullable=False
        )
        state_id = Column(
            String(60), ForeignKey('states.id'), nullable=False
        )
        places = relationship(
            'Place',
            cascade='all, delete, delete-orphan',
            backref='cities'
        )
else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        name = ""
        state_id = ""
        places = None
