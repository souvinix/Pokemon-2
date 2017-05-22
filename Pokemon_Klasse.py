#Pokemons

class Pokemon(object):
    PRESENT_POKEMONS = 0
    def __init__(self, name, leben, present_ep, mind_ep, max_ep, statuswert, present_level,
                 mind_level, max_level, element):
        self.name = name
        self.leben = leben
        self.present_ep = present_ep
        self.mind_ep = mind_ep
        self.max_ep = max_ep
        self.statuswert = statuswert
        self.present_level = present_level
        self.mind_level = mind_level
        self.max_level = max_level
        self.element = element

        Pokemon.PRESENT_POKEMONS += 1
        print('Das Pokemon: '+self.name+' wurde\nerfolgreich generiert!')


    def __del__(self):
        Pokemon.PRESENT_POKEMONS -= 1
        print('Pokemon: '+self.name+' wurde gelöscht!')

    def angreifen(self, schaden, ziel):
        if self.schaden > ziel.max_leben:
            ziel.present_leben = 0
        else:
            ziel.present_leben -= self.schaden
        

#leben, present_ep, mind_ep, max_ep, statuswert, present_level, mind_level, max_level, element
Schiggy = Pokemon("Schiggy", 25, 0, 1, 30, "Normal", 5, 1, 100, "Wasser")
Glumanda = Pokemon("Glumanda", 20, 0, 1, 45, "Normal", 5, 1, 100, "Feuer")
Bisasam = Pokemon("Bisasam", 20, 0, 1, 25, "Normal", 5, 1, 100, "Blatt")
