#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'latin1'
    }
    name = mapped_column(
        String(128), nullable=False, sort_order=3
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = mapped_column(
        String(60), ForeignKey('states.id'), nullable=False, sort_order=4
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='cities'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
