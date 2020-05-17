from Game.Dungeon import *
from Game.settings import *
from Solvers.BreadthFirstSearch import *
from Solvers.Dijkstra import *
game= Dungeon(test_board)
# game.build()
agent=BFS(game)
# agent=Dkstra(game)

agent.solve()
# game.run()

