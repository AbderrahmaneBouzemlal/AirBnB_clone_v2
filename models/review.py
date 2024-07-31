#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, mapped_column

from models.base_model import BaseModel, Base

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = 'reviews'
        place_id = mapped_column(
            String(60), ForeignKey('places.id'), nullable=False, sort_order=3
        )
        user_id = mapped_column(
            String(60), ForeignKey('users.id'), nullable=False, sort_order=4
        )
        text = mapped_column(
            String(1024), nullable=False, sort_order=5
        )
else:
    class Review(BaseModel):
        place_id = ''
        user_id = ''
        text = ''
