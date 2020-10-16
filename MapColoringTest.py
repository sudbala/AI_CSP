
from MapColoringCSP import MapColoringCSP
from CSP import *


class MapColoringTest:
    # # Test class to try a few things to get everything working
    #
    # # Making a MapColoringCSP
    # # Variables: VT = 0, NH = 1, ME = 2, MA = 3
    # # Domains: R = 0, G = 1, B = 2
    # # Constraints: (0,1) means that WA cannot be same color as NT
    # v = [0, 1, 2, 3]
    # d = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2]}
    # c = [(0, 1), (0, 3), (1, 2), (1, 3)]
    #
    # # Now we create a MapColoringCSP. Fingers crossed this works
    # mapCSP = MapColoringCSP(v, d, c)
    # print(mapCSP.constraints)
    #
    # assignment = backtracking_search(mapCSP)
    # print(assignment)
    #
    # # Making a MapColoringCSP
    # # Variables: WA = 0, NT = 1, Q = 2, NSW = 3, V = 4, SA = 5, T = 6
    # # Domains: R = 0, G = 1, B = 2
    # # Constraints: (0,1) means that WA cannot be same color as NT
    # v = [0, 1, 2, 3, 4, 5, 6]
    # d = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2], 5: [0, 1, 2], 6: [0, 1, 2]}
    # c = [(0, 1), (0, 5), (1, 2), (1, 5), (2, 3), (3, 5), (3, 4)]
    #
    # # Now we create a MapColoringCSP. Fingers crossed this works
    # mapCSP = MapColoringCSP(v, d, c)
    # print(mapCSP.constraints)
    # print("Maximum Domain Length: " + str(mapCSP.max_domain_len))
    #
    # assignment = backtracking_search(mapCSP)
    # print("Number of Backtrack Calls: " + str(mapCSP.backtrack_calls))
    # print(assignment)

    # Making a MapColoringCSP
    # Variables: WA = 0, NT = 1, Q = 2, NSW = 3, V = 4, SA = 5, T = 6
    # Domains: R = 0, G = 1, B = 2
    # Constraints: (0,1) means that WA cannot be same color as NT
    v = [0, 1, 2, 3, 4, 5, 6]
    d = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2], 5: [0, 1, 2], 6: [0, 1, 2]}
    c = [(0, 1), (0, 5), (1, 2), (1, 5), (2, 3), (2, 5), (3, 5), (3, 4), (4, 5)]

    # # Now we create a MapColoringCSP. Fingers crossed this works
    # mapCSP = MapColoringCSP(v, d, c)
    # print("Maximum Domain Length: " + str(mapCSP.max_domain_len))
    #
    # assignment = backtracking_search(mapCSP)
    # print("Number of Backtrack Calls (No Heuristics): " + str(mapCSP.backtrack_calls))
    # print(assignment)
    #
    # mapCSP = MapColoringCSP(v, d, c, mrv=True)
    # assignment = backtracking_search(mapCSP)
    # print("Number of Backtrack Calls (MRV): " + str(mapCSP.backtrack_calls))
    # print(assignment)
    #
    # mapCSP = MapColoringCSP(v, d, c, degree=True)
    # assignment = backtracking_search(mapCSP)
    # print("Number of Backtrack Calls (Degree): " + str(mapCSP.backtrack_calls))
    # print(assignment)
    #
    # mapCSP = MapColoringCSP(v, d, c, lcv=True)
    # print(mapCSP.constraints)
    # print("Neighbor Lists: " + str(mapCSP.neighbors))
    # assignment = backtracking_search(mapCSP)
    # print("Number of Backtrack Calls (LCV): " + str(mapCSP.backtrack_calls))
    # print(assignment)

    mapCSP2 = MapColoringCSP(v, d, c, inference=True, lcv=True)
    assignment = backtracking_search(mapCSP2)
    print("Number of Backtrack Calls (Inferences, MRV, LCV): " + str(mapCSP2.backtrack_calls))
    print(assignment)
