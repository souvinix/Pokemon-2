import sqlite3
from tkinter import *
import os

try:
    Verzeichnis = '/Users/All Users/Desktop/Thelegendofthestickman'
    if not os.path.exists(Verzeichnis):
        os.makedirs(Verzeichnis)
except:
    try:
        Verzeichnis = '/home/nwantoch/Arbeitsfläche/Thelegendofthestickman'
        if not os.path.exists(Verzeichnis):
            os.makedirs(Verzeichnis)
    except:
        Verzeichnis = '/home/eritorti/Arbeitsfläche/Thelegendofthestickman'
        if not os.path.exists(Verzeichnis):
            os.makedirs(Verzeichnis)
        

try:
    connection = sqlite3.connect(Verzeichnis+'/Database.db')
except:
    print('Fehler beim erstellen der Datenbank.')

cursor = connection.cursor()
command = 'create table if not exists User (Name, Passwort, Level, Geld);'
cursor.execute(command)

fenster = Tk()
fenster.title('TheLegendOfTheStickman')
fenster.geometry('1000x600')
fenster.resizable(0,0)

MyCanvas = Canvas(fenster, width = 1000, height = 600)
MyCanvas.place(x = 0, y = 0)

Menu_bg = PhotoImage(file = Verzeichnis+'/Menu_bg.gif')
startbutton_img = PhotoImage(file = Verzeichnis+'/Startbutton.gif')
startbutton_enter_img = PhotoImage(file = Verzeichnis+'/Startbutton_enter.gif')

class Mainmenu(object):
    def __init__(self, master, Canvas):
        self.master = master
        self.Canvas = Canvas
    def Aufrufen(self):
        def Startbutton_enter(event):
            self.Canvas.itemconfigure(self.Startbutton, image = startbutton_enter_img)
        def Startbutton_leave(event):
            self.Canvas.itemconfigure(self.Startbutton, image = startbutton_img)
            
        self.Canvas.create_image(400, 100, image = Menu_bg, tags = 'Menu_bg')
        self.Startbutton = self.Canvas.create_image(500, 250, image = startbutton_img)

        self.Canvas.tag_bind(self.Startbutton, '<Enter>', Startbutton_enter)
        self.Canvas.tag_bind(self.Startbutton, '<Leave>', Startbutton_leave)
        


Hauptmenü = Mainmenu(fenster, MyCanvas)
Hauptmenü.Aufrufen()
fenster.mainloop()
