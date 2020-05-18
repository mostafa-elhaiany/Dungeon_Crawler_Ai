# Dungeon Crawler Ai
Building different Ai with search algorithms able to learn and play a custom Dungeon Crawler game


# about the game
    The game is a maze in a way the player has to go search for a weapon, marked yellow, and go kill the monsters on 
    the board.
    it can't hit the walls/obstacles or it loses health and it can't hit a monster without a weapon or else it dies

# about the solvers
    I used three search algorithms, breadthfirst search, Dijkstra, and A* search to see which could solve the level
    in an efficient way,
    BFS was just taking too much time for a large board
    Dijkstra was much better working almost instantly 
    and A* also working instantly and solving the level effieciently 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The code runs on python3
you'll need the following library

```
pygame
```
which handles the game GUI

everything else is plain vanilla python



### Installing


make sure you have a python3 setup up and running

then to install the needed libraries

```
pip install pygame
```

to make sure everything is up and running
```
python main.py
```
this should start the game where you can play yourself. 


### Break down into file system and Algorithms used

the code is divided into two parts, the game, and the solvers

```
GAME
```
for the game folder settings hold some of the constants and settings used for colours number of rows and columns etc,
Dungeon holds the code for building the game with pygame GUI, all the needed information are commented in the file


```
Solvers
```
for the solvers folder there is a different class for every solver,

1)  BreadthFirstSearch.py
        for bfs you usually have a graph and you're searching for a certain value, and you go down, level by level
        checking each till you find the certain value you're looking for.
        as such every valid cell is a node, and every possible move from that cell is an adjacent node
        and you search through all possible combinations on each level untill you find the answer you're looking for
        and then the rest is as easy as following directions to that node.
        however it takes a lot of time to run, and haven't solved big boards

2)  Dijsktra.py
        Dijkstra shortest path algorithm as the name applies is an efficient path finding approach
        that finds the shortest path to get to each node from a starting point,
        using the same node-cell notion I built a table that for every cell position (i,j) holds information as 
        the set of directions you need to get there and the cost of such movement, for simplicity the cost of 
        moving from any cell to an adjacent one is 1.
        then you use a priority queue and pop elements to find the shortest path between each node till you reach your
        goal node.

3)  Astar.py
        A* search algorithm works the same like Dijkstra,
        however a problem with dijkstra is it follows a short path without minding for the direction of that path
        even though it can be searching in a path quite the opposite of your goal point

        so A* introduces the use of heuristics each node now has the set of directions it needs to take, its cost
        which is the length of the set of directions but also the heuristic function, which for this example was ecluidean 
        distance.
        
        so now the algorithm not only uses the cost of the node from the start position but also the heuristic of the goal position


### Running the Agents

in the main file game is the dungeon puzzle that the Ai will try to solve,
test_board is a premade testboard that you can run instantly 
or you can run the function build which gives you the ability to build the board you want the ai to solve,
the game has to has a player, a weapon, at least one obstacle and at least one monster,
you simply click on the cell you want to add something in, press p,w,o,m for player,weapon,obstacle,or monster respectivly
and then run agent.solve() which will use the chosen agent to solve that level




