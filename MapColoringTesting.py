# CS 76: Artificial Intelligence - PA4:CSP
# Fall 2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaboration: Discussed ideas with James Fleming

# Import statements to bring in CSP solvers and MapColoring CSP
from MapColoringCSP import MapColoringCSP
from CSP import *


# Testing Class For Map Coloring
class MapColoringTesting:
    # Test class to try a few things to get everything working

    # MAP COLORING CONSTRAINT SATISFACTION PROBLEMS

    # Making a MapColoringCSP with New Hampshire
    # Variables: VT = 0, NH = 1, ME = 2, MA = 3
    # Domains: R = 0, G = 1, B = 2
    # Constraints: (0,1) means that WA cannot be same color as NT
    v = [0, 1, 2, 3]
    var_dictionary = {0: 'VT', 1: 'NH', 2: 'ME', 3: 'MA'}
    d = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2]}
    value_dictionary = {0: 'red', 1: 'green', 2: 'blue'}
    c = [(0, 1), (0, 3), (1, 2), (1, 3)]
    # Now we create a MapColoringCSP. Fingers crossed this works. Test if constraint generation works
    mapCSP = MapColoringCSP(v, d, c)
    assignment = backtracking_search(mapCSP)
    print("MapColoringCSP Test 1: New Hampshire and Friends (No Heuristics) Consistency Checks: "
          + str(mapCSP.is_consistent_checks))
    print(mapCSP.print_assignment(assignment, var_dictionary, value_dictionary) + "\n")

    # Making a MapColoringCSP with Australia
    # Variables: WA = 0, NT = 1, Q = 2, NSW = 3, V = 4, SA = 5, T = 6
    # Domains: R = 0, G = 1, B = 2
    # Constraints: (0,1) means that WA cannot be same color as NT
    v = [0, 1, 2, 3, 4, 5, 6]
    var_dictionary = {0: 'WA', 1: 'NT', 2: 'Q', 3: 'NSW', 4: 'V', 5: 'SA', 6: 'T'}
    value_dictionary = {0: 'red', 1: 'green', 2: 'blue'}
    d = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2], 5: [0, 1, 2], 6: [0, 1, 2]}
    c = [(0, 1), (0, 5), (1, 2), (1, 5), (2, 3), (2, 5), (3, 5), (3, 4), (4, 5)]
    mapCSP2 = MapColoringCSP(v, d, c)
    assignment = backtracking_search(mapCSP2)
    print("MapColoringCSP Test 2: Australia (No Heuristics) Consistency Checks: "
          + str(mapCSP2.is_consistent_checks))
    print(mapCSP2.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    # MRV Heuristic
    mapCSP3 = MapColoringCSP(v, d, c, mrv=True)
    assignment = backtracking_search(mapCSP3)
    print("MapColoringCSP Test 3: Australia (MRV Heuristic) Consistency Checks: "
          + str(mapCSP2.is_consistent_checks))
    print(mapCSP2.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    mapCSP4 = MapColoringCSP(v, d, c, degree=True)
    assignment = backtracking_search(mapCSP4)
    print("MapColoringCSP Test 4: Australia (Degree Heuristic) Consistency Checks: "
          + str(mapCSP4.is_consistent_checks))
    print(mapCSP4.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    mapCSP5 = MapColoringCSP(v, d, c, lcv=True)
    assignment = backtracking_search(mapCSP5)
    print("MapColoringCSP Test 5: Australia (LCV Heuristic) Consistency Checks: "
          + str(mapCSP5.is_consistent_checks))
    print(mapCSP5.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    mapCSP6 = MapColoringCSP(v, d, c, lcv=True, mrv=True)
    assignment = backtracking_search(mapCSP6)
    print("MapColoringCSP Test 6: Australia (MRV + LCV Heuristic) Consistency Checks: "
          + str(mapCSP6.is_consistent_checks))
    print(mapCSP6.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    mapCSP7 = MapColoringCSP(v, d, c, lcv=True, degree=True)
    assignment = backtracking_search(mapCSP7)
    print("MapColoringCSP Test 7: Australia (Degree + LCV Heuristic) Consistency Checks: "
          + str(mapCSP7.is_consistent_checks))
    print(mapCSP7.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    # Now with inferences AC-3
    mapCSP8 = MapColoringCSP(v, d, c, inference=True)
    assignment = backtracking_search(mapCSP8)
    print("MapColoringCSP Test 8: Australia (Arc Consistency) Consistency Checks: "
          + str(mapCSP8.is_consistent_checks))
    print(mapCSP8.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    # Now with inferences AC-3
    mapCSP9 = MapColoringCSP(v, d, c, inference=True, lcv=True)
    assignment = backtracking_search(mapCSP9)
    print("MapColoringCSP Test 9: Australia (LCV + Arc Consistency) Consistency Checks: "
          + str(mapCSP9.is_consistent_checks))
    print(mapCSP9.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')

    # Now with inferences AC-3
    mapCSP10 = MapColoringCSP(v, d, c, inference=True, lcv=True, mrv=True)
    assignment = backtracking_search(mapCSP10)
    print("MapColoringCSP Test 10: Australia (MRV + LCV + Arc Consistency) Consistency Checks: "
          + str(mapCSP10.is_consistent_checks))
    print(mapCSP10.print_assignment(assignment, var_dictionary, value_dictionary) + '\n')
