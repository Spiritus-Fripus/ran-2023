from os import system
from time import sleep
from classes.Elf import Elf
from classes.Orc import Orc


orc = Orc("Didier")
elf = Elf("Dobby")
elf.level_up(10)

while orc.health > 0 and elf.health > 0:
    orc.attack(elf)
    elf.attack(orc)
    sleep(1)
    system("cls")