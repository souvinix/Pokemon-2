#Alle Pokemons

class Pokemon (object):
    def __init__(self, name, mind_hp, max_hp, present_hp, present_level,
                 max_level, element, attacken, atk):
        
        self.name = name
        self.mind_hp = mind_hp
        self.max_hp = max_hp
        self.present_hp = present_hp
        self.present_level = present_level
        self.max_level = max_level
        self.element = element
        self.attacken = attacken
        self.atk = atk
    

    def angreifen (self, ziel, damage):
        ziel.present_hp -= damage

Glumanda = Pokemon("Glumanda", 1, 20, 20, 1, 100, "Feuer", ["Glut", "Schlitzer", "Ultrablaster", "ZZZ"], 5)
Schiggy = Pokemon("Schiggy", 1, 20, 20, 1, 100, "Wasser", ["lol", "a","s","d"], 7)


    
        
        
        
