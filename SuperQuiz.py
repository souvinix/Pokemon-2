from tkinter import *
import random
import sqlite3
import os

try:
    Verzeichnis = ('/Users/noahg/Desktop/SuperQuiz2')
    if not os.path.exists(Verzeichnis):
        os.makedirs(Verzeichnis)
except:
    Verzeichnis = ('/home/nwantoch/Arbeitsfläche/SuperQuiz2')
    if not os.path.exists(Verzeichnis):
        os.makedirs(Verzeichnis)
try:
    connection = sqlite3.connect('/Users/noahg/Desktop/SuperQuiz2/SuperDatabase.db')
except:
    try:
        connection = sqlite3.connect('/home/nwantoch/Arbeitsfläche/SuperQuiz2')
    except:
        connection = sqlite3.connect('SuperDatabase.db')

cursor = connection.cursor()
command = ('create table if not exists Quiz (Frage, a1, a2, a3, a4);')
cursor.execute(command)

fenster = Tk()
fenster.title('SuperQuiz')
fenster.geometry('800x600')
fenster.resizable(0,0)

class Hauptmenü(object):
    def __init__(self, master):
        def start():
            pass
        self.logo_pos = 0
        self.logo_y = 0
        
        self.master = master
        self.MyCanvas = Canvas(self.master, width = 800, height = 600)
        self.MyCanvas.place(x = 0, y = 0)

        self.logo = self.MyCanvas.create_text(400, 100, text = 'SuperQuiz', fill = 'red',
                                              font = ('Terminator Two', 80), tags = 'Logo')

        self.startbutton = Button(self.master, text = 'Starten', font = ('Terminator Two', 50),
                                  command = start, fg = 'blue', bd = 0)
        self.startbutton.place(x = 250, y = 300)

    def move_logo(self):
        Geschwindigkeit = 45
        if self.logo_pos == 0:
            self.logo_y = 1
        elif self.logo_pos == 25:
            self.logo_y = -1

        if self.logo_y == 1:
            self.logo_pos += 1
        elif self.logo_y == -1:
            self.logo_pos -= 1
        
        x = 0
        self.MyCanvas.move(self.logo, x, self.logo_y)
        self.MyCanvas.after(Geschwindigkeit, self.move_logo)

    def move_startbutton(self):
        if self.logo_pos == 0:
            self.y = 1
        elif self.logo_pos == 25:
            self.y = -1

        if self.logo_y == 1:
            self.logo_pos += 1
        elif self.logo_y == -1:
            self.logo_pos -= 1
        
        x = 0
        self.MyCanvas.move(self.logo, x, self.logo_y)
        self.MyCanvas.after(30, self.move_logo)

    def move_ALL(self):
        self.move_logo()
        self.move_startbutton()
        

MeinHauptmenü = Hauptmenü(fenster)
MeinHauptmenü.move_ALL()
fenster.mainloop()

    
        

