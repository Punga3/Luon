import random
from core import *
d = 0
for i in range(0,10000):
    personD = Person("D",10,2,10,2,weaponDagger)
    personS = Person("S",10,2,10,-2,weaponSword)
    while (not personD.isDead()) and (not personS.isDead()):
        personD.hit(personS)
        personS.hit(personD)
    if personS.isDead():
        d+=1
print("Dex: "+str(d))
print("Str: "+str(10000-d))
