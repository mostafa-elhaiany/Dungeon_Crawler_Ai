WIDTH = 800
HEIGHT= 600

#colours
WHITE=(255,255,255)
BLACK=(0,0,0)

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
GRAY=(190,190,190)
YELLOW=(255,255,0)

#boards
ROWS=10
COLS=15
O='o'
P='p'
W='w'
M='m'
test_board=[
    [O, P, O, M, 0, 0, 0, 0, 0, O],
    [O, 0, O, 0, 0, 0, 0, O, O, O],
    [O, 0, O, 0, 0, 0, 0, O, M, O],
    [O, 0, 0, O, O, 0, 0, O, 0, O],
    [O, 0, 0, 0, O, 0, 0, O, 0, O],
    [O, 0, 0, O, 0, 0, O, O, 0, O],
    [O, 0, 0, 0, 0, 0, O, 0, 0, O],
    [O, 0, 0, 0, 0, 0, O, 0, 0, O],
    [O, 0, 0, 0, 0, 0, O, O, 0, O],
    [O, 0, O, O, O, 0, 0, 0, 0, O],
    [O, 0, O, W, O, 0, 0, 0, 0, O],
    [O, 0, 0, 0, O, 0, 0, 0, 0, O],
    [O, 0, 0, 0, O, 0, 0, 0, 0, O],
    [O, O, O, O, O, O, O, O, O, O],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

#positions and sizes
MARGIN=100
grid_pos= (40, 80, WIDTH-MARGIN, HEIGHT-MARGIN)
cell_size= 50
grid_size= cell_size * ROWS 

