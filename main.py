import resources
import blind_selectors

def main():
    resources.add_random()
    possibilities = resources.possible_directions()
    round = 0
    results1 = []
    results2 = []
    results3 = []
    results4 = []
    results5 = []
    results6 = []
    contender = 0
    best_result = 0
    pattern_hunt(10,50)
    blind_selectors.reset_step()

    for i in range(1000):
        pass
    '''
        play(blind_selectors.preferred_directions1)
        results1.append(resources.points)
        if(resources.points > best_result):
            best_result = resources.points
            contender = resources.game_grid.copy()
            print("--------1")
            resources.print_grid()

        play(blind_selectors.preferred_directions2)
        results2.append(resources.points)
        if(resources.points > best_result):
            best_result = resources.points
            contender = resources.game_grid.copy()
            print("--------2")
            resources.print_grid()

        play(blind_selectors.short_sighted)
        results3.append(resources.points)
        if(resources.points > best_result):
            best_result = resources.points
            contender = resources.game_grid.copy()
            print("--------3")
            resources.print_grid()

        play(blind_selectors.random_select)
        results4.append(resources.points)
        if(resources.points > best_result):
            best_result = resources.points
            contender = resources.game_grid.copy()
            print("--------4")
            resources.print_grid()

        play(blind_selectors.periodic_select1, [0, 1, 0, 1, 3, 1])
        results5.append(resources.points)
        if(resources.points > best_result):
            best_result = resources.points
            contender = resources.game_grid.copy()
            print("--------5")
            resources.print_grid()
        play(blind_selectors.periodic_select2, blind_selectors.selector_pattern)
        results6.append(resources.points)
        if(resources.points > best_result):
            best_result = resources.points
            contender = resources.game_grid.copy()
            print("--------6")
            resources.print_grid()
    '''

    print(sum(results1))
    print(max(results1))

    print(sum(results2))
    print(max(results2))

    print(sum(results3))
    print(max(results3))

    print(sum(results4))
    print(max(results4))

    print(sum(results5))
    print(max(results5))

    print(sum(results6))
    print(max(results6))


def playManually():
    print("Start the game")
    resources.add_random()
    for round in range(60):
        command = input("Read command")
        try:
            command = int(command)
            resources.take_turn(command)
        except:
            print("invalid input")
        resources.print_grid()
        print("-------"+str(round%4))


def pattern_hunt(length, accuracy):
    find_pattern(length, accuracy)
    print(blind_selectors.selector_pattern)


def play(selector, pattern = False):
    resources.reset_points()
    resources.reset_game_grid()
    resources.add_random()
    possibilities = resources.possible_directions()
    if not pattern:
        while possibilities != [-1, -1, -1, -1]:
            dir = selector(possibilities)
            resources.take_turn(dir)
            possibilities = resources.possible_directions()
    else:
        while possibilities != [-1, -1, -1, -1]:
            dir = selector(possibilities, pattern)
            resources.take_turn(dir)
            possibilities = resources.possible_directions()   

def find_pattern(length, accuracy):
    for round in range(length):
        blind_selectors.reset_candidates()
        for cycle in range(accuracy):
            for dir in range(4):
                play(blind_selectors.periodic_select2, blind_selectors.selector_pattern)
                blind_selectors.update_candidate(dir, resources.points)
        print(blind_selectors.candidates)
        blind_selectors.select_candidate()

main()
#pattern_hunt()