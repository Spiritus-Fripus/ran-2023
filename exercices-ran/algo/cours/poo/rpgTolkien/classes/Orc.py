from classes.Attack import Attack
from classes.Character import Character


class Orc(Character):
    
    def __init__(self, pseudo: str) -> None:
        super().__init__(pseudo)       
        self.strength = 7
        self.mana = 0
        self.defense = 8
        self.speed = 3
        self.attacks = [
            Attack("Coup de poing",2),
            Attack("Coup de masse", 4),
            Attack("Coup de hache", 6),
            Attack("Descente du coude", 8)
        ]




        