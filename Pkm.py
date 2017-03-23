#The Elder Scrolls 6: Pokemon

from tkinter import *
from tkinter import ttk
import time

fenster = Tk()
fenster.title('The Elder Scrolls 6: Pokemon')
fenster.geometry('800x600')
fenster.resizable(0,0)

MyMenu = Menu()
fenster.configure(menu=MyMenu)
Menubutton1 = Menu(MyMenu)
MyMenu.add_cascade(label = 'Commands', menu = Menubutton1)
Menubutton1.add_command(label = 'Quit', command = fenster.destroy)


prof_eich = PhotoImage(file = 'prof eich.gif')
sprechblase = PhotoImage(file = 'sprechblase.gif')
Hooh = PhotoImage(file = 'hooh.gif')
boy = PhotoImage(file = 'boy.gif')
girl = PhotoImage(file = 'girl.gif')
schwarz = PhotoImage(file = 'schwarz.gif')
glumanda = PhotoImage(file = 'Glumanda.gif')
bisasam = PhotoImage(file = 'Bisasam.gif')
schiggy = PhotoImage(file = 'Schiggy.gif')
bg_for_pokechoice = PhotoImage(file = 'bg_for_pokechoice.gif')
schiggy_button = PhotoImage(file = 'Schiggy_Button.gif')
glumanda_button = PhotoImage(file = 'Glumanda_Button.gif')
bisasam_button = PhotoImage(file = 'Bisasam_Button.gif')

############################

Meine_Pokemons = []
spielen = False
Geschlecht = ''
Geld = 0
Pokebälle = 0
Mein_Max_Leben = 100
Mein_Aktuelles_Leben = 100

############################

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
    global logo, startbutton, shopbutton, quitbutton
    
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

    

Hauptmenü()
fenster.mainloop()
    