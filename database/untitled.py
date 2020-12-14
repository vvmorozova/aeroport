import tkinter as tk
from tkinter import *
import tksheet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import *
from tkinter import ttk

my_w = tk.Tk()
my_w.geometry("600x400") 

my_conn = create_engine("postgresql://client:uw0ntgue22@localhost:5432/")
####### end of connection ####

r_set=my_conn.execute("SELECT * FROM plane")
i=0 
for aircraft_type in r_set: 
    for j in range(len(aircraft_type)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, aircraft_type[j])
    i=i+1
my_w.mainloop()