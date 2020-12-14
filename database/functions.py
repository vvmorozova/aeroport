from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Time, Table, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from classes import *

def add_flight(session):
	new_plane = Plane(aircraft_type = (input('aircraft_type ')), capacity = (input('capacity ')), first_class = (input('first_class ')))
	session.add(new_plane)
	return new_plane

def add_airport(session):
	new_plane = Plane(aircraft_type = (input('aircraft_type ')), capacity = (input('capacity ')), first_class = (input('first_class ')))
	session.add(new_plane)
	return new_plane