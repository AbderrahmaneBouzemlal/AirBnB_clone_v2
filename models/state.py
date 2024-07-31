#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column
from models.city import City


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = mapped_column(
            String(128), nullable=False, sort_order=3
        )
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
            )
else:
    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            """Returns the list of City instance with state_id
            equal to the current state.id"""
            from models import storage
            cities_all = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_all.append(value)
            return cities_all
