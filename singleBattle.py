from core import *
personD = Person("S",10,2,10,2,weaponSword)
personS = Person("D",10,2,10,-2,weaponDagger)
i=0
while (not personD.isDead()) and (not personS.isDead()):
    i+=1
    personD.vHit(personS,-2)
    personS.vHit(personD)
print(str(i))
