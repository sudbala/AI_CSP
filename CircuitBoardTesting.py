# CS 76: Artificial Intelligence - PA4:CSP
# Fall 2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaboration: Discussed ideas with James Fleming

# Import statements to bring in CSP solvers and CircuitBoard CSP
from CircuitBoardCSP import CircuitBoardCSP
from CSP import *


# Test class for CircuitBoard CSP
class CircuitBoardTesting:
    # Test class to try a few things to get everything working

    # Making a CircuitBoardCSP with provided Example
    # Variables: Component a: 0, Component b: 1, Component c: 2, Component e: 3
    # Domains: For a given component, all possible bottom left coordinates for component
    # Constraints: (0,1) means that component a cannot overlap with component b
    v = [0, 1, 2, 3]
    var_dictionary = {0: 'a', 1: 'b', 2: 'c', 3: 'e'}
    d = {0: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
             (5, 1), (6, 1), (7, 1)],
         1: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)],
         2: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)],
         3: [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 2), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2)]}
    c = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    dimensions = {0: (3, 2), 1: (5, 2), 2: (2, 3), 3: (7, 1), 'board': (10, 3)}

    circuit_board_csp = CircuitBoardCSP(v, d, c, dimensions)
    assignment = backtracking_search(circuit_board_csp)
    print("CircuitBoardCSP Test 1: Provided Example (No Heuristics) Consistency Checks: "
          + str(circuit_board_csp.is_consistent_checks))
    print(circuit_board_csp.print_assignment(assignment, var_dictionary) + "\n")

    # MRV
    circuit_board_csp2 = CircuitBoardCSP(v, d, c, dimensions, mrv=True)
    assignment = backtracking_search(circuit_board_csp2)
    print("CircuitBoardCSP Test 2: Provided Example (MRV Heuristic) Consistency Checks: "
          + str(circuit_board_csp2.is_consistent_checks))
    print(circuit_board_csp2.print_assignment(assignment, var_dictionary) + "\n")

    # Degree
    circuit_board_csp3 = CircuitBoardCSP(v, d, c, dimensions, degree=True)
    assignment = backtracking_search(circuit_board_csp3)
    print("CircuitBoardCSP Test 3: Provided Example (Degree Heuristic) Consistency Checks: "
          + str(circuit_board_csp3.is_consistent_checks))
    print(circuit_board_csp3.print_assignment(assignment, var_dictionary) + "\n")

    # LCV
    circuit_board_csp4 = CircuitBoardCSP(v, d, c, dimensions, lcv=True)
    assignment = backtracking_search(circuit_board_csp4)
    print("CircuitBoardCSP Test 4: Provided Example (LCV Heuristic) Consistency Checks: "
          + str(circuit_board_csp4.is_consistent_checks))
    print(circuit_board_csp4.print_assignment(assignment, var_dictionary) + "\n")

    # MRV + LCV
    circuit_board_csp5 = CircuitBoardCSP(v, d, c, dimensions, mrv=True, lcv=True)
    assignment = backtracking_search(circuit_board_csp5)
    print("CircuitBoardCSP Test 5: Provided Example (MRV + LCV Heuristic) Consistency Checks: "
          + str(circuit_board_csp5.is_consistent_checks))
    print(circuit_board_csp5.print_assignment(assignment, var_dictionary) + "\n")

    # Degree + LCV
    circuit_board_csp6 = CircuitBoardCSP(v, d, c, dimensions, degree=True, lcv=True)
    assignment = backtracking_search(circuit_board_csp6)
    print("CircuitBoardCSP Test 6: Provided Example (Degree + LCV Heuristic) Consistency Checks: "
          + str(circuit_board_csp6.is_consistent_checks))
    print(circuit_board_csp6.print_assignment(assignment, var_dictionary) + "\n")

    # Arc Consistency
    circuit_board_csp7 = CircuitBoardCSP(v, d, c, dimensions, inference=True)
    assignment = backtracking_search(circuit_board_csp7)
    print("CircuitBoardCSP Test 7: Provided Example (Arc Consistency) Consistency Checks: "
          + str(circuit_board_csp7.is_consistent_checks))
    print(circuit_board_csp7.print_assignment(assignment, var_dictionary) + "\n")

    # MRV + Arc Consistency
    circuit_board_csp8 = CircuitBoardCSP(v, d, c, dimensions, mrv=True, inference=True)
    assignment = backtracking_search(circuit_board_csp8)
    print("CircuitBoardCSP Test 8: Provided Example (MRV + Arc Consistency) Consistency Checks: "
          + str(circuit_board_csp8.is_consistent_checks))
    print(circuit_board_csp8.print_assignment(assignment, var_dictionary) + "\n")

    # Degree + Arc Consistency
    circuit_board_csp9 = CircuitBoardCSP(v, d, c, dimensions, degree=True, inference=True)
    assignment = backtracking_search(circuit_board_csp9)
    print("CircuitBoardCSP Test 9: Provided Example (Degree + Arc Consistency) Consistency Checks: "
          + str(circuit_board_csp9.is_consistent_checks))
    print(circuit_board_csp9.print_assignment(assignment, var_dictionary) + "\n")

    # MRV + LCV + Arc Consistency
    circuit_board_csp10 = CircuitBoardCSP(v, d, c, dimensions, mrv=True, lcv=True, inference=True)
    assignment = backtracking_search(circuit_board_csp10)
    print("CircuitBoardCSP Test 10: Provided Example (MRV + LCV + Arc Consistency) Consistency Checks: "
          + str(circuit_board_csp10.is_consistent_checks))
    print(circuit_board_csp10.print_assignment(assignment, var_dictionary) + "\n")
