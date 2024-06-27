#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String, length=128, nullable=False)
    cities = relationship("City")

    def __init__(self, name):
        self.name = name
        BaseModel.save()

    @property
    def cities(self):
        """Returns the list of City instance with state_id
        equal to the current state.id"""
        all_cities = storage.all("City")
        city_list = []

        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
