#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        name = mapped_column(
            String(128), nullable=False, sort_order=3
        )
        state_id = mapped_column(
            String(60), ForeignKey('states.id'), nullable=False, sort_order=4
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
