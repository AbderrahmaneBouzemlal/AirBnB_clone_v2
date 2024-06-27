#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String, ForeignKey("states.id"), length=60, nullable=False)
    name = Column(String, length=128, nullable=False)
    states = relationship("State")

    def __init__(self, state_id, name):
        self.state_id = state_id
        self.name = name
        BaseModel.save()
