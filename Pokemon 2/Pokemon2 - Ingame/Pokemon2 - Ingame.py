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
def Sprint_Beenden(event):
    global Geschwindigkeit, Sprint_Geschwindigkeit
    Geschwindigkeit = 10

Schrittgeschwindigkeit1 = 0 #Muss 0 sein
Schrittgeschwindigkeit2 = 7
Schrittgeschwindigkeit3 = 14
Schrittgeschwindigkeit4 = 21
timerUP =
0
timerDOWN = 0
timerLEFT = 0
timerRIGHT = 0

def Map_Up(event):
    global testmap_x, testmap_y, timerUP
    timerUP += 1

    if (timerUP >= Schrittgeschwindigkeit1):
        Ash.configure(image = Nach_Oben_schritt1)
    if (timerUP >= Schrittgeschwindigkeit2):
        Ash.configure(image = Nach_Oben_stehen)
    if (timerUP >= Schrittgeschwindigkeit3):
        Ash.configure(image = Nach_Oben_schritt2)
    if (timerUP >= Schrittgeschwindigkeit4):
        timerUP = 0
    if(timerUP == 0):
        Ash.configure(image = Nach_Oben_stehen)
    
    testmap_y += Geschwindigkeit
    Testmap.place(x = testmap_x, y = testmap_y)
def Map_Down(event):
    global testmap_x, testmap_y, timerDOWN

    timerDOWN += 1

    if (timerDOWN >= Schrittgeschwindigkeit1):
        Ash.configure(image = Nach_Unten_schritt1)
    if (timerDOWN >= Schrittgeschwindigkeit2):
        Ash.configure(image = Nach_Unten_stehen)
    if (timerDOWN >= Schrittgeschwindigkeit3):
        Ash.configure(image = Nach_Unten_schritt2)
    if (timerDOWN >= Schrittgeschwindigkeit4):
        timerDOWN = 0
    if(timerDOWN == 0):
        Ash.configure(image = Nach_Unten_stehen)

    testmap_y -= Geschwindigkeit
    Testmap.place(x = testmap_x, y = testmap_y)
def Map_Left(event):
    global testmap_x, testmap_y, timerLEFT

    timerLEFT += 1

    if (timerLEFT >= Schrittgeschwindigkeit1):
        Ash.configure(image = Nach_Links_schritt1)
    if (timerLEFT >= Schrittgeschwindigkeit2):
        Ash.configure(image = Nach_Links_stehen)
    if (timerLEFT >= Schrittgeschwindigkeit3):
        Ash.configure(image = Nach_Links_schritt2)
    if (timerLEFT >= Schrittgeschwindigkeit4):
        timerLEFT = 0
    if(timerLEFT == 0):
        Ash.configure(image = Nach_Links_stehen)
        
    testmap_x += Geschwindigkeit
    Testmap.place(x = testmap_x, y = testmap_y)
def Map_Right(event):
    global testmap_x, testmap_y, timerRIGHT

    timerRIGHT += 1

    if (timerRIGHT >= Schrittgeschwindigkeit1):
        Ash.configure(image = Nach_Rechts_schritt1)
    if (timerRIGHT >= Schrittgeschwindigkeit2):
        Ash.configure(image = Nach_Rechts_stehen)
    if (timerRIGHT >= Schrittgeschwindigkeit3):
        Ash.configure(image = Nach_Rechts_schritt2)
    if (timerRIGHT >= Schrittgeschwindigkeit4):
        timerRIGHT = 0
    if(timerRIGHT == 0):
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

#Entsprinten
fenster.bind('<Key-F>', Sprint_Beenden)
fenster.bind('<Key-f>', Sprint_Beenden)

LOL = Label(fenster, font = ('Terminator Two', 30))
LOL.place(x = 0,y = 0)

Ash = Label(fenster, image = Nach_Rechts_stehen, bd = 0)
Ash.place(x = 370, y = 250)




fenster.mainloop()

