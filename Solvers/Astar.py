import copy,time,math
class Ast:
    def __init__(self,game):
        self.game=game
        self.board= copy.deepcopy(self.game.grid)
        
    def HeuristicFunction(self,point,goalPoint):
        return math.sqrt((point[0]-goalPoint[0])**2 + (point[1]-goalPoint[1])**2)

    def setHeuristics(self,hFunction,goalPoint):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.table[i][j][2]=hFunction((i,j),goalPoint)


    def solve(self):
        
        startPos = self.game.player.pos
        goalPoint=self.game.weapon
        print(goalPoint)
        self.table=[[[[''],100000000,-1] for _ in range(len(self.board[0]))] for _ in range(len(self.board))]
        self.table[startPos[0]][startPos[1]] = [[''],0,-1]
        self.setHeuristics(self.HeuristicFunction,goalPoint)

        self.astar(startPos)
        solToGoal = self.table[goalPoint[0]][goalPoint[1]][0]
        print(solToGoal)
       
        startPos = self.game.weapon
        self.game.player.hasWeapon=True
        for monster in self.game.monsters:
            print(startPos,'to',monster)
            goalPoint=monster
            self.table=[[[[''],10000,-1] for _ in range(len(self.board[0]))] for _ in range(len(self.board))]
            self.table[startPos[0]][startPos[1]] = [[''],0,-1]
            self.setHeuristics(self.HeuristicFunction,goalPoint)
            self.astar(startPos)
            solToMonster = self.table[goalPoint[0]][goalPoint[1]][0]
            solToGoal+=solToMonster
            startPos=monster
        
        self.game.player.hasWeapon=False
        self.game.step()
        for direction in solToGoal:
            time.sleep(0.1)
            self.game.validPlayerMove(self.game.player.pos,direction)
            self.game.player.move(direction)
            self.game.step()
        

    
    def astar(self,startPos):
        print('A*',startPos)
        queue = [startPos]
        possible_moves=['up','down','left','right']
        while queue:
            self.sortQueue(queue)
            # print(queue)
            pos= queue.pop(0)
            if(self.table[pos[0]][pos[1]][2]==0):
                return 
            path = self.table[pos[0]][pos[1]][0]
            cost = self.table[pos[0]][pos[1]][1]
            for move in possible_moves:
                if(self.game.validMove(pos,move)):
                    newPath = path+[move]
                    newCost = cost+1
                    newPos=self.game.getPosFromPath(newPath,startPos)
                    oldCost = self.table[newPos[0]][newPos[1]][1]
                    heuristic= self.table[newPos[0]][newPos[1]][2]
                    if(newCost<oldCost):
                        self.table[newPos[0]][newPos[1]]=[newPath,newCost,heuristic]
                        queue.append(newPos)

                    
                    

    def sortQueue(self,queue):
        self.quick_sort(queue,0,len(queue)-1)

    def partition(self,array, start, end):
        pivot = array[start]
        pivot = self.table[pivot[0]][pivot[1]][1]+self.table[pivot[0]][pivot[1]][2]
        low = start + 1
        high = end

        while True:
            check=array[high]
            check= self.table[check[0]][check[1]][1]+self.table[check[0]][check[1]][2]
            while low <= high and check >= pivot:
                high = high - 1

            check2=array[low]
            check2= self.table[check2[0]][check2[1]][1]+self.table[check2[0]][check2[1]][2]
            while low <= high and check2 <= pivot:
                low = low + 1

            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        return high

    def quick_sort(self,array, start, end):
        if start >= end:
            return
        p = self.partition(array, start, end)
        self.quick_sort(array, start, p-1)
        self.quick_sort(array, p+1, end)

        
        
