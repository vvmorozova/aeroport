from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Time, Table, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from classes import Plane, Airport, Flight
#from functions import filtration
engine = create_engine("postgresql://client:uw0ntgue22@localhost:5432/", echo=True)#creating an engine(connection to db)

Session = sessionmaker(bind=engine) #new session
session = Session()

q = false
while q == false:

    while (a!='Plane') and (a!='Airport') and(a!='Flight'):

         print('Print name of the table you want to work with (Plane, Airport or Flight): \n')

         a = input()

    print('Now you can work with table ', a)

    if a == 'Plane':

    	while (a!='filter') or (a!='sort') or (a!='add'):

            print('What do you want to do?(filter, sort, add)')

            a = input()

         if a == 'sort':

         	while (sort!='aircraft type') or  (sort !='first class') or (sort !='capacity'):
            print('Print sorting parameter:')
            sort = input()
            
        if (sort =='aircraft type'):
        	Plane.filter_aircraft_type()
 
         if a == 'filter':

         	while (sort !='aircraft type') or  (((sort !='first class') or (sort !='capacity')) and (value.isdigit())):

         	   print('First filter parameter and then its value:')
         	   sort = input()
         	   value = input()

         	if sort == 'aircraft type':
         		Plane.sort_aircraft_type(plane, session)

         if a == 'add':

         	Plane.add_plane(session)


    if a == 'Airport':

    if a == 'Flight':
    