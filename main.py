from Game.Dungeon import *
from Game.settings import *
from Solvers.BreadthFirstSearch import *
o='o'
p='p'
w='w'
m='m'
e='e'

small_test_board=[
    [o,o,o,o],
    [o,p,e,m],
    [e,e,e,o],
    [e,e,e,o],
    [e,e,o,o],
    [e,e,w,m],
]

small_test_board2=[
    [O, P, O, M, 0, 0, 0, 0, 0, O],
    [O, 0, O, 0, 0, 0, 0, O, M, O],
    [O, 0, 0, O, O, 0, 0, O, 0, O],
    [O, 0, 0, 0, O, 0, 0, O, 0, O],
    [O, 0, 0, O, 0, 0, O, O, 0, O],
    [O, 0, 0, 0, 0, 0, O, 0, 0, O],
    [O, 0, 0, 0, 0, 0, O, 0, 0, O],
    [O, 0, O, W, O, 0, 0, 0, 0, O],
    [O, O, O, O, O, O, O, O, O, O],
]
game= Dungeon()
game.build()
bfs=BFS(game)
bfs.solve()

# game.run()

