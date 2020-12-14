from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Time, Table, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import delete
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import select
from sqlalchemy.inspection import inspect
from sqlalchemy import text

engine = create_engine("postgresql://client:uw0ntgue22@localhost:5432/", echo=True)
Base = declarative_base()
metadata = MetaData()
def delete(table,ssession):
        return delete(table).where(table.id == value)

def save(session):
        return session.commit()

def refresh(session):
        return session.refresh()


class Plane(Base):
    __tablename__ = 'plane'
    id = Column(Integer, primary_key = True)
    aircraft_type = Column(String)
    capacity = Column(Integer)
    first_class = Column(Integer)
    
    def __repr__(self):
        return "<plane(type='%s', capacity='%d', first_class='%d')>" % (
                            self.aircraft_type, self.capacity, self.first_class)
    def add_plane(session, at, cp, fc):

        new_plane = Plane(aircraft_type = at, capacity = cp, first_class = fc)
        session.add(new_plane)
        session.commit()
        return new_plane

    def filter_capacity(value, table, session):
        return session.query(table).filter_by(capacity = value).all()

    def filter_aircraft_type(value, table, session):
        return session.query(table).filter_by(aircraft_type = value).all()

    def filter_first_class(value, table, session):
        return session.query(table).filter_by(first_class = value).all()


   

    def sort_capacity(session):
        return session.query('plane.capacity','plane.aircraft_type').order_by(text("plane.capacity")).all()

    def sort_aircraft_type(session):
        return session.query('plane').order_by(text("plane.aircraft_type")).all()

    def sort_first_class(session):
        return session.query('plane').order_by(text("plane.first_class")).all()


    
    #def print_table(table):
        
     #   table = inspect(engine)
      #  for i in metadata.aircraft_type:
       #     print (i.aircraft_type)
    
class Airport(Base):
    """Класс для представления аэропорта """
    __tablename__ = 'airport'
    id = Column(Integer, primary_key = True)
    airport_code = Column(String)
    town_name = Column(String)

    def __repr__(self):
        return "<airport(airport_code='%s', town_name'%s' " % (
							self.aircraft_type, self.capacity, self.first_class)
    def add_airport(session):
        new_plane = Plane(airport_code = (input('airport_code ')), town_name = (input('town_name ')))
        session.add(new_plane)
        return new_plane

    def filter_airport_code(value, table, session):
        return session.query(table).filter_by(airport_code = value).all()

    def filter_town_name(value, table, session):
        return session.query(table).filter_by(town_name = value).all()

    def sort_airport_code(value, table, session):
        return session.query(table).order_by(airport_code).all()

    def sort_town_name(value, table, session):
        return session.query(table).order_by(town_name).all()


class Flight(Base):
    """Класс для представления рейсов"""
    __tablename__ = 'flight'
    id = Column(Integer, primary_key = True)
    time = Column(Time)
    airline_code = Column(String)
    aircraft_type_id = Column(Integer, ForeignKey("plane.id"))
    aircraft_type = relationship("Plane", foreign_keys=[aircraft_type_id])
    departure_aiport_code_id = Column(Integer, ForeignKey("airport.id"))
    arrival_aiport_code_id = Column(Integer, ForeignKey("airport.id"))
    departure_aiport_code = relationship("Airport", foreign_keys=[departure_aiport_code_id])
    arrival_aiport_code = relationship("Airport", foreign_keys=[arrival_aiport_code_id])
    gate = Column(String)
    exit_number = Column(Integer)
    status = Column(String)

    def add_flight(session):
        new_plane = Plane(time = (input('time ')), airline_code = (input('airline_code ')), aircraft_type = (input('aircraft_type ')), departure_aiport_code = (input('departure_aiport_code ')), 
			                      arrival_aiport_code = (input('arrival_aiport_code ')), gate = (input('gate ')), exit_number = (input('exit_number ')), status = (input('status ')))
        session.add(new_plane)
        return new_plane

    def filter_time(value, table, session):
        return session.query(table).filter_by(time = value).all()

    def filter_airline_code(value, table, session):
        return session.query(table).filter_by(airline_code = value).all()
    
    def filter_aircraft_type(value, table, session):
        return session.query(table).filter_by(aircraft_type= value).all()

    def filter_departure_aiport_code(value, table, session):
        return session.query(table).filter_by(departure_aiport_code = value).all()

    def filter_arrival_aiport_code(value, table, session):
        return session.query(table).filter_by(arrival_aiport_code= value).all()

    def filter_gate(value, table, session):
        return session.query(table).filter_by(gate = value).all()

    def filter_exit_number(value, table, session):
        return session.query(table).filter_by(exit_number = value).all()

    def filter_status(value, table, session):
        return session.query(table).filter_by(status = value).all()

    def sort_time(value, table, session):
        return session.query(table).order_by(airport_code).all()

    def sort_airline_code(value, table, session):
        return session.query(table).order_by(town_name).all()

    def sort_aircraft_type(value, table, session):
        return session.query(table).order_by(aircraft_type).all()

    def sort_departure_aiport_code(value, table, session):
        return session.query(table).order_by(departure_aiport_code).all()

    def sort_arrival_aiport_code(value, table, session):
        return session.query(table).order_by(arrival_aiport_code).all()

    def sort_gate(value, table, session):
        return session.query(table).order_by(gate).all()

    def sort_exit_number(value, table, session):
        return session.query(table).order_by(exit_number).all()

    def sort_status(value, table, session):
        return session.query(table).order_by(status).all()

Base.metadata.create_all(engine)