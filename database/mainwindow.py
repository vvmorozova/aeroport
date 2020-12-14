import tkinter as tk
from tkinter import *
import tksheet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import *
from tkinter import ttk
import time
from tkinter import messagebox as mb
engine = create_engine("postgresql://client:uw0ntgue22@localhost:5432/", echo=True)#creating an engine(connection to db)

Session = sessionmaker(bind=engine) #new session
session = Session()

class PlaneWindow(Toplevel): 

    def add_plane(newwindow):
         
        self = Tk()
        self.resizable(width=False, height=False)
        self.title("Добавить самолёт") 
        self.geometry("400x250") 
        
        def logicfunc(capacitytxt, typetxt, first_classtxt):
            if (capacitytxt.get().isdigit()) and (first_classtxt.get().isdigit()) and (typetxt.get().strip()):
                if int(capacitytxt.get()) < int(first_classtxt.get()):
                    mb.showerror("Ошибка", "Успех!")
                else:
                    addbtn = Button(self, text = "Добавить",font = ("Arial", 10), width = 10, state = NORMAL, command = Plane.add_plane(session, typetxt.get(), int(capacitytxt.get()), int(first_classtxt.get()))) 
                    addbtn.place(x = 160, y = 210)

            else:
                addbtn = Button(self, text = "Добавить",font = ("Arial", 10), width = 10, state = DISABLED)
                addbtn.place(x = 160, y = 210)
                print('False')

        typetxt = Entry(self, width = 40) 
        typetxt.place(x = 30, y = 30)

        typelbl = Label(self, text = "Модель самолета",font = ("Arial", 10)) 
        typelbl.place(x = 135, y = 5)

        capacitytxt = Entry(self, width = 40) 
        capacitytxt.place(x = 30, y = 100)

        capacitylbl = Label(self, text = "Вместимость",font = ("Arial", 10)) 
        capacitylbl.place(x = 150, y=75)

        first_classtxt = Entry(self, width = 40) 
        first_classtxt.place(x = 30, y = 170)

        first_classlbl = Label(self, text = "Количество мест в бизнес-классе",font = ("Arial", 10)) 
        first_classlbl.place(x = 90, y = 145)
        refreshbtn = Button(self, text = "Обновить",font = ("Arial", 10), width = 10) 
        refreshbtn.place(x = 300, y = 210)
        refreshbtn.bind("<Button>", lambda e: logicfunc(capacitytxt, typetxt, first_classtxt)) 

        self. after(50, logicfunc(capacitytxt, typetxt, first_classtxt))
            

        
        self.mainloop()

    def refreshit(session):
        refresh(plane,session)

    def sort(newwindow):
        self = Tk()
        self.resizable(width=False, height=False)
        self.title("Сортировать по:") 
        self.geometry("400x250") 

        refreshbtn = Button(self, text = "Модели самолета",font = ("Arial", 10), width = 30) 
        refreshbtn.place(x = 80, y = 5)
        refreshbtn.bind("<Button>", lambda e: Plane.sort_aircraft_type(session) )

        refreshbtn = Button(self, text = "Вместимости",font = ("Arial", 10), width = 30) 
        refreshbtn.place(x = 80, y = 55)
        refreshbtn.bind("<Button>", lambda e: Plane.sort_capacity(session) ) 

        refreshbtn = Button(self, text = "Количеству мест в бизнес-классе",font = ("Arial", 10), width = 30) 
        refreshbtn.place(x = 80, y = 105)
        refreshbtn.bind("<Button>", lambda e: Plane.sort_first_class(session)) 


    def __init__(self, master = None): 
        
        self = tk.Tk()
        self.resizable(width=False, height=False)
        self.title("Таблица самолетов") 
        self.geometry("635x400") 
        my_conn = create_engine("postgresql://client:uw0ntgue22@localhost:5432/")

        r_set=my_conn.execute("SELECT * FROM plane")

        i=0 
        for aircraft_type in r_set: 
            for j in range(len(aircraft_type)):
                e = Entry(self, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, aircraft_type[j])
            i=i+1

        addbtn = Button(self, 
            text ="Добавить",font=("Arial", 20), width=17) 

        addbtn.bind("<Button>",lambda e: PlaneWindow.add_plane(master)) 

        addbtn.place(x=345, y=15)

        delbtn = Button(self, 
            text ="Удалить",font=("Arial", 20), width=17) 

        #addbtn.bind("<Button>", 
        #lambda e: PlaneWindow(master)) 

        delbtn.place(x=345, y=80)

        sortbtn = Button(self, 
            text ="Сортировать",font=("Arial", 20), width=17) 

        sortbtn.bind("<Button>", lambda e: PlaneWindow.sort(master)) 

        sortbtn.place(x=345, y=145)

        filterbtn = Button(self, 
            text ="Фильтры",font=("Arial", 20), width=17) 

        #filterbtn.bind("<Button>", lambda e: PlaneWindow.filter(master)) 

        filterbtn.place(x=345, y=210)

        refreshbtn = Button(self, 
            text ="Обновить",font=("Arial", 20), width=17) 

        refreshbtn.bind("<Button>",lambda e: PlaneWindow.refreshit(session)) 

        refreshbtn.place(x=345, y=275)

        savebtn = Button(self, 
            text ="Сохранить",font=("Arial", 20), width=17) 

        #addbtn.bind("<Button>", 
        #lambda e: PlaneWindow(master)) 

        savebtn.place(x=345, y=340)

        self.mainloop()

class FlightWindow(Toplevel): 
    
    def __init__(self, master = None): 
        
        super().__init__(master = master) 
        self.title("Таблица рейсов") 
        self.geometry("200x200") 
        label = Label(self, text ="This is a new Window") 
        label.pack() 


class AirportWindow(Toplevel): 
    
    def __init__(self, master = None): 
        
        super().__init__(master = master) 
        self.title("Таблица аэропортов") 
        self.geometry("200x200") 
        label = Label(self, text ="This is a new Window") 
        label.pack() 

master = Tk() 
master.title("База данных аэропорта") 
master.geometry("400x400") 
master.resizable(width=False, height=False)
label = Label(master, text ="Выберите таблицу:",font=("Arial", 30)) 
label.pack(side = TOP, pady = 20) 

planebtn = Button(master, 
            text ="Самолёты",font=("Arial", 20), width=20) 

planebtn.bind("<Button>", 
        lambda e: PlaneWindow(master)) 

planebtn.place(x=40, y=80)

flightbtn = Button(master, 
            text ="Рейсы",font=("Arial", 20), width=20) 

flightbtn.bind("<Button>", 
        lambda e: FlightWindow(master)) 

flightbtn.place(x=40, y=140)

airportbtn = Button(master, 
            text ="Аэропорты",font=("Arial", 20), width=20) 

airportbtn.bind("<Button>", 
        lambda e: AirportWindow(master)) 

airportbtn.place(x=40, y=200)

quitbtn = Button(master, 
            text ="Выход",font=("Arial", 12), width=10, command = master.destroy) 

quitbtn.place(x=270, y=360)


mainloop() 
