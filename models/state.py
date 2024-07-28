#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(
            String(128), nullable=False
        )
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            back_populates='state'
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
