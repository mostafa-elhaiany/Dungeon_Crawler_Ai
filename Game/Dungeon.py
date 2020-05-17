import pygame, sys
import random as rn
import math
import copy
from Game.settings import *
from Game.Player import *

class Dungeon:
    def __init__(self,board=None):
        pygame.init()
        self.window=pygame.display.set_mode((WIDTH,HEIGHT))
        self.font = pygame.font.SysFont('arial',int(cell_size//2))
        self.running = True
        print('loading board!!')
        self.selected = None
        self.mouse_pos = None
        self.number=None
        self.finished=False
        self.obstacles=[]
        self.monsters=[]
        self.weapon=None
        self.player=None
        if(not board):
            self.state='building'
            self.grid=[['E' for _ in range(COLS)]for _ in range(ROWS)]
        else:
            self.state='playing'
            self.grid=board
            self.loadBoardData()
        print("done loading, let's play!")
        print(self.player)
    

# main functions

    def start_new_game(self,board=None):
        self.running = True
        print('loading board!!')
        self.selected = None
        self.mouse_pos = None
        self.number=None
        self.finished=False
        self.obstacles=[]
        self.monsters=[]
        self.weapon=None
        self.player=None
        if(not board):
            self.state='building'
            self.grid=[['E' for _ in range(COLS)]for _ in range(ROWS)]
        else:
            self.state='playing'
            self.grid=board
            self.loadBoardData()

    def loadBoardData(self):
        for rIdx,r in enumerate(self.grid):
            for cIdx,c in enumerate(r):
                pos=(rIdx,cIdx)
                if(c=='w' or c=='W'):
                    self.weapon=pos
                elif(c=='p' or c=='P'):
                    self.player=Player(pos)
                elif(c=='m' or c=='M'):
                    self.monsters.append(pos)
                elif(c=='o' or c=='O'):
                    self.obstacles.append(pos)
        if(not self.player):
            raise Exception('board must have a player')
        if(not self.weapon):
            raise Exception('board must have a weapon')
        if(len(self.obstacles)==0):
            raise Exception('board must have obstacles')
        if(len(self.monsters)==0):
            raise Exception('board must have monsters')

        print('board loaded to game')
    
    def start_new_game(self,board=None):
        self.window=pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True
        print('loading board!!')
        self.selected = None
        self.mouse_pos = None
        self.number=None
        self.finished=False
        if(not board):
            self.state='building'
            self.grid=[[0 for _ in range(COLS)]for _ in range(ROWS)]
        else:
            self.state='playing'
            self.grid=board
            self.loadBoardData()

        self.obstacles=[]
        self.monsters=[]
        self.weapon=None
        self.player=None



    #main loop of the game
    def run(self):
        while self.running:
            self.events(self.state)
            self.update(self.state)
            self.draw(self.state)
        pygame.quit()
        sys.exit()

    def build(self):
        while(self.state=='building'):
            self.step()

    #1 step of the game for the Ai
    def step(self):
        self.events(self.state)
        self.update(self.state)
        self.draw(self.state)

    #main draw function
    def draw(self,state):
        self.window.fill(WHITE)
            
        if self.selected:
            self.drawSelection(self.window,self.selected)

        if(self.weapon):
            self.shadeCells(self.window,[self.weapon],YELLOW)
        if(self.player):
            self.shadeCells(self.window,[self.player.pos],GREEN)
        self.shadeCells(self.window,self.obstacles,GRAY)
        self.shadeCells(self.window,self.monsters,RED)

        
            

        self.drawGrid(self.window)

        self.textToScreen(self.window,self.state, (WIDTH//2,1), colour=BLACK)
        if(self.state=='playing'):
            self.textToScreen(self.window,"health", (10,20), colour=BLACK)
            pygame.draw.rect(self.window,RED,(15,50,self.player.health,5))
        elif(self.state=='won' or self.state=='dead' ):
            self.textToScreen(self.window,"press space to play again", (WIDTH//2,50), colour=BLACK)
    


        pygame.display.update()

    #updates the game with the mouse position
    def update(self,state):
        self.mouse_pos= pygame.mouse.get_pos()
        self.grid=[["E" for _ in range(ROWS)]for _ in range(COLS)]
        for pos in self.monsters:
            self.grid[pos[0]][pos[1]]='M'
        for pos in self.obstacles:
            self.grid[pos[0]][pos[1]]='O'
        if(self.player):
            pos=self.player.pos
            self.grid[pos[0]][pos[1]]='P'
        if(self.weapon):
            pos=self.weapon
            self.grid[pos[0]][pos[1]]='W'
        if(self.state=='playing'):
            if(self.player.health<=0):
                self.state='dead'

    #handles all kinds of ingame events
    def events(self,state):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                self.running=False
                pygame.quit()
                sys.exit()
            if(self.state=='playing'):
                self.handlePlayingEvents(event)
            elif(self.state=='building'):
                self.handleBuildingEvents(event)
            elif(self.state=='dead' or self.state=='won'):
                self.handleGameOverEvents(event)
    

#events helper Functions

    def handlePlayingEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected= self.handleMouseSelection()
            if(selected):
                self.selected=selected
            else:
                self.selected=None
        if event.type == pygame.KEYDOWN:
            if(event.unicode=='w' or event.unicode=='W'):
                if(self.validPlayerMove(self.player.pos,'up')):
                    self.player.move('up')
            elif(event.unicode=='s' or event.unicode=='S'):
                if(self.validPlayerMove(self.player.pos,'down')):
                    self.player.move('down')
            elif(event.unicode=='a' or event.unicode=='A'):
                if(self.validPlayerMove(self.player.pos,'left')):
                    self.player.move('left')
            elif(event.unicode=='d' or event.unicode=='d'):
                if(self.validPlayerMove(self.player.pos,'right')):
                    self.player.move('right')
            
    def handleBuildingEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected= self.handleMouseSelection()
            if(selected):
                self.selected=selected
            else:
                self.selected=None
        elif event.type == pygame.KEYDOWN:
            if(self.selected):
                #obstacle handling
                if(event.unicode=='o' or event.unicode=='O'):
                    if(self.selected in self.monsters):
                        print('can\'t choose this point, remove the monster to add something here!')
                        return
                    if(self.player):
                        if(self.player.pos == self.selected):
                            print('can\'t choose this point, change the player pos to add something here!')
                            return
                    if(self.weapon):
                        if(self.weapon == self.selected):
                            print('can\'t choose this point, change the weapon pos to add something here!')
                            return
                    if(self.selected not in self.obstacles):
                        print('added as obstacle')
                        self.obstacles.append(self.selected)
                    else:
                        print('removed from obstacles')
                        self.obstacles.remove(self.selected)             
                #weapon handling
                if(event.unicode=='w' or event.unicode=='W'):
                    if(self.selected in self.monsters):
                        print('can\'t choose this point, remove the monster to add something here!')
                        return
                    if(self.selected in self.obstacles):
                        print('can\'t choose this point, remove the obstacle to add something here!')
                        return
                    if(self.player):
                        if(self.player.pos == self.selected):
                            print('can\'t choose this point, change the player pos to add something here!')
                            return
                    if(not self.weapon):
                        self.weapon=self.selected
                        print('added weapon')
                    else:
                        if(self.weapon == self.selected):
                            print('removed weapon')
                            self.weapon=None
                        else:
                            print('changed weapon pos')
                            self.weapon=self.selected
                #monster handling
                if(event.unicode=='m' or event.unicode=='M'):
                    if(self.selected in self.obstacles):
                        print('can\'t choose this point, remove the obstacle to add something here!')
                        return
                    if(self.player):
                        if(self.player.pos == self.selected):
                            print('can\'t choose this point, change the player pos to add something here!')
                            return
                    if(self.weapon):
                        if(self.weapon == self.selected):
                            print('can\'t choose this point, change the weapon pos to add something here!')
                            return
                    if(self.selected not in self.monsters):
                        print('added as monster')
                        self.monsters.append(self.selected)
                    else:
                        print('removed from monsters')
                        self.monsters.remove(self.selected)
                #player handling
                if(event.unicode=='p' or event.unicode=='P'):
                    if(self.selected in self.obstacles):
                        print('can\'t choose this point, remove the obstacle to add something here!')
                        return
                    if(self.selected in self.monsters):
                            print('can\'t choose this point, remove the monster to add something here!')
                            return
                    if(self.weapon):
                        if(self.weapon == self.selected):
                            print('can\'t choose this point, change the weapon pos to add something here!')
                            return
                    if(self.player):
                        if(self.selected == self.player.pos):
                            self.player=None
                            print('removed player!')
                        else:
                            self.player=Player(self.selected)
                            print('changed player pos!')    
                    else:
                        self.player=Player(self.selected)
           #handling state change
            if(event.unicode==' '):
                if(not self.player):
                    print('please add a player to the field!')
                    return
                if(not self.weapon):
                    print('please add a weapon to the field')
                    return
                if(len(self.monsters)==0):
                    print('please add at least one monster')
                    return
                if(len(self.obstacles)==0):
                    print('please add at least one obstacle')
                    return
                print('done building')
                self.state='playing'
                self.displayGrid()

    def handleGameOverEvents(self,event):
        if event.type == pygame.KEYDOWN:
            if(event.unicode==' '):
                self.start_new_game()

    def handleMouseSelection(self):
        x_in_grid= grid_pos[0] <self.mouse_pos[0]< grid_pos[2]+grid_pos[0]
        y_in_grid= grid_pos[1] <self.mouse_pos[1]< grid_pos[3]+grid_pos[1]
        if( x_in_grid and y_in_grid):
            return ((self.mouse_pos[0]-grid_pos[0])//cell_size,(self.mouse_pos[1]-grid_pos[1])//cell_size)
        return False

    #player movement helper functions
    def validPlayerMove(self,position,direction):
        pos = [position[0],position[1]]

        if(direction=='up'):
            pos[1]-=1
        elif(direction=='down'):
            pos[1]+=1
        elif(direction=='left'):
            pos[0]-=1
        elif(direction=='right'):
            pos[0]+=1

        pos= (pos[0],pos[1])
        if((pos[0]<0 or pos[0]>=len(self.grid)) or (pos[1]<0 or pos[1]>=len(self.grid[0])) ):
            # print('invalid move! out of bounds')
            return False

        if(pos in self.obstacles):
            # print('invalid move! obstacle here')
            self.player.health/=2
            # print('you lost health')
            if(self.player.health<=1):
                self.player.health = 0
                # print('you died')
                self.finished=True
            return False
        if(pos in self.monsters):
            if(self.player.hasWeapon):
                # print('nice you killed a monster!')
                self.monsters.remove(pos)
                if(len(self.monsters)==0):
                    # print('you killed all monsters you won the game!!')
                    self.finished=True
                    self.state="won"
                return True
            else:
                # print('invalid move! monster here')
                self.player.health = 0
                # print('you died')
                self.finished=True
                # self.running=False
                return False
        if(pos==self.weapon):
            # print('nice move! weapon here')
            self.player.health = 100
            self.player.hasWeapon=True
            self.weapon=None
        return True
        
    #player movement helper functions
    def validMove(self,position,direction):
        pos = [position[0],position[1]]

        if(direction=='up'):
            pos[1]-=1
        elif(direction=='down'):
            pos[1]+=1
        elif(direction=='left'):
            pos[0]-=1
        elif(direction=='right'):
            pos[0]+=1

        pos= (pos[0],pos[1])
        if((pos[0]<0 or pos[0]>=len(self.grid)) or (pos[1]<0 or pos[1]>=len(self.grid[0])) ):
            return False
        if(pos in self.obstacles):
            return False
        if(pos in self.monsters):
            if(self.player.hasWeapon):
                if(len(self.monsters)==0):
                    print('game won!')
                return True
            else:
                return False
        if(pos==self.weapon):
            return True
        return True
#drawing helper functions

    #draws the sudoku grid
    def drawGrid(self,window):
        pygame.draw.rect(window,BLACK,grid_pos,2)
        for c in range(COLS):
            start_x=grid_pos[0]+(c*cell_size)
            start_y= grid_pos[1]
            end_x=grid_pos[0]+(c*cell_size)
            end_y= grid_pos[1]+grid_pos[3]
            pygame.draw.line(window, BLACK,(start_x,start_y),(end_x,end_y),2)
            for r in range(ROWS):
                start_x=grid_pos[0]
                start_y= grid_pos[1]+(r*cell_size)
                end_x=grid_pos[0]+grid_pos[2]
                end_y= grid_pos[1]+(r*cell_size)
                pygame.draw.line(window, BLACK,(start_x,start_y),(end_x,end_y),2)
                        

    #draws the blue box showing the selected cell
    def drawSelection(self,window,pos):
        margin = 3
        pygame.draw.rect(window,BLUE,(pos[0]*cell_size + grid_pos[0],pos[1]*cell_size+ grid_pos[1],cell_size+margin,cell_size+margin))

    #adds the numbers inside their prober cells
    def drawNumbers(self,window):
        margin = 10
        for rIdx,row in enumerate(self.grid):
            for cIdx,col in enumerate(row):
                if col != 0:
                    self.textToScreen(window,str(col),(rIdx*cell_size + grid_pos[0]+ margin,cIdx*cell_size+ grid_pos[1]+ margin))

    #adds text to the GUI
    def textToScreen(self,window,text, pos, colour=BLACK):
        font = self.font.render(text,False,colour)
        window.blit(font,pos)


    #adds a shade to cells
    def shadeCells(self,window,cells,colour):
        margin=3
        for cell in cells:
            pygame.draw.rect(window,colour,(cell[0]*cell_size + grid_pos[0],cell[1]*cell_size+ grid_pos[1],cell_size+margin,cell_size+margin))

#general helpers

    # proper printing function
    def displayGrid(self):
        for row in self.grid:
            for col in row:
                print(f"{col}, ",end='')
            print()

    def isPathToGoal(self,path,goalPos):
        aPlayer=Player(self.player.pos)
        for direction in path:
            aPlayer.move(direction)
        print(aPlayer.pos,goalPos)
        if(aPlayer.pos==goalPos):
            return True
        # print(aPlayer.pos,goalPos)
        return False

    def getPosFromPath(self,path):
        aPlayer=Player(self.player.pos)
        for direction in path:
            aPlayer.move(direction)
        return aPlayer.pos
        