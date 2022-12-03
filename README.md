This is a practice project to implement AI to popular number game.

resources
---------
This file contains all the components needed to play the game, such as taking a turn and spawning next cell. It also contains global variables and all the functions used to interact with them.

main
----
File to run the game and the decision selectors. Currently "messy", since it has all the possible simulation. TODO: either break into multiple main functions or take run parameters.

tests
-----
Contains some test of base game functions.

blind_selectors
---------------
Contains simplest decision making functions, which only input is the possible directions and points given by the very next move. These include

    - Preferred directions
    - Maximized points + preferred direction (as a tie breaker)
    - Random move
    - Preset pattern
    - Pattern finder (builds a pattern with x members by playing 4*y games per rotation and selecting the best candidate for next member to the pattern)

