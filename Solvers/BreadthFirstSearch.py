import copy,time

class BFS:
    
    def __init__(self,game):
        self.game=game
        self.board = copy.deepcopy(self.game.grid)
        self.num_rows=len(self.game.grid)
        self.num_cols=len(self.game.grid[0])   
         
    def solve(self):
        playerStartingPos=self.game.player.pos
        queue=[[""]]
        sol=[""]
        possible_moves=['up','down','left','right']
        self.game.displayGrid()
        print('starting to solve')

        while not self.game.isPathToGoal(sol,self.game.weapon):
            if(queue):
                sol = queue.pop(0)
                for move in possible_moves:
                    pos = self.game.getPosFromPath(sol)
                    if(self.game.validMove(pos,move)):
                        new_sol = sol+[move]
                        print(new_sol)
                        queue.append(new_sol)
        
        print(sol)
        self.game.player.hasWeapon=True
        for monster in self.game.monsters:
            queue=[sol]
            print(sol)
            while not self.game.isPathToGoal(sol,monster):
                if(queue):
                    sol = queue.pop(0)
                    for move in possible_moves:
                        pos = self.game.getPosFromPath(sol)
                        if(self.game.validMove(pos,move)):
                            new_sol = sol+[move]
                            print(new_sol)
                            queue.append(new_sol)
        
        print(sol)
        # self.game.start_new_game(self.board)
        self.game.player.hasWeapon=False
        # self.game.displayGrid()
        for direction in sol:
            self.game.step()
            time.sleep(0.2)
            self.game.validPlayerMove(self.game.player.pos,direction)
            self.game.player.move(direction)


        
    