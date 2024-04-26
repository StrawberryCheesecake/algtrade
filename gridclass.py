import random

class grid:
    x = 20
    pgrid = { (i,j):0 for i in range(20) for j in range(20) }
    fgrid = { (i,j):0 for i in range(20) for j in range(20) }
    
    def __init__(self, x, pgrid = None ,fgrid = None):
        self.x = x
        self.pgrid = pgrid if pgrid is not None else self.createGrid(x)
        self.fgrid = fgrid if fgrid is not None else self.createGrid(x)
    
    #get functions for a grid
    def getGrid(self):
        return self.pgrid
    def getFGrid(self):
        return self.fgrid
    def getGridSize(self):
        return self.x
    
    #create grid function to avoid repeating the code and improve readability
    @staticmethod
    def createGrid(x):
        return { (i,j):0 for i in range(x) for j in range(x) }
    
    #reset grid to empty state
    def resetGridState(self):
        self.pgrid = grid.createGrid(self.x)
        return 
    #reset F grid to empty state
    def resetFGridState(self):
        self.fgrid = grid.createGrid(self.x)
        return 
    
    #update a specific spot in the grid to a new value
    def updateGridSpot(self, x, y, value):
        if (x,y) in self.pgrid:    
            if (value == 1 or value == 0):
                self.pgrid[x,y] = value
                return
            raise("Error your grid value is out of bounds")
        raise("Error your grid point is out of bounds")
    #update a specific spot in the grid to a new value
    def updateFGridSpot(self, x, y, value):
        if (x,y) in self.fgrid:    
            if (value == 1 or value == 0):
                self.fgrid[x,y] = value
                return
            raise("Error your grid value is out of bounds")
        raise("Error your grid point is out of bounds")
        
    #update the grids entire grid based upon a new grid value
    def updateGrid(self):
        self.pgrid = self.fgrid
        self.resetFGridState()
        return
        
    #function to calculate future state based upon current state
    def calculateFState(self):
        #iterate through all cells
        for i in range(self.x):
            for j in range(0,self.x):
                #get all neighbors of the cell and itself to see what is alive
                count = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        #print ("this is ij:", i, j)
                        #print(k,l)
                        if (k,l) in self.pgrid:
                            if self.pgrid[k,l] == 1:
                                count += 1
                #now with all our neighbors we do something depending on the neighbors and if cell is alive
                #check if cell alive, if the cell is alive we counted itself in above so deduct one
                #print(count)
                if self.pgrid[i,j] == 1:
                    count -= 1
                    #Cell in survive range survive otherwise it dies
                    if 1 < count < 4:
                        self.fgrid[i,j] = 1
                    else:
                        self.fgrid[i,j] = 0
                #cell dead but it is in range
                else:
                    if count == 3:
                        self.fgrid[i,j] = 1
                    else:
                        self.fgrid[i,j] = 0
        #after iterating through every cell we set pgrid to be fgrid and reset fgrid
        self.updateGrid()
        return
    
    #TODO create random grid state
    def createRandomGrid(self):
        for key in self.pgrid:
            self.pgrid[key] = random.choice([0,1])
        return
    #TODO Save grid state? 
    #TODO Import Grid State?

    
#simple ascii dispaly of a grid to help 
def displayGridASC(grid):
    for i in range(0,grid.x):
        for j in range(0,grid.x):
            print(grid.pgrid[i,j], end = "    ")
        print("\n")    
            


            
