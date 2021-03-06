#The Elder Scrolls 6: Pokemon

from tkinter import *
from tkinter import ttk
import time
import random
from Pokemon_Klasse import *

fenster = Tk()
fenster.title('The Elder Scrolls 6: Pokemon')
fenster.geometry('800x600')
fenster.resizable(0,0)
from Pokemon_Photoimages import *

MyMenu = Menu()
fenster.configure(menu=MyMenu)
Menubutton1 = Menu(MyMenu)
MyMenu.add_cascade(label = 'Commands', menu = Menubutton1)
Menubutton1.add_command(label = 'Quit', command = fenster.destroy)

############################

Wasser = 0
Meine_Pokemons = []
spielen = False
Geschlecht = ''
Geld = 0
Pokebälle = 0
Mein_Max_Leben = 100
Mein_Aktuelles_Leben = 100
sprinten = False
Alle_Items = []
name = 'Unbekannt'
Mission = []

############################
#########Meine Räume########
############################
#Mit Ash_Pos:

    #Ash_Haus_Zimmer
    #Ash_Haus_Wohnzimmer
    #Ash_Haus_Küche

    #Neuborkia

############################
########Meine Objekte#######
############################

beginn = True
Buch = False
Pikachu = False
Uhr = False
Pumelluff = False
Fernseher = False
Wii = False
Mutter_unten = False
Mutter_links = False
Mutter_oben = False
Pokemon_Mutter = False
Schwester = False
Pokemon_Schwester = False
Bücherregal_Secret = False
Bücherregal = False
Blume = False
Blume_Item = False
Gold_Uhr = False
Waschbecken = False
Herdplatte = False
Bild = False
Kühlschrank = False
Kühlschrank_Item = False
Mülleimer = False

############################
def Ingame_Escape(event):
    Ingame()

def Ingame():
    global timerRIGHT, timerLEFT, timerDOWN, timerUP
    global Map_x, Map_y, Geschwindigkeit, Ingame_map, Ash_Pos, Map_Hit
    global ingame_fenster, Alle_Objekte, Ash, Pikachu, Buch, Uhr, Pumelluff, Aktionsblase, beginn

    time.sleep(0.5)
    
    Ash_Pos = 'Ash_Haus_Zimmer'
    try:
        Hauptmenü_Destroy()
        test_ingame.destroy()
    except:
        pass

    if beginn == True:
        ingame_fenster = fenster
        ingame_fenster.title('Pokemon 2 - InGame')
        ingame_fenster.geometry('800x600')
        ingame_fenster.resizable(0,0)
    elif beginn == False:
        pass

################################
    if beginn == True:
        Map_x = 369
        Map_y = 250
    elif beginn == False:
        Map_x = 500
        Map_y = 230
    Geschwindigkeit = 4
################################

    Schrittgeschwindigkeit1 = 0 #Muss 0 bleiben
    Schrittgeschwindigkeit2 = 6
    Schrittgeschwindigkeit3 = 12
    Schrittgeschwindigkeit4 = 18
    timerUP = 0
    timerDOWN = 0
    timerLEFT = 0
    timerRIGHT = 0

    if beginn == True:
        AshDirection = 'Down'
    elif beginn == False:
        AshDirection = 'Left'

    if beginn == True:
        def Alle_Objekte():
            global Map_x, Map_y, AshDirection, Pikachu, Buch, Uhr, Pumelluff, Aktionsblase, Map_Hit
            global Fernseher, Wii, Mutter, Pokemon_Mutter, Schwester, Pokemon_Schwester, Bücherregal, Bücherregal_Secret
            global Blume, Blume_Item, Wasser, Alle_Items, Mutter_oben, Mutter_links, Mutter_unten, Ja, Nein, Gold_Uhr
            global Waschbecken, Herdplatte, Kühlschrank, Mülleimer

            if Ash_Pos == 'Ash_Haus_Zimmer':
                #Bett
                if (Map_x < 300 and Map_y < 280 and Map_x < Map_y):
                    Map_y += Geschwindigkeit
                elif (Map_x < 315 and Map_y < 280 and Map_x > 310):
                    Map_x += Geschwindigkeit
                    
                #Bett Pikachu(Objekt)
                if (Map_x < 320 and Map_y < 250):
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
                if (Map_x > 510 and Map_y < 285 and Map_x < 515):
                    Map_x -= Geschwindigkeit
                elif (Map_x > 510 and Map_y < 285 and Map_x > 515):
                    Map_y += Geschwindigkeit
                #Treppe(Funktion)
                if(Map_x > 505 and Map_y < 260):
                    Ingame_2()

                #Pflanze
                if (Map_x > 535 and Map_y > 400):
                    Map_x -= Geschwindigkeit
                elif (Map_x > 550 and Map_y > 390 and not Map_y > 420):
                    Map_y -= Geschwindigkeit

                #Glastisch
                    #Vorbeigehen können
                if (Map_x > 385 and Map_y > 405):
                    if(Map_x > 385 and Map_y > 400 and Map_x < 480 and Map_y <= 412):
                        Map_y += Geschwindigkeit
                
                elif (Map_x > 475 and Map_y > 330):
                    if(Map_x < 490 and Map_y < 405):
                        Map_x += Geschwindigkeit

                    #Obere und linke Seite
                if(Map_x > 380 and Map_y > 330 and Map_x < 390 and Map_y < 405):
                    Map_x -= Geschwindigkeit
                elif(Map_x > 395 and Map_y > 305 and Map_x < 480 and Map_y < 325):
                    Map_y -= Geschwindigkeit


                    #Buch, von oben (Objekt)
                if(Map_x > 440 and Map_x < 465 and Map_y > 300 and Map_y < 310):
                    if(AshDirection == 'Down'):
                        Buch = True
                    if(Buch == True and AshDirection != 'Down'):
                        Buch = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    #Buch, von rechts (Objekt)
                elif(Map_x > 485 and Map_x < 495 and Map_y > 330 and Map_y < 360):
                    if(AshDirection == 'Left'):
                        Buch = True
                    if(Buch == True and AshDirection != 'Left'):
                        Buch = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    

                #Couch
                    #Vorbeigehen können
                if (Map_x > 305 and Map_y > 410):
                    if(Map_x > 300 and Map_y > 410 and Map_x < 365 and Map_y <= 415):
                        Map_y += Geschwindigkeit
                        
                elif (Map_x > 365 and Map_y > 340):
                    if(Map_x < 377 and Map_y < 405):
                        Map_x += Geschwindigkeit

                    #Obere und linke Seite
                if(Map_x > 300 and Map_y > 320 and Map_x < 310 and Map_y < 400):
                    Map_x -= Geschwindigkeit
                    
                elif(Map_x > 305 and Map_y > 310 and Map_x < 350 and Map_y < 330):
                    Map_y -= Geschwindigkeit

                    

                    #Couch Pumelluff(Objekt)
                if(Map_x > 365 and Map_y > 350 and Map_x < 384 and Map_y < 380):
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
                    Map_y += Geschwindigkeit
                    #Rand oben, Uhr (Objekt)
                if(Map_x > 440 and Map_y < 225 and Map_x < 465):
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
                if(Map_y > 460): 
                    Map_y -= Geschwindigkeit
                    #LINKS
                if (Map_x < 215): 
                    Map_x += Geschwindigkeit
                    #RECHTS
                if(Map_x > 580):
                    Map_x -= Geschwindigkeit

            elif Ash_Pos == 'Ash_Haus_Wohnzimmer':
                
                     #Rand
                #Linke Wand
                if(Map_x < 220):
                    Map_x += Geschwindigkeit
                #Untere Wand
                elif(Map_y > 470):
                    Map_y -= Geschwindigkeit
                #Rechte Wand
                elif(Map_x > 585):
                    Map_x -= Geschwindigkeit
                #Obere Wand
                elif(Map_y < 174):
                    Map_y += Geschwindigkeit

                    #Golduhr(Objekt)
                if(Map_x > 290 and Map_x < 315 and Map_y > 170 and Map_y < 180):
                    if(AshDirection == 'Up'):
                        Gold_Uhr = True
                    if(Gold_Uhr == True and AshDirection != 'Up'):
                        Gold_Uhr = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                #Zur Küche (Funktion)
                if(Map_x > 580 and Map_x < 590 and Map_y > 350 and Map_y < 400 and AshDirection == 'Right'):
                    Ingame3()

                    #Bücherregal
                if(Map_x > 505 and Map_x < 515 and Map_y > 170 and Map_y < 220):
                    Map_x -= Geschwindigkeit
                elif(Map_x > 517 and Map_x < 590 and Map_y > 210 and Map_y < 220):
                    Map_y += Geschwindigkeit

                    #Bücherregal_Secret(Objekt)
                if(Map_x > 504 and Map_x < 515 and Map_y > 165 and Map_y < 220):
                    if(AshDirection == 'Right'):
                        Bücherregal_Secret = True
                    if(Bücherregal_Secret == True and AshDirection != 'Right'):
                        Bücherregal_Secret = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    #Bücherregal(Objekt)
                if(Map_x > 537 and Map_x < 585 and Map_y > 215 and Map_y < 225):
                    if(AshDirection == 'Up'):
                        Bücherregal = True
                    if(Bücherregal == True and AshDirection != 'Up'):
                        Bücherregal = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    #Holztisch
                if(Map_x > 520 and Map_x < 590 and Map_y > 240 and Map_y < 255):
                    Map_y -= Geschwindigkeit
                elif(Map_x > 510 and Map_x < 520 and Map_y > 255 and Map_y < 320):
                    Map_x -= Geschwindigkeit
                elif(Map_x > 520 and Map_x < 590 and Map_y > 325 and Map_y < 335):
                    Map_y += Geschwindigkeit

                    #Blume, links(Objekt)
                if(Map_x > 505 and Map_x < 520 and Map_y > 270 and Map_y < 300):
                    if(AshDirection == 'Right'):
                        Blume = True
                    if(Blume == True and AshDirection != 'Right'):
                        Blume = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                            Got_Item.destroy()
                        except:
                            pass
                        
                    #Blume, oben(Objekt)
                elif(Map_x > 520 and Map_x < 560 and Map_y > 235 and Map_y < 250):
                    if(AshDirection == 'Down'):
                        Blume = True
                    if(Blume == True and AshDirection != 'Down'):
                        Blume = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                            Got_Item.destroy()
                        except:
                            pass

                    #Treppe
                if(Map_x > 280 and Map_x < 290 and Map_y > 170 and Map_y < 255):
                    Map_x += Geschwindigkeit
                elif(Map_x > 220 and Map_x < 270 and Map_y > 250 and Map_y < 265):
                    Map_y += Geschwindigkeit

                    #Treppe(Funktion)
                if(Map_x > 280 and Map_x < 295 and Map_y > 200 and Map_y < 222):
                    Ingame()

                    #Pflanze
                if(Map_x > 220 and Map_x < 260 and Map_y > 265 and Map_y < 295):
                    Map_x += Geschwindigkeit
                elif(Map_x > 220 and Map_x < 250 and Map_y > 295 and Map_y < 310):
                    Map_y += Geschwindigkeit

                    #Fernseher UND Konsole
                if(Map_x > 349 and Map_x < 360 and Map_y > 170 and Map_y < 210):
                    Map_x -= Geschwindigkeit
                if(Map_x > 350 and Map_x < 490 and Map_y > 205 and Map_y < 225):
                    Map_y += Geschwindigkeit
                elif(Map_x > 480 and Map_x < 495 and Map_y > 170 and Map_y < 210):
                    Map_x += Geschwindigkeit

                    #Fernseher(Objekt)
                if(Map_x > 375 and Map_x < 425 and Map_y > 220 and Map_y < 230):
                    if(AshDirection == 'Up'):
                        Fernseher = True
                    if(Fernseher == True and AshDirection != 'Up'):
                        Fernseher = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass
                    #Wii (Objekt)
                elif(Map_x > 435 and Map_x < 480 and Map_y > 220 and Map_y < 230):
                    if(AshDirection == 'Up'):
                        Wii = True
                    if(Wii == True and AshDirection != 'Up'):
                        Wii = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    #Mutter (Sitzt auf einem Stuhl)
                        #Von links
                if (Map_x > 340 and Map_x < 347 and Map_y > 285 and Map_y < 370):
                    Map_x -= Geschwindigkeit
                        #Von unten
                elif(Map_x > 345 and Map_x < 415 and Map_y > 360 and Map_y < 375):
                    Map_y += Geschwindigkeit
                        #Von rechts
                elif(Map_x > 405 and Map_x < 415 and Map_y > 285 and Map_y < 370):
                    Map_x += Geschwindigkeit
                        #Von oben
                elif(Map_x > 345 and Map_x < 415 and Map_y > 280 and Map_y < 290):
                    Map_y -= Geschwindigkeit

                    #Mutter, oben(Objekt)
                if(Map_x > 360 and Map_x < 405 and Map_y > 275 and Map_y < 290):
                    if(AshDirection == 'Down'):
                        Mutter_oben = True
                    if(Mutter_oben == True and AshDirection != 'Down'):
                        Mutter_oben = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass
                        
                    #Mutter, links(Objekt)
                elif(Map_x > 335 and Map_x < 345 and Map_y > 320 and Map_y < 360):
                    if(AshDirection == 'Right'):
                        Mutter_links = True
                    if(Mutter_links == True and AshDirection != 'Right'):
                        Mutter_links = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                            Ja.destroy()
                            Nein.destroy()
                        except:
                            pass
                        
                    #Mutter, unten(Objekt)
                elif(Map_x > 360 and Map_x < 400 and Map_y > 370 and Map_y < 382):
                    if(AshDirection == 'Up'):
                        Mutter_unten = True
                    if(Mutter_unten == True and AshDirection != 'Up'):
                        Mutter_unten = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass
                        
                    #Pokemon (neben der Mutter auf einem Stuhl)
                        #Von oben
                if(Map_x > 415 and Map_x < 455 and Map_y > 300 and Map_y < 330):
                    Map_y -= Geschwindigkeit
                        #Von rechts
                if(Map_x > 445 and Map_x < 460 and Map_y > 335 and Map_y < 360):
                    Map_x += Geschwindigkeit
                        #Von unten
                elif(Map_x > 415 and Map_x < 455 and Map_y > 350 and Map_y < 370):
                    Map_y += Geschwindigkeit

                    #Pokemon (neben der Mutter auf einem Stuhl)(Objekt)
                        #Von oben
                if(Map_x > 415 and Map_x < 435 and Map_y > 295 and Map_y < 305):
                    if(AshDirection == 'Down'):
                        Pokemon_Mutter = True
                    if(Pokemon_Mutter == True and AshDirection != 'Down'):
                        Pokemon_Mutter = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass
                        
                        #Von rechts
                elif(Map_x > 440 and Map_x < 463 and Map_y > 330 and Map_y < 355):
                    if(AshDirection == 'Left'):
                        Pokemon_Mutter = True
                    if(Pokemon_Mutter == True and AshDirection != 'Left'):
                        Pokemon_Mutter = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass
                        
                        #Von unten
                elif(Map_x > 410 and Map_x < 440 and Map_y > 363 and Map_y < 375):
                    if(AshDirection == 'Up'):
                        Pokemon_Mutter = True
                    if(Pokemon_Mutter == True and AshDirection != 'Up'):
                        Pokemon_Mutter = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                        
            elif Ash_Pos == 'Ash_Haus_Küche':
                #Rand(Unten, links, oben, rechts)

                if(Map_y > 457):
                    Map_y -= Geschwindigkeit
                if(Map_x < 250):
                    Map_x += Geschwindigkeit
                if(Map_y < 175):
                    Map_y += Geschwindigkeit
                if(Map_x > 560):
                    Map_x -= Geschwindigkeit

                #Tür zum Wohnzimmer (Funktion)
                if(Map_x > 240 and Map_x < 252 and Map_y > 370 and Map_y < 385 and AshDirection == 'Left'):
                    Ingame_2()

                    #Pflanze
                if(Map_x > 515 and Map_x < 530 and Map_y > 415 and Map_y < 460):
                    Map_x -= Geschwindigkeit

                elif(Map_x > 520 and Map_x < 600 and Map_y > 395 and Map_y < 405):
                    Map_y -= Geschwindigkeit

                    #Tisch(Unten)
                if(Map_x > 340 and Map_x < 460 and Map_y > 360 and Map_y < 366):
                    Map_y += Geschwindigkeit
                    #Tisch(Rechts)
                elif(Map_x > 455 and Map_x < 465 and Map_y > 280 and Map_y < 360):
                    Map_x += Geschwindigkeit
                    #Tisch(Links)
                elif(Map_x > 340 and Map_x < 345 and Map_y > 264 and Map_y < 350):
                    Map_x -= Geschwindigkeit
                    #Tisch, kante, Schwesterkopf(Oben)
                if(Map_x > 345 and Map_x < 400 and Map_y > 260 and Map_y < 284):
                    Map_y -= Geschwindigkeit
                    #Tisch(Oben)
                elif(Map_x > 380 and Map_x < 460 and Map_y > 270 and Map_y < 275):
                    Map_y -= Geschwindigkeit

                    #Pflanze(oben, links(im raum))
                if(Map_x > 240 and Map_x < 275 and Map_y > 200 and Map_y < 227):
                    Map_y += Geschwindigkeit
                elif(Map_x > 265 and Map_x < 285 and Map_y > 165 and Map_y < 220):
                    Map_x += Geschwindigkeit

                    #Waschbecken
                if(Map_x > 300 and Map_x < 310 and Map_y > 170 and Map_y < 180):
                    Map_x -= Geschwindigkeit
                elif(Map_x > 300 and Map_x < 390 and Map_y > 190 and Map_y < 200):
                    Map_y += Geschwindigkeit
                elif(Map_x > 385 and Map_x < 400 and Map_y > 170 and Map_y < 190):
                    Map_x += Geschwindigkeit

                    #Kühlschrank
                if(Map_x > 405 and Map_x < 415 and Map_y > 170 and Map_y < 190):
                    Map_x -= Geschwindigkeit
                elif(Map_x > 420 and Map_x < 475 and Map_y > 200 and Map_y < 210):
                    Map_y += Geschwindigkeit
                elif(Map_x > 460 and Map_x < 475 and Map_y > 170 and Map_y < 190):
                    Map_x += Geschwindigkeit

                    #Mülleimer
                if(Map_x > 540 and Map_x < 550 and Map_y > 170 and Map_y < 210):
                    Map_x -= Geschwindigkeit
                elif(Map_x > 545 and Map_x < 570 and Map_y > 205 and Map_y < 216):
                    Map_y += Geschwindigkeit

                    #Eine weitere Golduhr(Objekt)
                if(Map_x > 280 and Map_x < 305 and Map_y > 160 and Map_y < 180):
                    if(AshDirection == 'Up'):
                        Gold_Uhr = True
                    if(Gold_Uhr == True and AshDirection != 'Up'):
                        Gold_Uhr = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass
                        
                    #Waschbecken(Objekt)
                if(Map_x > 305 and Map_x < 345 and Map_y > 170 and Map_y < 205):
                    if(AshDirection == 'Up'):
                        Waschbecken = True
                    if(Waschbecken == True and AshDirection != 'Up'):
                        Waschbecken = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    #Herdplatte(Objekt)
                elif(Map_x > 355 and Map_x < 380 and Map_y > 170 and Map_y < 205):
                    if(AshDirection == 'Up'):
                        Herdplatte = True
                    if(Herdplatte == True and AshDirection != 'Up'):
                        Herdplatte = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    #Kühlschrank(Objekt)
                elif(Map_x > 425 and Map_x < 460 and Map_y > 170 and Map_y < 214):
                    if(AshDirection == 'Up'):
                        Kühlschrank = True
                    if(Kühlschrank == True and AshDirection != 'Up'):
                        Kühlschrank = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                            Got_Item.destroy()
                        except:
                            pass

                    #Mülleimer(Objekt)
                if(Map_x > 530 and Map_x < 570 and Map_y > 172 and Map_y < 205):
                    if(AshDirection == 'Right'):
                        Mülleimer = True
                    if(Mülleimer == True and AshDirection != 'Right'):
                        Mülleimer = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass
                        
                elif(Map_x > 540 and Map_x < 570 and Map_y > 200 and Map_y < 220):
                    if(AshDirection == 'Up'):
                        Mülleimer = True
                    if(Mülleimer == True and AshDirection != 'Up'):
                        Mülleimer = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                        except:
                            pass

                    #Küchenbild (Objekt)
                if(Map_x > 510 and Map_x < 545 and Map_y > 165 and Map_y < 190):
                    if(AshDirection == 'Up'):
                        Küchenbild = True
                    if(Küchenbild == True and AshDirection != 'Up'):
                        Küchenbild = False
                        Map_Hit = False
                        try:
                            Aktionsblase.destroy()
                            KÜCHENBILD.destroy()
                        except:
                            pass



    elif begin == False:
        pass

    
    if beginn == True:
        
        def Key_Up(event):
            global Map_x, Map_y, timerUP, AshDirection, Ingame_map, timerDOWN, timerLEFT, timerRIGHT
            timerUP += 1
            timerLEFT = 0
            timerDOWN = 0
            timerRIGHT = 0

            AshDirection = 'Up'
            
            if (timerUP >= Schrittgeschwindigkeit1):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Oben_schritt1, tags = 'Ash')
            if (timerUP >= Schrittgeschwindigkeit2):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Oben_stehen, tags = 'Ash')
            if (timerUP >= Schrittgeschwindigkeit3):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Oben_schritt2, tags = 'Ash')
            if (timerUP >= Schrittgeschwindigkeit4):
                Ingame_map.delete("Ash")
                timerUP = 0
            if(timerUP == 0):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Oben_stehen, tags = 'Ash')

            Alle_Objekte()
            
            Map_y -= Geschwindigkeit
            
        def Key_Down(event):
            global Map_x, Map_y, timerDOWN, AshDirection, Ingame_map, timerLEFT, timerRIGHT, timerUP

            AshDirection = 'Down'

            timerDOWN += 1
            timerUP = 0
            timerLEFT = 0
            timerRIGHT = 0

            if (timerDOWN >= Schrittgeschwindigkeit1):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Unten_schritt1, tags = 'Ash')
            if (timerDOWN >= Schrittgeschwindigkeit2):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Unten_stehen, tags = 'Ash')
            if (timerDOWN >= Schrittgeschwindigkeit3):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Unten_schritt2, tags = 'Ash')
            if (timerDOWN >= Schrittgeschwindigkeit4):
                Ingame_map.delete("Ash")
                timerDOWN = 0
            if(timerDOWN == 0):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Unten_stehen, tags = 'Ash')

            Alle_Objekte()

            Map_y += Geschwindigkeit
          
        def Key_Left(event):
            global Map_x, Map_y, timerLEFT, AshDirection, Ingame_map, timerRIGHT, timerUP, timerDOWN

            AshDirection = 'Left'

            timerDOWN = 0
            timerUP = 0
            timerRIGHT = 0
            timerLEFT += 1

            if (timerLEFT >= Schrittgeschwindigkeit1):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Links_schritt1, tags = 'Ash')
            if (timerLEFT >= Schrittgeschwindigkeit2):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Links_stehen, tags = 'Ash')
            if (timerLEFT >= Schrittgeschwindigkeit3):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Links_schritt2, tags = 'Ash')
            if (timerLEFT >= Schrittgeschwindigkeit4):
                Ingame_map.delete("Ash")
                timerLEFT = 0
            if(timerLEFT == 0):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Links_stehen, tags = 'Ash')

            Alle_Objekte()

            Map_x -= Geschwindigkeit

        def Key_Right(event):
            global Map_x, Map_y, timerRIGHT, AshDirection, Ingame_map, timerUP, timerDOWN, timerLEFT

            AshDirection = 'Right'

            timerDOWN = 0
            timerUP = 0
            timerLEFT = 0
            timerRIGHT += 1

            if (timerRIGHT >= Schrittgeschwindigkeit1):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Rechts_schritt1, tags = 'Ash')
            if (timerRIGHT >= Schrittgeschwindigkeit2):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Rechts_stehen, tags = 'Ash')
            if (timerRIGHT >= Schrittgeschwindigkeit3):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Rechts_schritt2, tags = 'Ash')
            if (timerRIGHT >= Schrittgeschwindigkeit4):
                Ingame_map.delete("Ash")
                timerRIGHT = 0
            if(timerRIGHT == 0):
                Ingame_map.delete("Ash")
                Ingame_map.create_image(Map_x, Map_y, image = Nach_Rechts_stehen, tags = 'Ash')

            Alle_Objekte()

            Map_x += Geschwindigkeit

    elif beginn == False:
        pass




    try:
        Ingame_map.itemconfig('Ash.Haus.Wohnzimmer', image = ingame_map, tags = 'Map')
    except:
        Ingame_map = Canvas(ingame_fenster, width = 800, height = 595)
        Ingame_map.place(x = 0, y = 0)
        Ingame_map.create_image(400,300, image = ingame_map, tags = 'Map') 

    if beginn == True:
        ingame_fenster.bind('<Key-Up>', Key_Up)
        ingame_fenster.bind('<Key-Down>', Key_Down)
        ingame_fenster.bind('<Key-Left>', Key_Left)
        ingame_fenster.bind('<Key-Right>', Key_Right)
    elif beginn == False:
        pass
    
    #Hier wird "Ash" definiert
    if beginn == True:
        Ingame_map.create_image(Map_x, Map_y, image = Nach_Unten_stehen, tags = 'Ash') 
    elif beginn == False:
        pass

    if sprinten == True:
        try:
            sprintlabel.configure(text = 'Sprinten (G), Entsprinten (F)')
        except:
            sprintlabel = Label(ingame_fenster, text = 'Sprinten (G), Entsprinten (F)', font = ('Terminator Two', 10))
            sprintlabel.configure(bg = 'light blue', fg = 'dark blue')
            sprintlabel.place(x = 550, y = 560)

    if beginn == True:
        aktionslabel = Label(ingame_fenster, text = 'Aktion(K)', font = ('Terminator Two', 15))
        aktionslabel.configure(bg = 'light blue', fg = 'dark blue')
        aktionslabel.place(x = 675, y = 560)

        ingame_fenster.bind('<Key-o>', Pos)
        ingame_fenster.bind('<Key-O>', Pos)

        def Ingame_2(): #Wohnzimmer
            global Ingame_map, Alle_Objekte, Map_x, Map_y, AshDirection, Geschwindigkeit, Ash_Pos, beginn
            if beginn == True:
                beginn = False
            elif beginn == False:
                pass

            time.sleep(0.5)

            if Ash_Pos == 'Ash_Haus_Zimmer':
                Map_x = 293
                Map_y = 210
                AshDirection = 'Right'
            elif Ash_Pos == 'Ash_Haus_Küche':
                Map_x = 585
                Map_y = 385
                AshDirection = 'Left'
            Ingame_map.itemconfig('Ash')
                
            if Ash_Pos == 'Ash_Haus_Zimmer':
                Ingame_map.itemconfig('Map', image = ash_haus_wohnzimmer, tags = 'Ash.Haus.Wohnzimmer')
            elif Ash_Pos == 'Ash_Haus_Küche':
                Ingame_map.itemconfig('Ash.Haus.Küche', image = ash_haus_wohnzimmer, tags = 'Ash.Haus.Wohnzimmer')
                
            Ash_Pos = 'Ash_Haus_Wohnzimmer'
        def Ingame3(): #Küche
            global Ingame_map, Alle_Objekte, Map_x, Map_y, AshDirection, Geschwindigkeit, Ash_Pos
            Ash_Pos = 'Ash_Haus_Küche'
            time.sleep(0.5)
            Ingame_map.itemconfig('Ash.Haus.Wohnzimmer', image = ash_haus_küche, tags = 'Ash.Haus.Küche')
            Map_x, Map_y = 250, 380

    elif beginn == False:
        pass
        
        
    Map_Hit = False
def Aktion(event):
    try:
        global AshDirection, Pikachu, Aktionsblase, Map_x, Map_y, Map_Hit, Blume_Item, Wasser, Alle_Items
        global Got_Item, Kühlschrank_Item, Ja, Nein, Küchenbild

        #Ash's Zimmer
        if Ash_Pos == 'Ash_Haus_Zimmer':
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
                    
            elif(Buch == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = '"Das Legendäre Pokemon:\n M......"\nder rest ist verkratzt..')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

        if Ash_Pos == 'Ash_Haus_Wohnzimmer':
            if(Fernseher == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = '*Ein Rauschbild*...\nder Fernseher funktioniert\nnicht richtig..')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass
                
            if(Gold_Uhr == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Eine Golduhr...\ndies ist das Erbe meines Vaters')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Wii == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 15), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Krrrrrr!!!...')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Bücherregal_Secret == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Hier wurde etwas reingeritzt...\nfinde heraus wer es war!')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Bücherregal == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Viele alte Bücher...\n-Ich finde man sollte\nsie wegwerfen-')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Blume == True):
                if Blume_Item == False:
                    if Map_Hit == False:
                            Aktionsblase = Label(fenster, image = aktionsblase,
                                            compound = 'center', font = ('Terminator Two', 15), fg = 'blue', bg = 'black', bd = 0)
                            Aktionsblase.place(x = 175, y = 475)
                            Aktionsblase.configure(text = '*Du hast Wasser gefunden*')
                            Wasser += 1
                            Alle_Items += ['Wasser: '+str(Wasser)]
                            Got_Item = Label(fenster, text = '+1 Wasser', fg = 'white', bg = 'dark green',
                                             font = ('Terminator Two', 20))
                            Got_Item.place(x = 600, y = 20)
                            Map_Hit = True
                            Blume_Item = True
                    elif Map_Hit == True:
                            pass
                        
                elif Blume_Item == True:
                    if Map_Hit == False:
                            Aktionsblase = Label(fenster, image = aktionsblase,
                                            compound = 'center', font = ('Terminator Two', 15), fg = 'black', bg = 'black', bd = 0)
                            Aktionsblase.place(x = 175, y = 475)
                            Aktionsblase.configure(text = 'Die Blumen sind frisch.')
                            Map_Hit = True
                    elif Map_Hit == True:
                            pass
                        
            elif(Mutter_oben == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Bitte geh mir aus dem Bild '+str(name)+'!\nIch versuche den Fernseher\nzum laufen zu bringen!')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass
                
            elif(Mutter_links == True):
                if Map_Hit == False:
                    if not "Mutter" in Mission:
                        Aktionsblase = Label(fenster, image = aktionsblase,
                                        compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                        Aktionsblase.place(x = 175, y = 475)
                        Aktionsblase.configure(text = str(name)+', findest du bitte für mich heraus\n was deine Schwester getan hat?\nsie ist so komisch...')
                        Ja = Button(fenster, text = 'Ja', font = ('Terminator Two', 20), fg = 'black', bg = 'light grey', bd = 0, command = Ja_command)
                        Ja.place(x = 300, y = 550)
                        Nein = Button(fenster, text = 'Nein', font = ('Terminator Two', 20), fg = 'black', bg = 'light grey', bd = 0, command = Nein_command)
                        Nein.place(x = 400, y = 550)
                        Map_Hit = True
                    elif "Mutter" in Mission:
                        Aktionsblase = Label(fenster, image = aktionsblase,
                                        compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                        Aktionsblase.place(x = 175, y = 475)
                        Aktionsblase.configure(text = str(name)+', danke für deine Hilfe!')
                        Map_Hit = True
                elif Map_Hit == True:
                    pass
                
            elif(Mutter_unten == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = str(name)+'\nich möchte nicht\nvon hinten angesprochen werden!')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Pokemon_Mutter == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Pumelulululuff!!')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

                
        if Ash_Pos == 'Ash_Haus_Küche':
            
            if(Gold_Uhr == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Eine Golduhr...\ndies ist das Erbe meiner Großmutter')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Waschbecken == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = '-Grrrrr!!!\nnichts funktioniert hier...\nnichtmal das Waschbecken!!!-')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Herdplatte == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = '*Ein kleines flämchen,\ngibt ein hauch wärme von sich.*')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Kühlschrank == True):
                if Kühlschrank_Item == False:
                    if Map_Hit == False:
                            Aktionsblase = Label(fenster, image = aktionsblase,
                                            compound = 'center', font = ('Terminator Two', 15), fg = 'blue', bg = 'black', bd = 0)
                            Aktionsblase.place(x = 175, y = 475)
                            Aktionsblase.configure(text = '*Du hast Wasser gefunden*')
                            Wasser += 1
                            Alle_Items += ['Wasser: '+str(Wasser)]
                            Got_Item = Label(fenster, text = '+1 Wasser', fg = 'white', bg = 'dark green',
                                             font = ('Terminator Two', 20))
                            Got_Item.place(x = 600, y = 20)
                            Map_Hit = True
                            Kühlschrank_Item = True
                    elif Map_Hit == True:
                            pass
                        
                elif Kühlschrank_Item == True:
                    if Map_Hit == False:
                            Aktionsblase = Label(fenster, image = aktionsblase,
                                            compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                            Aktionsblase.place(x = 175, y = 475)
                            Aktionsblase.configure(text = 'Ein Kühlschrank, wo ab und zu etwas\ndrinn steht...')
                            Map_Hit = True
                    elif Map_Hit == True:
                            pass

            elif(Mülleimer == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Dieser Papierkorb ist leer.')
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

            elif(Küchenbild == True):
                if Map_Hit == False:
                    Aktionsblase = Label(fenster, image = aktionsblase,
                                    compound = 'center', font = ('Terminator Two', 10), fg = 'black', bg = 'black', bd = 0)
                    Aktionsblase.place(x = 175, y = 475)
                    Aktionsblase.configure(text = 'Ich habe es gemalt\nals ich klein war...')
                    KÜCHENBILD = Label(fenster, image = Küchen_Bild, bd = 0)
                    KÜCHENBILD.place(x = 350, y = 350)
                    Map_Hit = True
                elif Map_Hit == True:
                    pass

        


        else:
            pass




    except:
        print('Die Taste "K" kann nur im Spiel\nverwendet werden!')
                


def Ja_command():
    global Aktionsblasen, Ja, Nein, Mission
    
    if Mutter_links == True:
        Mission += ['Mutter']
        Aktionsblase.configure(text = 'Ich bin dir sehr dankbar!')
        Ja.destroy()
        Nein.destroy()
        
                


def Nein_command():
    global Aktionsblasen, Ja, Nein, Mission

    if Mutter_links == True:
        Aktionsblase.configure(text = str(name)+', du bist faul!')
        Ja.destroy()
        Nein.destroy()


def Pause(event):
    pass
                
fenster.bind('<Key-k>', Aktion)
fenster.bind('<Key-K>', Aktion)
fenster.bind('<Key-Escape>', Pause)


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
        print('-'*30)
        print('Map_x = {}, Map_y = {}'.format(Map_x, Map_y))
        print('-'*30)

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
