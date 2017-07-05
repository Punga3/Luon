import random
def D(num):
    return random.randrange(1,num+1)
def weaponSword(str,dex):
    return D(4)+D(4)+(str//2)
def weaponDagger(str,dex):
    return D(4)+(dex//2)
class Person:
    def __init__(self,name,strspi,strspin,dexrob,dexrobn,weapon):
        self.name=name
        self.strspi=strspi
        self.strspin=strspin
        self.dexrob=dexrob
        self.dexrobn=dexrobn
        self.weapon=weapon
        self.hp=self.getMaxHp()
    def getStr(self):
        return int(self.strspi * ((5+self.strspin)/10))
    def getSpi(self):
        return int(self.strspi * ((5-self.strspin)/10))
    def getDex(self):
        return int(self.dexrob * ((5-self.dexrobn)/10))
    def getRob(self):
        return int(self.dexrob * ((5+self.dexrobn)/10))
    def getDodge(self):
        if self.getDex() in range(0,11):
            return self.getDex()//2
        if self.getDex() in range(11,21):
            return 5+((self.getDex()-10)//2)
        if self.getDex() in range(21,31):
            return 10+((self.getDex()-20)//5)
        if self.getDex() in range(31,41):
            return 17+((self.getDex()-30)//10)
        if self.getDex() in range(41,61):
            return 18+((self.getDex()-40)//20)
    def getAtk(self):
        return self.weapon(self.getStr(),self.getDex())
    def isDead(self):
        return self.hp<=0
    def hit(self,other,mod=0):
        if other.getDodge() < D(20)+mod:
            other.hp -= self.getAtk()
    def vHit(self,other,mod=0):
        if other.getDodge() < D(20)+mod:
            other.hp -= self.getAtk()
            print(self.name+" ("+str(self.hp)+") hitted "+other.name+" ("+str(other.hp)+")")
        else:
            print(self.name+" ("+str(self.hp)+") missed "+other.name+" ("+str(other.hp)+")")
    def getMaxHp(self):
        hp = 5
        for r in range(0,self.getRob()+1):
            #if r in range(1,11):
            #    hp+=2
            #elif r in range(11,21):
            #    hp+=4
            #elif r in range(21,31):
            #    hp+=6
            #elif r in range(31,41):
            #    hp+=8
            #elif r in range(41,61):
            #    hp+=10
            #else:
            #    hp+=20
            hp+=2
        return hp

