from gridclass import *
from gameController import *

def main():
    g = grid(200)
    #print(g.getGrid())
    #print(g.pgrid)
    #g.updateGridSpot(2,2,1)
    #g.updateGridSpot(2,3,1)
    #g.updateGridSpot(3,2,1)
    #g.updateGridSpot(1,2,1)
    #g.updateGridSpot(2,1,1)
    #displayGridASC(g)
    g.createRandomGrid()
    runGame(g)

main()