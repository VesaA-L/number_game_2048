from resources import possible_directions, set_grid, get_grid, next_grid, insert, find_empty_positions, print_grid


'''
Takes 4x4 game grid as an input and returns a numeric evaluation of the
game state. The numeric value has minimum of 0 which occurs if the game is
lost.
'''
def evaluate_4x4_grid(grid):
    points = 0
    # There are no possible directions
    '''
    Add points by finding the largest cell:
    '''
    largest_cell = 0
    second_largest_cell = 0
    empty_cells = 0
    largest_cell_position = (0, 0)
    second_largest_cell_position = (0, 0)
    for row in range(4):
        for column in range(4):
            candidate = grid[row][column]
            if candidate == 0:
                empty_cells += 1
            elif candidate > largest_cell:
                second_largest_cell = largest_cell
                second_largest_cell_position = largest_cell_position
                largest_cell = candidate
                largest_cell_position = (row, column)
            elif candidate > second_largest_cell:
                second_largest_cell = candidate
                second_largest_cell_position = (row, column)
    points += 4*largest_cell.bit_length() + 2*second_largest_cell.bit_length()
    '''
    Add points by finding the total number of empty cells:
    '''
    points += empty_cells
    
    '''
    Add points by finding location of the largest cell and
    by finding location of the second largest cell compared to the largest:
    8 4 4 8
    4 0 0 4
    4 0 0 4
    8 4 4 8
    '''
    if not largest_cell == second_largest_cell:
        if largest_cell_position[0] == 0 or largest_cell_position[0] == 3:
            points += 5
        if largest_cell_position[1] == 0 or largest_cell_position[1] == 3:
            points += 5
        if abs(largest_cell_position[0]-second_largest_cell_position[0]) + abs(largest_cell_position[0]-second_largest_cell_position[0]) == 1:
            points += 5
    else:
        if abs(largest_cell_position[0]-second_largest_cell_position[0]) + abs(largest_cell_position[0]-second_largest_cell_position[0]) == 1:
            points += 7
        position_1 = 0
        position_2 = 0
        if largest_cell_position[0] == 0 or largest_cell_position[0] == 3:
            position_1 += 3
        if largest_cell_position[1] == 0 or largest_cell_position[1] == 3:
            position_1 += 3
        if second_largest_cell_position[0] == 0 or second_largest_cell_position[0] == 3:
            position_2 += 3
        if second_largest_cell_position[1] == 0 or second_largest_cell_position[1] == 3:
            position_2 += 3
        points += max(position_1, position_2)
    '''
    Add points by number of possible directions:
    3 or 4 -> 7pts
    2 -> 5pts
    '''
    available_directions = sum(map(lambda x : x != -1, possible_directions(grid)))
    if available_directions < 2:
        points += 7
    if available_directions == 2:
        points += 5
        
    return points

'''
Investigates the future possibilites and selects the best average scenario.
'''
def tree_search():
    original_grid = get_grid()
    directions = possible_directions()
    # Depth 1: make a move to an available direction
    evaluation_by_direction = [0,0,0,0]
    for i in range(4):
        set_grid(original_grid)
        if directions[i] == -1:
            continue
        next_grid(i)

        grid_after_first_move = get_grid()
        empty_positions = find_empty_positions()

        # Depth 2: insert the new cell to an available square
        depth2total = 0
        for first_position in empty_positions:
            for first_random in range(2):
                set_grid(grid_after_first_move)
                insert(2 + first_random *2, first_position[0], first_position[1])

                grid_after_first_random = get_grid()
                second_directions = possible_directions()

                # Depth 3: make a second move to an available direction
                depth3best = 0
                for j in range(4):
                    set_grid(grid_after_first_random)
                    if second_directions[j] == -1:
                        continue
                    next_grid(j)

                    grid_after_second_move = get_grid()
                    second_empty_positions = find_empty_positions()

                    # Depth 4: insert second new cell
                    depth4total = 0
                    for second_position in second_empty_positions:
                        for second_random in range(2):
                            set_grid(grid_after_second_move)
                            insert(2 + second_random *2, second_position[0], second_position[1])

                            grid_after_second_random = get_grid() 
                            third_directions = possible_directions()

                            # Depth 5: make a final move
                            best_evaluation = 0
                            for k in range(4):
                                set_grid(grid_after_second_random)
                                if third_directions[k] == -1:
                                    continue
                                next_grid(k)
                                result = evaluate_4x4_grid(get_grid())
                                if result > best_evaluation:
                                    best_evaluation = result
                            depth4total += best_evaluation
                    if depth3best < depth4total:
                        depth3best = depth4total
                depth2total += depth3best 
        evaluation_by_direction[i]=depth2total
    set_grid(original_grid)
    maximum = max(evaluation_by_direction)
    dir = evaluation_by_direction.index(maximum)
    if maximum == 0:
        return directions.index(next(x for x in directions if x != -1))
    return dir
     