import math
class Player:
    def __init__(self,pos):
        self.pos=pos
        self.health=100
        self.hasWeapon=False

    def move(self,direction):
        pos = [self.pos[0],self.pos[1]]
        if(direction=='up'):
            pos[1]-=1
        elif(direction=='down'):
            pos[1]+=1
        elif(direction=='left'):
            pos[0]-=1
        elif(direction=='right'):
            pos[0]+=1
        self.pos= (pos[0],pos[1])
    
    