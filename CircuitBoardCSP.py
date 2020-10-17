# CS 76: Artificial Intelligence - PA4:CSP
# Fall 2020
# Authors: Sudharsan Balasubramani & Alberto
# Collaboration: Discussed ideas with James Fleming

# Import General CSP to inherit from
from GeneralCSP import GeneralCSP


# CircuitBoardCSP very similar to any CSP, just the explicit constraints are a little different.
class CircuitBoardCSP(GeneralCSP):

    # Constructor for the Circuit Board CSP. Accepts a set of Vars, Domains, and Implicit Constraints
    # These implicit constraints will be turned into explicit later on. Inherits the General CSP constructor but
    # introduces its own explicit constraints and takes in dimensions to help
    def __init__(self, variables, domains, constraints, dimensions, mrv=False, degree=False, lcv=False, inference=False):
        super().__init__(variables, domains, constraints, mrv, degree, lcv, inference)
        self.dimensions = dimensions
        self.constraints = self.generate_explicit_constraints(self.implicit_constraints)

    # Generate our explicit constraints for the Circuit Board Problem
    def generate_explicit_constraints(self, constraints):
        explicit_constraints = {}

        # For a given tuple of implicit constraints, generate the associated explicit constraints
        for constraint in constraints:
            # Tuples have to be in order so that we don't mix up the relation between 0,1 and 1,0
            # These are just variable number indices
            min_var = min(constraint[0], constraint[1])
            max_var = max(constraint[0], constraint[1])
            constraint_key = (min_var, max_var)

            # Set the constraints for this key to be a list
            explicit_constraints[constraint_key] = list()

            # Now generate a bunch of explicit constraints
            for pos_min in self.domains[min_var]:
                for pos_max in self.domains[max_var]:
                    min_dx = self.dimensions[min_var][0]
                    min_dy = self.dimensions[min_var][1]
                    max_dx = self.dimensions[max_var][0]
                    max_dy = self.dimensions[max_var][0]
                    # Now we check if x and y fit
                    fits_y_constraint = pos_min[1] + min_dy <= pos_max[1] or pos_min[1] - max_dy >= pos_max[1]
                    fits_x_constraint = pos_min[0] + min_dx <= pos_max[0] or pos_min[0] - max_dx >= pos_max[0]
                    if fits_x_constraint or fits_y_constraint:
                        explicit_constraints[constraint_key].append((pos_min, pos_max))
        # Return this new constraint dictionary
        return explicit_constraints

    # Prints the circuit board assignment in ASCII
    def print_assignment(self, assignment, var_dictionary):
        # First generate the board
        board = [['.' for i in range(self.dimensions['board'][0])] for j in range(self.dimensions['board'][1])]

        # Flip the coordinates of the assignment so we can apply to 2d array
        for key in assignment.keys():
            assignment[key] = (assignment[key][1], assignment[key][0])
            for i in range(assignment[key][0], assignment[key][0] + self.dimensions[key][1]):
                for j in range(assignment[key][1], assignment[key][1] + self.dimensions[key][0]):
                    board[i][j] = var_dictionary[key]
        return_string = ""

        for j in range(self.dimensions['board'][1]):
            return_string = str(board[j]) + "\n" + return_string
        return return_string
