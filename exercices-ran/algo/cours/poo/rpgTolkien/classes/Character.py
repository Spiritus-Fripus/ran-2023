import random



class Character :
    
    def __init__(self, pseudo:str) -> None:
        self.pseudo = pseudo
        self.health = 100
        self.mana = None
        self.strength = None
        self.stamina = 100
        self.defense = None 
        self.speed = None 
        self.level = 1 
        self.attacks = []

    def level_up(self, Level : int = None) -> None:
        if Level:
            self.level = Level
        else: 
            self.level + 1

    def attack(self, character) -> None:
        print() 
        if self.health > 0:
            if character.health > 0 :
                print(f"--- {self.pseudo} attaque {character.pseudo} ---")
                attack = random.choice(self.attacks)
                total_damage = round(((attack.damage + (0.5 * self.level)) * (1 + self.strength / 100) * (1- character.defense/100)), 2) 
                character.health -= total_damage      
                self.stamina = self.stamina * (1 -attack.damage / 10)
                print()
                
                if character.health > 0 :
                    print(f"{self.pseudo} inflige {total_damage} de dégats à {character.pseudo} avec l'attaque {attack.name} !")
                    print(f"Il reste {character.health} points de vie à {character.pseudo}") 
                else:
                    print(f"{character.pseudo} est décédé")
            else: 
                print(f"Impossible d'attaquer {character.pseudo} il est mort")