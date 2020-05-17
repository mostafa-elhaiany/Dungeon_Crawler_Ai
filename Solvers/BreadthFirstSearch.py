import copy,time

class BFS:
    
    def __init__(self,game):
        self.game=game
        self.board = copy.deepcopy(self.game.grid)
        self.num_rows=len(self.game.grid)
        self.num_cols=len(self.game.grid[0])   
         
    def solve(self):
        playerStartingPos=self.game.player.pos
        self.game.displayGrid()
        print('starting to solve')
        sol=[""]
        sol=self.shortestPath(sol,self.game.weapon)
        self.game.player.hasWeapon=True
        for monster in self.game.monsters:
            sol =self.shortestPath(sol,monster)

        self.game.player.hasWeapon=False
        for direction in sol:
            self.game.step()
            time.sleep(0.2)
            self.game.validPlayerMove(self.game.player.pos,direction)
            self.game.player.move(direction)


        
    def shortestPath(self,path, goal):
        possible_moves=['up','down','left','right']
        queue=[path]
        while not self.game.isPathToGoal(path,goal):
            if(queue):
                path = queue.pop(0)
                for move in possible_moves:
                    pos = self.game.getPosFromPath(path)
                    if(self.game.validMove(pos,move)):
                        newPath = path+[move]
                        queue.append(newPath)
        return path