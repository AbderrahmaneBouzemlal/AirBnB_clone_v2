#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column

from models.base_model import BaseModel, Base

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """Represents an amenity data set."""
        __tablename__ = 'amenities'
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1'
        }
        name = mapped_column(
            String(128), nullable=False, sort_order=3
        )
else:
    class Amenity(BaseModel):
        """Represents an amenity data set."""
        name = ''
