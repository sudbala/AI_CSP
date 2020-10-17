# CS 76: Artificial Intelligence - PA4:CSP
# Fall 2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaboration: Discussed ideas with James Fleming

# Import statements. Copy imported to deepcopy the domain dictionary.
import copy


# Class that handles the general CSP that MapColoring and CircuitBoard inherit.
class GeneralCSP:

    def __init__(self, variables, domains, constraints, mrv=False, degree=False, lcv=False, inference=False):
        # initialize all variables. Deep copy the dictionaries so that they don't point to same dictionary
        self.variables = variables
        self.domains = copy.deepcopy(domains)
        self.working_domains = copy.deepcopy(domains)
        self.implicit_constraints = constraints

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
        self.is_consistent_checks = 0
        self.max_domain_len = self.max_domain_len()

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

    # Helper to get arcs of just one key. Simply gets all the neighbors to a given key
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
