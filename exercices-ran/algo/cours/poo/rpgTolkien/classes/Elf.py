from classes.Attack import Attack
from classes.Character import Character


class Elf(Character):
    
    def __init__(self, pseudo: str) -> None:
        super().__init__(pseudo)       
        self.strength = 5
        self.mana = 100
        self.defense = 5
        self.speed = 7
        self.attacks = [
            Attack("Gifle",2),
            Attack("Coup d'épée", 5),
            Attack("Tir de flèche", 4),
            Attack("Boule de feu", 7)
        ]