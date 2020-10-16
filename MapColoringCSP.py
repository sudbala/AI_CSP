# CS 76: Artificial Intelligence - PA4:CSP
# Authors: Sudharsan Balasubramani & Alberto
# Collaborated with: James Fleming

import copy


# Class that handles the Map-coloring constraint-satisfaction problem.
class MapColoringCSP:

    # Constructor for the Map Coloring CSP. Accepts a set of Vars, Domains, and Implicit Constraints
    # These implicit constraints will be turned into explicit later on
    def __init__(self, variables, domains, constraints, mrv=False, degree=False, lcv=False, inference=False):
        # initialize all variables
        self.variables = variables
        self.domains = copy.deepcopy(domains)
        self.working_domains = copy.deepcopy(domains)
        self.implicit_constraints = constraints
        self.constraints = self.generate_explicit_constraints(constraints)

        # Heuristics
        self.mrv = mrv
        self.lcv = lcv
        self.neighbors = self.get_neighbors()
        self.degree = degree
        if self.degree:
            self.degree_dictionary = self.get_degrees()

        self.inference = inference
        if self.inference:
            self.arcs = self.generate_arcs()
        self.backtrack_calls = 0
        self.max_domain_len = self.max_domain_len()

    # Generates the explicit constraints. For example, if SA does not equal Queensland, we generate all the
    # possible options that this pair could take on.
    def generate_explicit_constraints(self, constraints):
        explicit_constraints = {}
        # For a given tuple of explicit constraints, generate the explicit constraints associated with
        for constraint in constraints:
            # Tuples have to be in order so that we don't mix up the relation between 0,1 and 1,0
            # These are just variable number indices
            min_var = min(constraint[0], constraint[1])
            max_var = max(constraint[0], constraint[1])
            constraint_key = (min_var, max_var)

            # Set the constraints for this key to be a list
            explicit_constraints[constraint_key] = list()

            # Now, generate a bunch of explicit constraints
            for color_min in self.domains[min_var]:
                for color_max in self.domains[max_var]:
                    if color_min != color_max:
                        explicit_constraints[constraint_key].append((color_min, color_max))
        # Return this new constraint dictionary
        return explicit_constraints

    # For the degree heuristic, create a dictionary of degrees
    def get_degrees(self):
        degree_dictionary = dict.fromkeys(range(len(self.variables)), 0)
        for constraint in self.implicit_constraints:
            degree_dictionary[constraint[0]] += 1
            degree_dictionary[constraint[1]] += 1
        return degree_dictionary

    # For LCV, create a dictionary of neighbors
    def get_neighbors(self):
        neighbor_dictionary = {x: set() for x in range(len(self.variables))}
        for constraint in self.implicit_constraints:
            neighbor_dictionary[constraint[0]].add(constraint[1])
            neighbor_dictionary[constraint[1]].add(constraint[0])
        return neighbor_dictionary

    # For Arc Consistency, arc generation
    def generate_arcs(self):
        arcs = []
        for key in self.neighbors.keys():
            arcs.extend(self.get_arcs(key))
        return arcs

    def get_arcs(self, key):
        key_arcs = []
        for neighbor in self.neighbors[key]:
            key_arcs.append((neighbor, key))
        return key_arcs

    # Returns the maximum length of domain to use for mrv
    def max_domain_len(self):
        max_len = 0
        for key in self.domains.keys():
            max_len = max(max_len, len(self.domains[key]))
        return max_len


# A bit of test code. You might want to add to it to verify that things
#  work as expected.
if __name__ == "__main__":

    # Making a MapColoringCSP
    # Variables: WA = 0, NT = 1, Q = 2, NSW = 3, V = 4, SA = 5, T = 6
    # Domains: R = 0, G = 1, B = 2
    # Constraints: (0,1) means that WA cannot be same color as NT
    v = [0, 1, 2, 3, 4, 5, 6]
    d = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2], 5: [0, 1, 2], 6: [0, 1, 2]}
    c = [(0, 1), (0, 5), (1, 2), (1, 5), (2, 3), (2, 5), (3, 5), (3, 4), (4, 5)]

    # Now we create a MapColoringCSP. Fingers crossed this works
    mapCSP = MapColoringCSP(v, d, c, False)
    print(mapCSP.constraints)
