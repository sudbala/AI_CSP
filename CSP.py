# CS 76: Artificial Intelligence - PA4:CSP
# Authors: Sudharsan Balasubramani & Alberto
# Collaborated with: James Fleming

# Houses the algorithms for CSP

def backtracking_search(csp):
    return backtrack({}, csp)


def backtrack(self, assignment, csp):
    # First check if this is a complete assignment, then return the assignment
    if is_complete_assignment(assignment):
        return assignment

    # if not, then choose an unassigned variable
    var = select_unassigned_variable(csp)

    # Then for all values in the domain of that variable, try to find a solution. If inconsistency is detected, then
    # that is a failure, so we move back to try another value
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(csp, value, assignment):
            # If we are consistent, then add to our assignment
            assignment[var] = value
            if csp.inference:
                inferences = inference(csp, var, value)
                if inferences is not None:
                    # add inferences to assignment if you found more assignments
                    add_inferences(inferences, assignment)
                    result = backtrack(assignment, csp)
                    # if result returns something at all, return it
                    if result is not None:
                        return result
            else:
                result = backtrack(assignment, csp)
                # if result returns something at all, return it
                if result is not None:
                    return result
        del assignment[var]
    return None


# Returns whether the assignment is a complete assignment
def is_complete_assignment(assignment, csp):
    return len(assignment) == csp.variables

# Checks whether the current assignment is consistent with the constraints of the problem
def is_consistent(csp, value, assignment, var):
    # loop through the constraints
    for constraint



# Selects an unassigned variable from the CSP
def select_unassigned_variable(csp, assignment):
    # Selects a random variable to assign
    for variable in csp.variables:
        if variable not in assignment:
            return variable


# Orders the domain values based on heuristic if heuristic is provided.
def order_domain_values(var, assignment, csp):
    # for now, just return values associated with var
    return csp.domains[var]


# inferences via arc consistency. Will check if we can manipulate the domain and if so, return a list of additions where
# the domain is just one.
def inference(csp, var, value):
    pass


# Adds inferences to assigment
def add_inferences(inferences, assignment):
    for tuple_assignment in inferences:
        assignment[tuple_assignment(1)] = tuple_assignment(2)






