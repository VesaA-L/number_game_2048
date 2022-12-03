import random
'''
The first section of the blind selectors consists of basic algorithms
that select the nex direction based on the information given in the possibilities.

The second section is for the blind "learning" algorithms that builds a pattern
from the scratch by selecting new direction from the 4 candidates.
'''
# Up,left,right,down -> 0,3,1,2
def preferred_directions1(possibilities):
    if possibilities[0] != -1:
        return 0
    if possibilities[3] != -1:
        return 3
    if possibilities[2] != -1:
        return 2
    if possibilities[1] != -1:
        return 1


# Up,left,down,right -> 0,3,2,1
def preferred_directions2(possibilities):
    if possibilities[0] != -1:
        return 0
    if possibilities[3] != -1:
        return 3
    if possibilities[2] != -1:
        return 2
    if possibilities[1] != -1:
        return 1

# Select the direction which gives most points
def short_sighted(possibilities):
    choice = 0
    index = 1
    while(index < 4):
        if possibilities[index] > possibilities[choice]:
            choice = index
        index += 1
    return choice

# Random
def random_select(possibilities):
    return random.randrange(4)

current_step1 = 0
current_step2 = 0

def reset_step():
    global current_step1
    global current_step2
    current_step1 = 0
    current_step2 = 0

def periodic_select1(possibilities, pattern):
    next_dir = 0
    global current_step1
    loop = 0
    while(possibilities[pattern[current_step1]] == -1 and loop < len(pattern)):
        current_step1 = (current_step1+1)%len(pattern)
        loop += 1
    if loop < len(pattern):
        next_dir = pattern[current_step1]
        current_step1 = (current_step1+1)%len(pattern)
        return next_dir
    # Randomize the next step?
    else:
        while(next_dir < 4 and possibilities[next_dir] == -1):
            next_dir += 1
        return next_dir

#TODO DO BETTER
def periodic_select2(possibilities, pattern):
    next_dir = 0
    global current_step2
    loop = 0
    while(possibilities[pattern[current_step2]] == -1 and loop < len(pattern)):
        current_step2 = (current_step2+1)%len(pattern)
        loop += 1
    if loop < len(pattern):
        next_dir = pattern[current_step2]
        current_step2 = (current_step2+1)%len(pattern)
        return next_dir
    # Randomize the next step?
    else:
        while(next_dir < 4 and possibilities[next_dir] == -1):
            next_dir += 1
        return next_dir

'''
The "learning" selectors start here
'''
selector_pattern = [0,1]
candidates = [0,0,0,0]

def reset_candidates():
    global candidates
    candidates = [0,0,0,0]

def select_candidate():
    #!!! this is meme, wrost candidate
    selector_pattern.append(candidates.index(max(candidates)))

def update_candidate(index, amount):
    global candidates
    candidates[index] = candidates[index] + amount

def reset_pattern():
    global selector_pattern
    selector_pattern = [0,1]
# Considers the possibilities and the points given
def learning_selector_with_possibilities():
    return