import copy

import resources
from grid_evaluator import evaluate_4x4_grid, tree_search

def test_row_point_calculator():
  
    test_row_1 = [0,2,0,2,4]
    expected_1 = 4
    test_row_2 = [0,2,4,0,2,4]
    expected_2 = 0
    test_row_3 = [2,2,2,0,4]
    expected_3 = 4
    test_row_4 = [16,2,16,2,16,4,32,32,64,2,2]
    expected_4 = 68
    test_row_5 = [2,2,0,0,2,0,0,2,2,0,4]
    expected_5 = 8
    test_row_5 = [0,2,0,2,0,0,2,0,0,2,0,2,0,4]
    expected_5 = 8
    test_row_6 = [4,4,0,0]
    expected_6 = 8
    test_row_7 = [0,0,4,4]
    expected_7 = 8
    print(test_row_1)
    print(bool(resources.rowPointCalculation(test_row_1)==expected_1))
    print(test_row_1)
    print(bool(resources.rowPointCalculation(test_row_2)==expected_2))
    print(bool(resources.rowPointCalculation(test_row_3)==expected_3))
    print(bool(resources.rowPointCalculation(test_row_4)==expected_4))
    print(bool(resources.rowPointCalculation(test_row_5)==expected_5))
    print(bool(resources.rowPointCalculation(test_row_6)==expected_6))
    print(bool(resources.rowPointCalculation(test_row_7)==expected_7))




def test_row_movement():
    print("Testing movement")
    # movement direction <----
    test_row_1 = [0,2,0,2,4]
    expected_1 = True
    test_row_2 = [0,2,4,0,2,4]
    expected_2 = True
    test_row_3 = [2,2,2,0,4]
    expected_3 = True
    test_row_4 = [16,2,16,2,16,4,32,32,64,2,2]
    expected_4 = False
    test_row_5 = [2,2,0,0,2,0,0,2,2,0,4]
    expected_5 = True
    test_row_5 = [0,2,0,2,0,0,2,0,0,2,0,2,0,4]
    expected_5 = True
    test_row_6 = [4,4,0,0]
    expected_6 = False
    test_row_7 = [0,0,4,4]
    expected_7 = True
    print(test_row_1)
    print(bool(resources.check_movement(test_row_1)==expected_1))
    print(test_row_1)
    print(bool(resources.check_movement(test_row_2)==expected_2))
    print(bool(resources.check_movement(test_row_3)==expected_3))
    print(bool(resources.check_movement(test_row_4)==expected_4))
    print(bool(resources.check_movement(test_row_5)==expected_5))
    print(bool(resources.check_movement(test_row_6)==expected_6))
    print(bool(resources.check_movement(test_row_7)==expected_7))
    

def test_grid_evaluator():
    test_grid_1 = [
        [0,0,1,0],
        [0,16,32,0],
        [0,64,1,16],
        [8,0,1,0]
    ]
    test_grid_2 = [
        [0,0,1,0],
        [0,16,32,0],
        [0,64,128,16],
        [8,16,512,1024]
    ]
    test_grid_3 = [
        [0,0,1,0],
        [256,16,32,0],
        [0,64,1,16],
        [512,0,1,512]
    ]
    print("test1")
    print(evaluate_4x4_grid(test_grid_1))
    print("test2")
    print(evaluate_4x4_grid(test_grid_2))
    print("test3")
    print(evaluate_4x4_grid(test_grid_3))

test_row_point_calculator()
test_row_movement()
test_grid_evaluator()

test_grid_2 = [
        [0,0,1,0],
        [0,16,32,0],
        [0,64,128,16],
        [8,16,512,1024]
]
resources.set_grid(copy.deepcopy(test_grid_2))
tree_search()
resources.print_grid()
print(test_grid_2)