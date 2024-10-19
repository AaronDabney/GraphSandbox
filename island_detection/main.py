from copy import deepcopy

gridData = [
    [[1, 0],
     [0, 1],
     [1, 0],
     [1, 1]],

    [[1, 1],
     [0, 0],
     [0, 0],
     [1, 1]],

    [[1, 0, 1],
     [0, 0, 0],
     [0, 0, 0],
     [1, 0, 1]],

    [[1, 0, 1],
     [0, 0, 0],
     [0, 1, 0],
     [0, 0, 0],
     [1, 0, 1]],

    [[1, 0, 1],
     [0, 1, 0],
     [0, 1, 0],
     [0, 1, 0],
     [1, 0, 1]],
]

def islandDetector(gridInput):
    grid = deepcopy(gridInput) 

    gridWidth = len(grid[0])
    gridHeight = len(grid)

    offsets = [[ 0, 1],
               [ 1, 1],
               [ 1, 0],
               [ 1,-1],
               [ 0,-1],
               [-1,-1],
               [-1, 0],
               [-1, 1]]

    inBounds = lambda x, y : not (x < 0 or x >= gridWidth or y < 0 or y >= gridHeight)

    getGrid = lambda x, y : grid[y][x]

    def setGrid(x, y, val):
        grid[y][x] = val

    def searchAndZero(x, y):
        if (not inBounds(x, y)):
            return
        if (getGrid(x, y)):
            setGrid(x, y, 0)
            for offset in offsets:
                xOffset = offset[0]
                yOffset = offset[1]
                searchAndZero(x + xOffset, y + yOffset)


    islandCount = 0

    for y in range(gridHeight):
        for x in range(gridWidth):
            if (not getGrid(x, y)):
                continue
            islandCount += 1
            searchAndZero(x, y)
            
    return islandCount


for grid in gridData:
    print(islandDetector(grid))

# Output -> 1, 2, 4, 5, 1
