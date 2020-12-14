from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Time, Table, MetaData
from sqlalchemy.orm import relationship

engine = create_engine("postgresql://client:uw0ntgue22@localhost:5432/", echo=True)#creating an engine(connection to db)

#new table plane
meta_plane = MetaData()

plane = Table(
   'plane', meta_plane, 
   Column('id', Integer, primary_key = True), 
   Column('aircraft_type', String), 
   Column('capacity', Integer), 
   Column('first_class', Integer), 
)
meta_plane.create_all(engine)

#new table airport
meta_airport = MetaData()

airport = Table(
   'airport', meta_plane, 
   Column('id', Integer, primary_key = True), 
   Column('airport_code', String), 
   Column('town_name', String), 
)
meta_airport.create_all(engine)

#new table flight
meta_flight = MetaData()

flight = Table(
   'flight', meta_flight, 
   Column('id', Integer, primary_key = True), 
   Column('time', Time), 
   Column('airline_code', String), 
   Column('aircraft_type', String), 
   Column('departure_aiport_code', String), 
   Column('arrival_airport_code', String), 
   Column('gate', String), 
   Column('exit_number', Integer), 
   Column('status', String), 
)
meta_flight.create_all(engine)

with open('/home/vasuyan/airport/data/airport.csv', 'r') as f:    
    conn = create_engine('postgresql://client:uw0ntgue22@localhost:5432/').raw_connection()
    cursor = conn.cursor()
    cmd = 'COPY airport(airport_code, town_name) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
    cursor.copy_expert(cmd, f)
    conn.commit()