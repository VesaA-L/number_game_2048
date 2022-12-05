import random
import numpy as np
from copy import deepcopy
# Playing the game and blind algorithms work just fine with any dimensions, but grid analysing
# and neural networks work only with grid size 4
dim = 4
game_grid = np.zeros((dim, dim), dtype=np.int16) # max value 32k, sufficient for 4x4, otherwise use int32
points = 0

def reset_game_grid():
    global game_grid
    game_grid = np.zeros((dim, dim), dtype=np.int16)

def set_grid(grid):
    global game_grid
    game_grid = [grid[a][:] for a in range(dim)]

def get_grid():
    global game_grid
    return [game_grid[a][:] for a in range(dim)]

def insert(value, row, column):
    global game_grid
    game_grid[row][column] = value

def set_dim(int):
    global dim
    dim = int

def reset_points():
    global points
    points = 0

def take_turn(grid, dir):
    changed = next_grid(grid, dir)
    if changed:
        add_random(grid)
    return grid

def next_grid(grid, dir):
    global points
    changed = False
    match dir:
        case 0: #up
            for column in range(dim):
                # Combine
                for row in range(dim-1):
                    a = 1
                    while row + a < dim and grid[row+a][column] == 0:
                        a+=1
                    if row + a < dim and grid[row][column]==grid[row+a][column]:
                        grid[row][column]=2*grid[row][column]
                        grid[row+a][column]=0
                        points += grid[row][column]
                        changed = True
                # Move
                for row in range(dim-1):
                    if grid[row][column]==0:
                        for position in range(row+1,dim):
                            if grid[position][column] != 0:
                                grid[row][column]=grid[position][column]
                                grid[position][column] = 0
                                changed = True
                                break
        case 1: #right
            for row in grid:
                for column in range(dim-1):
                    a = 1
                    while column + a < dim and row[dim-1-(column+a)] == 0:
                        a+=1
                    if column + a < dim and row[dim-1-column]==row[dim-1-(column+a)]:
                        row[dim-1-column]=2*row[dim-1-column]
                        points += row[dim-1-column]
                        row[dim-1-(column+a)]=0
                        changed = True
                for column in range(dim-1):
                    if row[dim-1-column]==0:
                        for position in range(column + 1,dim):
                            if row[dim-1-position] != 0:
                                row[dim-1-column]=row[dim-1-position]
                                row[dim-1-position] = 0
                                changed = True
                                break
        case 2: #down
            for column in range(dim):
                # Combine
                for row in range(dim-1):
                    a = 1
                    while row + a < dim and grid[dim-1-(row+a)][column] == 0:
                        a+=1
                    if row + a < dim and grid[dim-1-row][column]==grid[dim-1-(row+a)][column]:
                        grid[dim-1-row][column]=2*grid[dim-1-row][column]
                        points += grid[dim-1-row][column]
                        grid[dim-1-(row+a)][column]=0
                        changed = True
                # Move
                for row in range(dim-1):
                    if grid[dim-1-row][column]==0:
                        for position in range(row+1,dim):
                            if grid[dim-1-position][column] != 0:
                                grid[dim-1-row][column]=grid[dim-1-position][column]
                                grid[dim-1-position][column] = 0
                                changed = True
                                break
        case 3: #left 
            for row in grid:
                for column in range(dim-1):
                    a = 1
                    while column + a < dim and row[column+a] == 0:
                        a+=1
                    if column + a < dim and row[column]==row[column+a]:
                        row[column]=2*row[column]
                        points += row[column]
                        row[column+a]=0
                        changed = True
                for column in range(dim-1):
                    if row[column]==0:
                        for position in range(column + 1,dim):
                            if row[position] != 0:
                                row[column]=row[position]
                                row[position] = 0
                                changed = True
                                break
        case _:
            #print("Invalid direction")
            return False
    return changed

def add_random(grid):
    empty_positions: list[tuple[int, int]] = []
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == 0:
                empty_positions.append((i,j))
    if not bool(empty_positions):
        print("something went wrong and there was no empty spaces")
        return
    positions = empty_positions[random.randrange(len(empty_positions))]
    if random.random()< 0.8:
        grid[positions[0]][positions[1]] = 2
    else:
        grid[positions[0]][positions[1]] = 4

def print_grid(grid):
    for i in range(dim):
        for j in range(dim):
            print(grid[i][j], end=" ")
        print()

# Directions are as follows: 0 up, 1 right, 2 down, 3 left

def possible_directions(grid):
    up, right, down, left= 0, 0, 0, 0
    # Up
    for column in range(dim):
        up_row = np.empty(dim, dtype= np.int16)
        for row in range(dim):
            up_row[row] = grid[row][column]
        up += rowPointCalculation(up_row)
    if(up == 0):
        up = -1
        for column in range(dim):
            up_row = np.empty(dim, dtype= np.int16)
            for row in range(dim):
                up_row[row] = grid[row][column]
            if(check_movement(up_row)):
                up = 0
                break
    # Right
    for row in grid:
        right += rowPointCalculation(np.flip(row))
    if(right == 0):
        right = -1
        for row in grid:
            if(check_movement(np.flip(row))):
                right = 0
                break
    # Down
    for column in range(dim):
        down_row = np.empty(dim, dtype= np.int16)
        for row in range(dim):
            down_row[row] = grid[dim-1-row][column]
        down += rowPointCalculation(down_row)
    if(down == 0):
        down = -1
        for column in range(dim):
            down_row = np.empty(dim, dtype= np.int16)
            for row in range(dim):
                down_row[row] = grid[dim-1-row][column]
            if(check_movement(down_row)):
                down = 0
                break
    # Left
    for row in grid:
        left += rowPointCalculation(row)
    if(left == 0):
        left = -1
        for row in grid:
            if(check_movement(row)):
                left = 0
                break

    return [up, right, down, left]


# Param: row is expeced to be a List with dim members
def rowPointCalculation(row):
    # Global dim not used for testing purposes
    dim = row.size
    points = 0
    a = 0
    while(a<dim-1):
        i=1
        while(a + i < dim and row[a+i] == 0):
            i += 1
        if(a + i == dim):
            return points
        if row[a] == row[a + i]:
                points += 2 * row[a]
                a+=i
        a+=1
    return points

def check_movement(row):
    a = 0
    while(a < row.size):
        if row[a] == 0:
            i = 1
            while(a+i < row.size):
                if(row[a+i] != 0):
                    return True
                i += 1
        a += 1
        
    return False


def find_empty_positions(grid):
    empty_positions: list[tuple[int, int]] = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                empty_positions.append((i,j))
    return empty_positions