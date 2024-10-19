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

    width = len(grid[0])
    height = len(grid)

    offsets = [[ 0, 1],
               [ 1, 1],
               [ 1, 0],
               [ 1,-1],
               [ 0,-1],
               [-1,-1],
               [-1, 0],
               [-1, 1]]

    def inBounds(x, y):
        if (x < 0 or y < 0):
            return False
        if (x >= width or y >= height):
            return False
        return True

    def getGrid(x, y):
        return grid[y][x]

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

    for y in range(height):
        for x in range(width):
            if (not getGrid(x, y)):
                continue
            islandCount += 1
            searchAndZero(x, y)
            
    return islandCount


for grid in gridData:
    print(islandDetector(grid))

# Output -> 1, 2, 4, 5, 1
