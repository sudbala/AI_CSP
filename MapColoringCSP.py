# CS 76: Artificial Intelligence - PA4:CSP
# Authors: Sudharsan Balasubramani & Alberto
# Collaborated with: James Fleming

# Import general CSP class to inherit.
from GeneralCSP import GeneralCSP


# Class that handles the Map-coloring constraint-satisfaction problem.
class MapColoringCSP(GeneralCSP):

    # Constructor for the Map Coloring CSP. Accepts a set of Vars, Domains, and Implicit Constraints
    # These implicit constraints will be turned into explicit later on. Inherits the super constructor but
    # generates its own explicit constraints based on the type of problem it is.
    def __init__(self, variables, domains, constraints, mrv=False, degree=False, lcv=False, inference=False):

        super().__init__(variables, domains, constraints, mrv, degree, lcv, inference)
        self.constraints = self.generate_explicit_constraints(constraints)

    # Generates the explicit constraints. For example, if SA does not equal Queensland, we generate all the
    # possible options that this pair could take on.
    def generate_explicit_constraints(self, constraints):
        explicit_constraints = {}
        # For a given tuple of implicit constraints, generate the explicit constraints associated with
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

    # Print out the colors associated in assignment
    def print_assignment(self, assignment, var_dictionary, value_dictionary):
        return_string = ''
        for key in assignment.keys():
            return_string += var_dictionary[key] + ':' + value_dictionary[assignment[key]] + ' '
        return return_string


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

    # Now we create a MapColoringCSP. Fingers crossed this works. Test if constraint generation works.
    mapCSP = MapColoringCSP(v, d, c, False)
    print(mapCSP.constraints)
