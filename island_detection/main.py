from copy import deepcopy

grid_data = [
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

def island_detector(grid_input):
    grid = deepcopy(grid_input) 

    grid_width = len(grid[0])
    grid_height = len(grid)

    offsets = [[ 0, 1],
               [ 1, 1],
               [ 1, 0],
               [ 1,-1],
               [ 0,-1],
               [-1,-1],
               [-1, 0],
               [-1, 1]]

    in_bounds = lambda x, y : not (x < 0 or x >= grid_width or y < 0 or y >= grid_height)

    get_grid = lambda x, y : grid[y][x]

    def set_grid(x, y, val):
        grid[y][x] = val

    def search_and_zero(x, y):
        if (not in_bounds(x, y)):
            return
        if (get_grid(x, y)):
            set_grid(x, y, 0)
            for offset in offsets:
                x_Offset = offset[0]
                y_Offset = offset[1]
                search_and_zero(x + x_Offset, y + y_Offset)


    island_count = 0

    for y in range(grid_height):
        for x in range(grid_width):
            if (not get_grid(x, y)):
                continue
            island_count += 1
            search_and_zero(x, y)
            
    return island_count


for grid in grid_data:
    print(island_detector(grid))

# Output -> 1, 2, 4, 5, 1
