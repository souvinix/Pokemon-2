from tkinter import *
from tkinter import ttk
import random
import time

fenster = Tk()
fenster.title('Pokemon 2 - InGame')
fenster.geometry('800x600')
fenster.resizable(0,0)

testmap_x = 0
testmap_y = 0
Geschwindigkeit = 10
Sprint_Geschwindigkeit = 20

def Sprint(event):
    global Geschwindigkeit, Sprint_Geschwindigkeit
    Geschwindigkeit = Sprint_Geschwindigkeit
def Ash_Pos(event):
    global LOL
    for pop in range(2000):
        x, y = event.x, event.y
        LOL.configure(text = str('x = '+x+' y = ')+y)
        

def Map_Up(event):
    global testmap_x, testmap_y
    Ash.configure(image = Nach_Oben_stehen)
    testmap_y += Geschwindigkeit
    Testmap.place(x = testmap_x, y = testmap_y)
def Map_Down(event):
    global testmap_x, testmap_y
    Ash.configure(image = Nach_Unten_stehen)
    testmap_y -= Geschwindigkeit
    Testmap.place(x = testmap_x, y = testmap_y)
def Map_Left(event):
    global testmap_x, testmap_y
    Ash.configure(image = Nach_Links_stehen)
    testmap_x += Geschwindigkeit
    Testmap.place(x = testmap_x, y = testmap_y)
def Map_Right(event):
    global testmap_x, testmap_y
    Ash.configure(image = Nach_Rechts_stehen)
    testmap_x -= Geschwindigkeit
    Testmap.place(x = testmap_x, y = testmap_y)

pfad = ''

Nach_Links_stehen = PhotoImage(file = pfad+'Von_links_stehen.gif')
Nach_Links_schritt1 = PhotoImage(file = pfad+'Von_links_schritt1.gif')
Nach_Links_schritt2 = PhotoImage(file = pfad+'Von_links_schritt2.gif')

Nach_Rechts_stehen = PhotoImage(file = pfad+'Von_rechts_stehen.gif')
Nach_Rechts_schritt1 = PhotoImage(file = pfad+'Von_rechts_schritt1.gif')
Nach_Rechts_schritt2 = PhotoImage(file = pfad+'Von_rechts_schritt2.gif')

Nach_Unten_stehen = PhotoImage(file = pfad+'Von_vorne_stehen.gif')
Nach_Unten_schritt1 = PhotoImage(file = pfad+'Von_vorne_schritt1.gif')
Nach_Unten_schritt2 = PhotoImage(file = pfad+'Von_vorne_schritt2.gif')

Nach_Oben_stehen = PhotoImage(file = pfad+'Von_hinten_stehen.gif')
Nach_Oben_schritt1 = PhotoImage(file = pfad+'Von_hinten_schritt1.gif')
Nach_Oben_schritt2 = PhotoImage(file = pfad+'Von_hinten_schritt2.gif')

testmap = PhotoImage(file = 'Testmap.gif')

Testmap = Label(fenster, image = testmap)
Testmap.place(x = testmap_x, y = testmap_y)
fenster.bind('<Key-Up>', Map_Up)
fenster.bind('<Key-Down>', Map_Down)
fenster.bind('<Key-Left>', Map_Left)
fenster.bind('<Key-Right>', Map_Right)

#Sprinten
fenster.bind('<Key-G>', Sprint)
fenster.bind('<Key-g>', Sprint)

LOL = Label(fenster, font = ('Terminator Two', 30))
LOL.place(x = 0,y = 0)

Ash = Label(fenster, image = Nach_Rechts_stehen, bd = 0)
Ash.place(x = 370, y = 250)
fenster.bind('<Key-f>', Ash_Pos)




fenster.mainloop()

