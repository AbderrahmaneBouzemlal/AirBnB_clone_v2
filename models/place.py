#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, mapped_column

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    ),
    mysql_engine='InnoDB',
    mysql_charset='latin1'
)
"""Represents the many to many relationship table
between Place and Amenity records.
"""

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1'
        }
        city_id = mapped_column(
            String(60), ForeignKey('cities.id'), nullable=False, sort_order=3
        )
        user_id = mapped_column(
            String(60), ForeignKey('users.id'), nullable=False, sort_order=4
        )
        name = mapped_column(
            String(128), nullable=False, sort_order=5
        )
        description = mapped_column(
            String(1024), nullable=True, sort_order=6
        )
        number_rooms = mapped_column(
            Integer, nullable=False, default=0, sort_order=7
        )
        number_bathrooms = mapped_column(
            Integer, nullable=False, default=0, sort_order=8
        )
        max_guest = mapped_column(
            Integer, nullable=False, default=0, sort_order=9
        )
        price_by_night = mapped_column(
            Integer, nullable=False, default=0, sort_order=10
        )
        latitude = mapped_column(
            Float, nullable=True, sort_order=11
        )
        longitude = mapped_column(
            Float, nullable=True, sort_order=12
        )
        reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan",
            backref='place'
        )
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            backref='place_amenities'
        )
else:
    class Place(BaseModel):
        """ A place to stay """
        city_id = ''
        user_id = ''
        name = ''
        description = 0
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0.0
        latitude = 0.0
        longitude = 0.0
        reviews = None

        amenity_ids = []

        @property
        def amenities(self):
            """Returns the amenities of this Place"""
            from models import storage
            amenities_of_place = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_of_place.append(value)
            return amenities_of_place

        @amenities.setter
        def amenities(self, value):
            """Adds an amenity to this Place"""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Returns the reviews of this Place"""
            from models import storage
            reviews_of_place = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_of_place.append(value)
            return reviews_of_place
