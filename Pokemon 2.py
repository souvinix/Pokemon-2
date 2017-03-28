#The Elder Scrolls 6: Pokemon

from tkinter import *
from tkinter import ttk
import time
import random

Ash_Transparent = True

fenster = Tk()
fenster.title('The Elder Scrolls 6: Pokemon')
fenster.geometry('800x600')
fenster.resizable(0,0)

MyMenu = Menu()
fenster.configure(menu=MyMenu)
Menubutton1 = Menu(MyMenu)
MyMenu.add_cascade(label = 'Commands', menu = Menubutton1)
Menubutton1.add_command(label = 'Quit', command = fenster.destroy)

pfad = 'Alle_Bilder/'

prof_eich = PhotoImage(file = pfad+'prof eich.gif')
sprechblase = PhotoImage(file = pfad+'sprechblase.gif')
Hooh = PhotoImage(file = pfad+'hooh.gif')
boy = PhotoImage(file = pfad+'boy.gif')
girl = PhotoImage(file = pfad+'girl.gif')
schwarz = PhotoImage(file = pfad+'schwarz.gif')
glumanda = PhotoImage(file = pfad+'Glumanda.gif')
bisasam = PhotoImage(file = pfad+'Bisasam.gif')
schiggy = PhotoImage(file = pfad+'Schiggy.gif')
bg_for_pokechoice = PhotoImage(file = pfad+'bg_for_pokechoice.gif')
schiggy_button = PhotoImage(file = pfad+'Schiggy_Button.gif')
glumanda_button = PhotoImage(file = pfad+'Glumanda_Button.gif')
bisasam_button = PhotoImage(file = pfad+'Bisasam_Button.gif')
aktionsblase = PhotoImage(file = pfad+'Aktionsblase.gif')

if Ash_Transparent == False:

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

elif Ash_Transparent == True:

    pfad2 = 'Ash_Transparent/'
    Nach_Links_stehen = PhotoImage(file = pfad2+'Von_links_stehen.png')
    Nach_Links_schritt1 = PhotoImage(file = pfad2+'Von_links_schritt1.png')
    Nach_Links_schritt2 = PhotoImage(file = pfad2+'Von_links_schritt2.png')
    Nach_Rechts_stehen = PhotoImage(file = pfad2+'Von_rechts_stehen.png')
    Nach_Rechts_schritt1 = PhotoImage(file = pfad2+'Von_rechts_schritt1.png')
    Nach_Rechts_schritt2 = PhotoImage(file = pfad2+'Von_rechts_schritt2.png')
    Nach_Unten_stehen = PhotoImage(file = pfad2+'Von_vorne_stehen.png')
    Nach_Unten_schritt1 = PhotoImage(file = pfad2+'Von_vorne_schritt1.png')
    Nach_Unten_schritt2 = PhotoImage(file = pfad2+'Von_vorne_schritt2.png')
    Nach_Oben_stehen = PhotoImage(file = pfad2+'Von_hinten_stehen.png')
    Nach_Oben_schritt1 = PhotoImage(file = pfad2+'Von_hinten_schritt1.png')
    Nach_Oben_schritt2 = PhotoImage(file = pfad2+'Von_hinten_schritt2.png')

testmap = PhotoImage(file = pfad+'Anfangsraum.gif')

############################

Meine_Pokemons = []
spielen = False
Geschlecht = ''
Geld = 0
Pokebälle = 0
Mein_Max_Leben = 100
Mein_Aktuelles_Leben = 100
sprinten = False

############################
#########Meine Räume########
############################

Ash_Haus_1 = False
Ash_Haus_2 = False
Ash_Haus_3 = False
Neuborkia = False

############################
########Meine Objekte#######
############################

Buch = False
Pikachu = False
Uhr = False
Pumelluff = False

def Ingame_Escape(event):
    Ingame()

def Ingame():
    global timerRIGHT, timerLEFT, timerDOWN, timerUP
    global Map_x, Map_y, Geschwindigkeit, Testmap, Ash_Haus_1, Map_Hit
    global ingame_fenster, Alle_Objekte, Ash, Pikachu, Buch, Uhr, Pumelluff, Aktionsblase
    
    Ash_Haus_1 = True
    try:
        Hauptmenü_Destroy()
        test_ingame.destroy()
    except:
        pass
    
    ingame_fenster = fenster
    ingame_fenster.title('Pokemon 2 - InGame')
    ingame_fenster.geometry('800x600')
    ingame_fenster.resizable(0,0)

################################
    Map_x = 369
    Map_y = 250
    Geschwindigkeit = 4
################################

    Schrittgeschwindigkeit1 = 0 #Muss 0 bleiben
    Schrittgeschwindigkeit2 = 7
    Schrittgeschwindigkeit3 = 14
    Schrittgeschwindigkeit4 = 21
    timerUP = 0
    timerDOWN = 0
    timerLEFT = 0
    timerRIGHT = 0

    AshDirection = 'Down'

    def Alle_Objekte():
        global Map_x, Map_y, AshDirection, Pikachu, Buch, Uhr, Pumelluff, Aktionsblase, Map_Hit

        if Ash_Haus_1 == True:
            #Bett
            if (Map_x < 297 and Map_y < 280 and Map_x < Map_y):
                Map_y += Geschwindigkeit
            elif (Map_x < 297 and Map_y < 280 and Map_x > Map_y):
                Map_x += Geschwindigkeit
                
            #Bett Pikachu(Objekt)
            if (Map_x < 305 and Map_y < 280):
                if(AshDirection == 'Left'):
                    Pikachu = True
                if(Pikachu == True and AshDirection != 'Left'):
                    Pikachu = False
                    Map_Hit = False
                    try:
                        Aktionsblase.destroy()
                    except:
                        pass
                    
            #Treppe
            if (Map_x > 494 and Map_y < 285 and Map_x < 500):
                Map_x -= Geschwindigkeit
            elif (Map_x > 494 and Map_y < 285 and Map_x > 500):
                Map_y += Geschwindigkeit
            #Treppe(Funktion)
            elif(Map_x > 490 and Map_y < 230):
                Ingame_2()

            #Pflanze
            if (Map_x > 520 and Map_y > 400 and Map_x > 525):
                Map_x -= Geschwindigkeit
            elif (Map_x > 520 and Map_y > 380 and Map_x > 525):
                Map_y -= Geschwindigkeit

            #Glastisch
                #Vorbeigehen können
            if (Map_x > 365 and Map_y > 405):
                if(Map_x > 365 and Map_y > 400 and Map_x < 480 and Map_y <= 412):
                    Map_y += Geschwindigkeit
            
            elif (Map_x > 480 and Map_y > 290):
                if(Map_x > 475 and Map_y > 290 and Map_y < 480 and Map_x <= 486):
                    Map_x += Geschwindigkeit
                #Obere und linke Seite
            elif(Map_x > 365 and Map_y > 290 and Map_x < 370 and not Map_x > 466):
                Map_x -= Geschwindigkeit
            elif(Map_x > 365 and Map_y > 285 and Map_x < 400 and not Map_y > 406):
                Map_y -= Geschwindigkeit

            #Couch
                #Vorbeigehen können
            if (Map_x > 300 and Map_y > 410):
                if(Map_x > 300 and Map_y > 410 and Map_x < 365 and Map_y <= 415):
                    Map_y += Geschwindigkeit
                    
            elif (Map_x > 360 and Map_y > 300):
                if(Map_x > 360 and Map_y > 300 and Map_x < 365 and Map_y <= 415):
                    Map_x += Geschwindigkeit

                #Obere und linke Seite
            elif(Map_x > 285 and Map_y > 300 and Map_x < 360 and not Map_x > 365 and Map_y < 410):
                Map_x -= Geschwindigkeit
            elif(Map_x > 285 and Map_y > 295 and Map_x < 360 and not Map_y > 315):
                Map_y -= Geschwindigkeit

                #Couch Pumelluff(Objekt)
            if(Map_x > 285 and Map_y > 330 and not Map_x > 367 and Map_y < 370):
                if(AshDirection == 'Left'):
                    Pumelluff = True
                if(Pumelluff == True and AshDirection != 'Left'):
                    Pumelluff = False
                    Map_Hit = False
                    try:
                        Aktionsblase.destroy()
                    except:
                        pass
                

            #Rand
                #OBEN
            if(Map_y < 215):
                Map_y = 215
                #Rand oben, Uhr (Objekt)
            if(Map_x > 435 and Map_y < 220 and Map_x < 455):
                if(AshDirection == 'Up'):
                    Uhr = True
                if(Uhr == True and AshDirection != 'Up'):
                    Uhr = False
                    Map_Hit = False
                    try:
                        Aktionsblase.destroy()
                    except:
                        pass

            
                #UNTEN
            if(Map_y > 444): 
                Map_y = 444
                #LINKS
            if (Map_x < 206): 
                Map_x = 206
                #RECHTS
            if(Map_x > 560):
                Map_x = 560
    
    def Key_Up(event):
        global Map_x, Map_y, timerUP, AshDirection
        timerUP += 1

        AshDirection = 'Up'
        

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

        Alle_Objekte()
        
        Map_y -= Geschwindigkeit
        Ash.place(x = Map_x, y = Map_y)
        
    def Key_Down(event):
        global Map_x, Map_y, timerDOWN, AshDirection

        AshDirection = 'Down'

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

        Alle_Objekte()

        Map_y += Geschwindigkeit
        Ash.place(x = Map_x, y = Map_y)
      
    def Key_Left(event):
        global Map_x, Map_y, timerLEFT, AshDirection

        AshDirection = 'Left'

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

        Alle_Objekte()

        Map_x -= Geschwindigkeit
        Ash.place(x = Map_x, y = Map_y)

    def Key_Right(event):
        global Map_x, Map_y, timerRIGHT, AshDirection

        AshDirection = 'Right'

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

        Alle_Objekte()

        Map_x += Geschwindigkeit
        Ash.place(x = Map_x, y = Map_y)

    if Ash_Haus_1 == True:
        Testmap = Label(ingame_fenster, image =testmap) 
        Testmap.place(x = 0, y = 0)
    elif Ash_Haus_2 == True:
        pass
    
    ingame_fenster.bind('<Key-Up>', Key_Up)
    ingame_fenster.bind('<Key-Down>', Key_Down)
    ingame_fenster.bind('<Key-Left>', Key_Left)
    ingame_fenster.bind('<Key-Right>', Key_Right)

    Ash = Label(ingame_fenster, image = Nach_Unten_stehen, bd = 0)
    Ash.place(x = Map_x, y = Map_y)

    if sprinten == True:
        sprintlabel = Label(ingame_fenster, text = 'Sprinten (G), Entsprinten (F)', font = ('Terminator Two', 10))
        sprintlabel.configure(bg = 'light blue', fg = 'dark blue')
        sprintlabel.place(x = 550, y = 570)

    aktionslabel = Label(ingame_fenster, text = 'Aktion(K)', font = ('Terminator Two', 15))
    aktionslabel.configure(bg = 'light blue', fg = 'dark blue')
    aktionslabel.place(x = 550, y = 570)

    ingame_fenster.bind('<Key-o>', Pos)
    ingame_fenster.bind('<Key-O>', Pos)

    def Ingame_2():
        global Testmap, Alle_Objekte
        del Alle_Objekte
        def Alle_Objekte():
            pass
        Testmap.destroy()
        
        
        
    Map_Hit = False
    def Aktion(event):
        global AshDirection, Pikachu, Aktionsblase, Map_x, Map_y, Map_Hit, Pumelluff, Uhr, Buch
        if(Pikachu == True):
            if Map_Hit == False:
                Aktionsblase = Label(fenster, image = aktionsblase,
                             compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                Aktionsblase.place(x = 175, y = 475)
                Aktionsblase.configure(text = 'Dies ist ein Pikachu !\naber kein echtes...')
                Map_Hit = True
            elif Map_Hit == True:
                pass
            
        elif(Pumelluff == True):
            if Map_Hit == False:
                Aktionsblase = Label(fenster, image = aktionsblase,
                             compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                Aktionsblase.place(x = 175, y = 475)
                Aktionsblase.configure(text = 'Ein pumeliges Pumelluff !')
                Map_Hit = True
            elif Map_Hit == True:
                pass

        elif(Uhr == True):
            if Map_Hit == False:
                Aktionsblase = Label(fenster, image = aktionsblase,
                             compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                Aktionsblase.place(x = 175, y = 475)
                Aktionsblase.configure(text = 'Die Uhr ist sehr verstaubt...\nfinde etwas um sie\nsauber zu machen.')
                Map_Hit = True
            elif Map_Hit == True:
                pass
                
            

        

    fenster.bind('<Key-k>', Aktion)
    fenster.bind('<Key-K>', Aktion)

def Maus_Pos(event):
    global ingame_fenster
    x, y = event.x, event.y
    print('x = {}, y = {}'.format(x, y))
    ingame_fenster.bind('<Motion>', Maus_Pos)
    try:
        fenster.bind('<Key-x>', Maus_Pos)
    except:
        pass
    
def Pos(event):
        print('-'*20)
        print('Map_x = {}, Map_y = {}'.format(Map_x, Map_y))
        print('-'*20)

def weiter1():
    nextbutton.configure(command = weiter2)
    message = 'Unser\nVorstellungsgespräch\nist erst in\n10 Minuten!!!'
    text.configure(text = message)
    text.place(x = 190, y = 155)
def weiter2():
    nextbutton.configure(command = weiter3)
    message = 'Unser\nVorstellungsgespräch\nist erst in\n10 Minuten!!!\negal ich erzähle\ndir etwas'
    text.configure(text = message)
def weiter3():
    nextbutton.configure(command = weiter4)
    message = '...'
    text.configure(text = message, font = ('Terminator Two', 60))
    text.place(x = 280, y = 165)
def weiter4():
    global yes_button, no_button
    nextbutton.configure(command = weiter5, state = 'disabled')
    message = 'Sicher hast du\nschon etwas über\nPokemon gehört, richtig?'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 190, y = 150)

    yes_button = Button(fenster, text = 'Ja', font = ('Terminator Two', 20), bd = 0)
    yes_button.configure(bg = 'light grey', fg = 'black', command = JA)
    yes_button.place(x = 220, y = 210)

    no_button = Button(fenster, text = 'Nein', font = ('Terminator Two', 20), bd = 0)
    no_button.configure(bg = 'light grey', fg = 'black', command = NEIN)
    no_button.place(x = 300, y = 210)
def JA():
    yes_button.destroy()
    no_button.destroy()
    message = 'Gut, dann muss ich\ndir dazu nicht\nviel sagen...'
    nextbutton.configure(state = 'normal')
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 215, y = 140)
    
def NEIN():
    no_button.destroy()
    yes_button.configure(text = 'Weiter', font = ('Terminator Two', 12), command = _next1_)
    yes_button.place(x = 275, y = 240)
    message = 'Was?!'
    text.configure(text = message, font = ('Terminator Two', 20))
    text.place(x = 260, y = 160)
def _next1_():
    message = 'Nagut, Pokemon sind\nLebewesen die uns\nschon lange begleiten\nmanche zähmen sie\nund nutzen sie\nals Haustiere\noder kämpfen mit\nihnen'
    text.configure(text = message, font = ('Terminator Two', 10))
    text.place(x = 215, y = 125)
    yes_button.configure(command = _next2_)
def _next2_():
    message = 'Niemand weiß,\nwie sie entstanden\nsind. Vielleicht findest\ndu es ja\nheraus!'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 200, y = 135)
    yes_button.configure(command = _next3_)
def _next3_():
    message = 'Nun gut,\ndie Zeit wird knapp\nich zeige dir\nmein Pokemon!'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 215, y = 160)
    yes_button.destroy()
    nextbutton.configure(state = 'normal', command = weiter6)
def weiter5():
    nextbutton.configure(command = weiter6)
    message = 'Gut, dann muss ich\ndir dazu nicht\nviel sagen...\n\nwenn du willst,\nkann ich dir meins\nzeigen!'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 215, y = 140)
def weiter6():
    global hooh
    nextbutton.configure(command = weiter7)
    message = 'Das ist Ho-oh,\nes war einst ein\nLegendäres Pokemon,\nheute gibt es\ntausende Klone\nvon ihm.'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 210, y = 140)

    hooh = Label(fenster, image = Hooh, width = 225, height = 250)
    hooh.place(x = 200, y = 285)
def weiter7():
    global a1,a2
    nextbutton.configure(command = weiter8, state = 'disabled')
    message = 'Nach "Pokemon XY"\nhat sich alles\nverändert...'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 210, y = 140)

    a1 = Button(fenster, text = 'Pokemon X/Y?', font = ('Terminator Two', 12), bd = 0)
    a1.configure(bg = 'light grey', fg = 'black', command = A1)
    a1.place(x = 225, y = 200)

    a2 = Button(fenster, text = 'Ich verstehe', font = ('Terminator Two', 12), bd = 0)
    a2.configure(bg = 'light grey', fg = 'black', command = A2)
    a2.place(x = 225, y = 235)
def A1():
    global weiter_button
    a1.destroy()
    a2.destroy()
    message = '"Pokemon XY" ist\neine Epoche, wo\nviele neue Pokemons\nentdeckt wurden,\ndazu gehören auch\nLegendäre Pokemons '
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 200, y = 130)

    weiter_button = Button(fenster, bd = 0)
    weiter_button.configure(bg = 'light grey', fg = 'black', command = next1_xy)
    weiter_button.configure(text = 'Weiter', font = ('Terminator Two', 12))
    weiter_button.place(x = 275, y = 240)
def next1_xy():
    weiter_button.configure(command = next2_xy)
    message = 'Pokemons\ndie einst\nmal besonders waren\nwie Ho-oh, Mew,\nLugia, Darkrai usw.\n wurden von\nTeam Rockett kopiert...'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 200, y = 120)
def next2_xy():
    weiter_button.configure(command = next3_xy)
    message = 'Eigentlich möchte\n ich nicht viel\n Wort darüber verlieren\nich hoffe, ich\nfinde jemanden\nder das\nrückgängig machen\nkann.'
    text.configure(text = message, font = ('Terminator Two', 10))
    text.place(x = 200, y = 120)
def next3_xy():
    weiter_button.destroy()
    message = '...'
    text.configure(text = message, font = ('Terminator Two', 60))
    text.place(x = 280, y = 165)
    nextbutton.configure(state = 'normal', command = weiter8)
def A2():
    a1.destroy()
    a2.destroy()
    weiter8()
def weiter8():
    global name_entry_label, name_entry, name_entry_label2, name, message, text
    nextbutton.configure(state = 'normal', command = weiter9)
    message = 'Naja...\nNun zu dir!\nwie ist dein Name?'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 220, y = 120)

    name_entry_label = Label(fenster, text = 'Mein Name ist', font = ('Terminator Two', 10), fg = 'red')
    name_entry_label.place(x = 250, y = 180)
    
    name_entry = Entry(fenster, bd = 0)
    name_entry.place(x = 250, y = 200)
    
    name_entry_label2 = Label(fenster, text = 'Schön sie\nkennenzulernen', font = ('Terminator Two', 10), fg = 'red')
    name_entry_label2.place(x = 240, y = 220)

    name = name_entry.get()
def weiter9():
    name = name_entry.get()
    if (name == ''):
        pass
    else:
        text.configure(text = '')
        name_entry_label.destroy()
        name_entry.destroy()
        name_entry_label2.destroy()
        message = str(name)+'\nbist du\nmännlich\noder\nweiblich?'
        Sprechblase.configure(text = message, font = ('Terminator Two', 11), compound = 'center')
        nextbutton.configure(command = weiter10)
def weiter10():
    global männlich, weiblich
    Sprechblase.configure(text = '')
    nextbutton.configure(command = weiter12)
    nextbutton.configure(state = 'disabled')
    message = ''
    text.configure(text = message, font = ('Terminator Two', 11))

    männlich = Button(fenster, image = boy, command = männlich_choice, bd = 0)
    männlich.place(x = 250, y = 130)

    weiblich = Button(fenster, image = girl, command = weiblich_choice, bd = 0)
    weiblich.place(x = 310, y = 130)
    
    männlich.bind('<Enter>', männlich_enter)
    männlich.bind('<Leave>', männlich_leave)
    weiblich.bind('<Enter>', weiblich_enter)
    weiblich.bind('<Leave>', weiblich_leave)

def männlich_enter(event):
    männlich.configure(bd = 2)
def männlich_leave(event):
    männlich.configure(bd = 0)
def weiblich_enter(event):
    weiblich.configure(bd = 2)
def weiblich_leave(event):
    weiblich.configure(bd = 0)

def männlich_choice():
    männlich.destroy()
    weiblich.destroy()
    Geschlecht = 'männlich'
    weiter11()
def weiblich_choice():
    männlich.destroy()
    weiblich.destroy()
    Geschlecht = 'weiblich'
    weiter11()
    
def weiter11():
    nextbutton.configure(state = 'normal')
    message = 'Interessant!\n...\nIch habe eine\nÜberraschung für\ndich'
    text.configure(text = message, font = ('Terminator Two', 11))
    text.place(x = 220, y = 155)
def weiter12():
    global okay_button
    nextbutton.configure(state = 'disabled')
    message = 'SCHLIEßE\nDEINE\nAUGEN!'
    text.configure(text = message, font = ('Terminator Two', 20))
    text.place(x = 235, y = 135)
    
    okay_button = Button(fenster, text = 'Okay', font = ('Terminator Two', 15), bd = 0)
    okay_button.configure(bg = 'light grey', fg = 'red', command = weiter13)
    okay_button.place(x = 265, y = 230)
    
def weiter13():
    global schwarzes_bild, augenauf
    schwarzes_bild = Label(fenster, image = schwarz)
    schwarzes_bild.place(x = 0, y = 0)
    
    augenauf = Button(fenster, text = 'Augen\nöffnen', bg = 'black', fg = 'white', font = ('Terminator Two', 50))
    augenauf.configure(bd = 0, command = weiter14)
    augenauf.place(x = 225, y = 215)


def weiter14():
    global Glumanda, Bisasam, Schiggy, text1, bgforpokechoice
    try:
        schwarzes_bild.destroy()
        augenauf.destroy()
        Eich.destroy()
        Sprechblase.destroy()
        text.destroy()
        okay_button.destroy()
        hooh.destroy()
        message = ''
        nextbutton.destroy()
    except:
        pass

    y = 80
    
    bgforpokechoice = Label(fenster, image = bg_for_pokechoice)
    bgforpokechoice.place(x = 0, y = y)

    fenster.configure(bg = 'white')
    Schiggy = Button(fenster, text = 'Schiggy', image = schiggy_button, bd = 0, compound = 'center', fg = 'white',
                     font = ('Terminator Two', 20), command = schiggy_command)
    Schiggy.place(x = 2,y = y)

    Glumanda = Button(fenster, text = 'Glumanda', image = glumanda_button, bd = 0, compound = 'center', fg = 'white',
                      font = ('Terminator Two', 20), command = glumanda_command)
    Glumanda.place(x = 273,y = y)

    Bisasam = Button(fenster, text = 'Bisasam', image = bisasam_button, bd = 0, compound = 'center', fg = 'white',
                     font = ('Terminator Two', 20), command = bisasam_command)
    Bisasam.place(x = 540,y = y)

    text1 = Label(fenster, text = 'Wähle dein eigenes Pokemon', bg = 'white', fg = 'black',
                 font = ('Terminator Two', 30))
    text1.place(x = 50, y = 30)

def pokechoice_destroy():
    global ja_button, nein_button
    bgforpokechoice.destroy()
    Schiggy.destroy()
    Glumanda.destroy()
    Bisasam.destroy()
    backbutton.destroy()
    text1.configure(text = 'Bist du sicher?')
    text1.place(x = 205, y = 200)

    ja_button = Button(fenster, text='Ja', font = ('Terminator Two', 40), bg = 'light grey', fg = 'black')
    ja_button.configure(command = __Ja__, bd = 0)
    ja_button.place(x = 230, y = 250)

    nein_button = Button(fenster, text='Nein', font = ('Terminator Two', 40), bg = 'light grey', fg = 'black')
    nein_button.configure(command = __Nein__, bd = 0)
    nein_button.place(x = 380, y = 250)

def __Ja__():
    ja_button.destroy()
    nein_button.destroy()
    text1.configure(text = 'Eine Zeit später...')
    text1.place(x=190,y=200)
    
def __Nein__():
    ja_button.destroy()
    nein_button.destroy()
    text1.destroy()
    anfangspokemon = ''
    weiter14()

def schiggy_command():
    pokechoice_destroy()
    anfangspokemon = 'Schiggy'

def glumanda_command():
    pokechoice_destroy()
    anfangspokemon = 'Glumanda'
    
def bisasam_command():
    pokechoice_destroy()
    anfangspokemon = 'Bisasam'

def back():
    Start_Destroy()
    Hauptmenü()
    spielen = False

def Start_Destroy():
    backbutton.destroy()
    Eich.destroy()
    Sprechblase.destroy()
    nextbutton.destroy()
    text.destroy()
    try:
        hooh.destroy()
    except:
        pass
    try:
        text.destroy()
    except:
        pass
    try:
        name_entry_label.destroy()
        name_entry.destroy()
        name_entry_label2.destroy()
    except:
        pass
    try:
        a1.destroy()
        a2.destroy()
    except:
        pass
    try:
        weiter_button.destroy()
    except:
        pass
    try:
        yes_button.destroy()
    except:
        pass
   
    try:
        no_button.destroy()
    except:
        pass
    
    

def start():
    global backbutton, Eich, Sprechblase, nextbutton, text

    spielen = True
    message = 'Hallo Abenteurer,\n mein Name ist Prof. Eich\n'
    
    Hauptmenü_Destroy()
    backbutton = Button(fenster, text = 'Hauptmenü', font = ('Terminator Two', 10), bg = 'light grey')
    backbutton.configure(fg = 'red', command = back, bd = 0)
    backbutton.place(x = 5, y = 5)
    backbutton.bind('<Enter>', backbutton_enter)
    backbutton.bind('<Leave>', backbutton_leave)

    nextbutton = Button(fenster, text = 'Weiter', bg = 'light grey', fg = 'red', font = ('Terminator Two', 15))
    nextbutton.configure(bd = 0, command = weiter1)
    nextbutton.place(x = 350, y = 550)

    Eich = Label(fenster, image = prof_eich)
    Eich.place(x = 500, y = 200)

    Sprechblase = Label(fenster, image = sprechblase)
    Sprechblase.place(x = 170, y = 50)

    text = Label(fenster, text = message, fg = 'black', font = ('Terminator Two', 11))
    text.place(x = 185, y = 175)

def shop():
    pass

def Hauptmenü_Destroy():
    logo.destroy()
    startbutton.destroy()
    quitbutton.destroy()
    shopbutton.destroy()

def startbutton_enter(event):
    startbutton.configure(bg = 'snow')
def startbutton_leave(event):
    startbutton.configure(bg = 'light grey')
def shopbutton_enter(event):
    shopbutton.configure(bg = 'snow')
def shopbutton_leave(event):
    shopbutton.configure(bg = 'light grey')
def quitbutton_enter(event):
    quitbutton.configure(bg = 'snow')
def quitbutton_leave(event):
    quitbutton.configure(bg = 'light grey')
def backbutton_enter(event):
    backbutton.configure(bg = 'snow')
def backbutton_leave(event):
    backbutton.configure(bg = 'light grey')

def Hauptmenü():
    global logo, startbutton, shopbutton, quitbutton, test_ingame
    
    logo = Label(fenster, text = 'Pokémon', fg = 'red', bg = 'light grey', font = ('Terminator Two', 80))
    logo.place(x = 110, y = 50)

    startbutton = Button(fenster, text = 'Starten', font = ('Terminator Two', 50), bd = 0, bg = 'light grey')
    startbutton.configure(fg = 'black', activebackground = 'light grey', command = start)
    startbutton.place(x = 190, y = 200)

    shopbutton = Button(fenster, text = 'Shop', font = ('Terminator Two', 50), bd = 0, bg = 'light grey')
    shopbutton.configure(fg = 'black', activebackground = 'light grey', command = shop)
    shopbutton.place(x = 260, y = 320)

    quitbutton = Button(fenster, text = 'Verlassen', font = ('Terminator Two', 50), bd = 0, bg = 'light grey')
    quitbutton.configure(fg = 'black', activebackground = 'light grey', command = fenster.destroy)
    quitbutton.place(x = 140, y = 440)

    startbutton.bind('<Enter>', startbutton_enter)
    startbutton.bind('<Leave>', startbutton_leave)

    shopbutton.bind('<Enter>', shopbutton_enter)
    shopbutton.bind('<Leave>', shopbutton_leave)

    quitbutton.bind('<Enter>', quitbutton_enter)
    quitbutton.bind('<Leave>', quitbutton_leave)

    test_ingame = Button(fenster, text = 'Test\nIngame', font = ('Terminator Two', 20), fg = 'black')
    test_ingame.configure(command = Ingame)
    test_ingame.place(x = 600, y = 350)
    fenster.bind('<Key-l>', Ingame_Escape)
    

Hauptmenü()
fenster.mainloop()
