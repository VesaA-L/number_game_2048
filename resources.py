import random

dim = 4
game_grid = [[0 for col in range(dim)] for row in range(dim)]
points = 0

def reset_game_grid():
    global game_grid
    game_grid = [[0 for col in range(dim)] for row in range(dim)]


def set_dim(int):
    global dim
    dim = int

def reset_points():
    global points
    points = 0

def take_turn(dir):
    global game_grid
    changed = next_grid(dir)
    if changed:
        add_random()
    return

def next_grid(dir):
    global game_grid
    global points
    changed = False
    match dir:
        case 0: #up
            for column in range(dim):
                # Combine
                for row in range(dim-1):
                    a = 1
                    while row + a < dim and game_grid[row+a][column] == 0:
                        a+=1
                    if row + a < dim and game_grid[row][column]==game_grid[row+a][column]:
                        game_grid[row][column]=2*game_grid[row][column]
                        game_grid[row+a][column]=0
                        points += game_grid[row][column]
                        changed = True
                # Move
                for row in range(dim-1):
                    if game_grid[row][column]==0:
                        for position in range(row+1,dim):
                            if game_grid[position][column] != 0:
                                game_grid[row][column]=game_grid[position][column]
                                game_grid[position][column] = 0
                                changed = True
                                break
        case 1: #right
            for row in game_grid:
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
                    while row + a < dim and game_grid[dim-1-(row+a)][column] == 0:
                        a+=1
                    if row + a < dim and game_grid[dim-1-row][column]==game_grid[dim-1-(row+a)][column]:
                        game_grid[dim-1-row][column]=2*game_grid[dim-1-row][column]
                        points += game_grid[dim-1-row][column]
                        game_grid[dim-1-(row+a)][column]=0
                        changed = True
                # Move
                for row in range(dim-1):
                    if game_grid[dim-1-row][column]==0:
                        for position in range(row+1,dim):
                            if game_grid[dim-1-position][column] != 0:
                                game_grid[dim-1-row][column]=game_grid[dim-1-position][column]
                                game_grid[dim-1-position][column] = 0
                                changed = True
                                break
        case 3: #left 
            for row in game_grid:
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

def add_random():
    global game_grid
    empty_positions: list[tuple[int, int]] = []
    for i in range(dim):
        for j in range(dim):
            if game_grid[i][j] == 0:
                empty_positions.append((i,j))
    if not bool(empty_positions):
        print("something went wrong and there was no empty spaces")
        return
    positions = empty_positions[random.randrange(len(empty_positions))]
    if random.random()< 0.8:
        game_grid[positions[0]][positions[1]] = 2
    else:
        game_grid[positions[0]][positions[1]] = 4

def print_grid():
    for i in range(dim):
        for j in range(dim):
            print(game_grid[i][j], end=" ")
        print()

# Directions are as follows: 0 up, 1 right, 2 down, 3 left

def possible_directions():
    global game_grid
    up, right, down, left= 0, 0, 0, 0
    # Up
    for column in range(dim):
        up_row = []
        for row in range(dim):
            up_row.append(game_grid[row][column])
        up += rowPointCalculation(up_row)
    if(up == 0):
        up = -1
        for column in range(dim):
            up_row = []
            for row in range(dim):
                up_row.append(game_grid[row][column])
            if(check_movement(up_row)):
                up = 0
                break
    # Right
    for row in game_grid:
        row.reverse()
        right += rowPointCalculation(row)
        # We need to reverse row's back
        row.reverse()
    if(right == 0):
        right = -1
        for row in game_grid:
            row.reverse()
            if(check_movement(row)):
                right = 0
                row.reverse()
                break
            row.reverse()
    # Down
    for column in range(dim):
        down_row = []
        for row in range(dim):
            down_row.append(game_grid[dim-1-row][column])
        down += rowPointCalculation(down_row)
    if(down == 0):
        down = -1
        for column in range(dim):
            down_row = []
            for row in range(dim):
                down_row.append(game_grid[dim-1-row][column])
            if(check_movement(down_row)):
                down = 0
                break
    # Left
    for row in game_grid:
        left += rowPointCalculation(row)
    if(left == 0):
        left = -1
        for row in game_grid:
            if(check_movement(row)):
                left = 0
                break

    return [up, right, down, left]


# Param: row is expeced to be a List with dim members
def rowPointCalculation(row):
    # Global dim not used for testing purposes
    dim = len(row)
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
    while(a < len(row)):
        if row[a] == 0:
            i = 1
            while(a+i < len(row)):
                if(row[a+i] != 0):
                    return True
                i += 1
        a += 1
        
    return False


