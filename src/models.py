import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class characters(Base):
     __tablename__ = 'characters'
     id = Column(Integer, primary_key=True)
     name = Column(String(250), nullable=False)
     age = Column(Integer, nullable=False)
     hair_color = Column(String(250), nullable=False)
     eye_color = Column(String(250), nullable=False)

class planets(Base):
     __tablename__ = 'planets'
     id = Column(Integer, primary_key=True)
     name = Column(String(250), nullable=False)
     population = Column(Integer, nullable=False)
     climate = Column(String(250), nullable=False)
     terrain = Column(String(250), nullable=False)

class vehicles(Base):
     __tablename__ = 'vehicles'
     id = Column(Integer, primary_key=True)
     name = Column(String(250), nullable=False)
     model = Column(String(250), nullable=False)
     cargo_capacity = Column(Integer, nullable=False)
     crew = Column(Integer, nullable=False)

class favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(characters)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(characters)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(vehicles)

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(favorites)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')