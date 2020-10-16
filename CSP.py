# CS 76: Artificial Intelligence - PA4:CSP
# Authors: Sudharsan Balasubramani & Alberto
# Collaborated with: James Fleming

# Houses the algorithms for CSP

def backtracking_search(csp):
    return backtrack({}, csp)


def backtrack(assignment, csp):
    # Increment num of backtrack calls
    csp.backtrack_calls += 1
    # First check if this is a complete assignment, then return the assignment
    if is_complete_assignment(assignment, csp):
        return assignment

    # if not, then choose an unassigned variable
    var = select_unassigned_variable(csp, assignment)

    # Then for all values in the domain of that variable, try to find a solution. If inconsistency is detected, then
    # that is a failure, so we move back to try another value
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(csp, value, assignment, var):
            # If we are consistent, then add to our assignment
            add_to_assignment(assignment, var, value, csp)
            if csp.inference:
                inf_bool, inferences = inference(csp, assignment)
                if inf_bool:
                    # add inferences to assignment if you found more assignments
                    if is_complete_assignment(assignment, csp):
                        return assignment
                    result = backtrack(assignment, csp)
                    # if result returns something at all, return it
                    if result is not None:
                        return result
                remove_from_assignment(assignment, var, value, csp, inferences)
            else:
                result = backtrack(assignment, csp)
                # if result returns something at all, return it
                if result is not None:
                    return result
                remove_from_assignment(assignment, var, value, csp)

    return None


# Returns whether the assignment is a complete assignment
def is_complete_assignment(assignment, csp):
    return len(assignment) == len(csp.variables)


# Checks whether the current assignment is consistent with the constraints of the problem
def is_consistent(csp, value, assignment, var):
    # loop through the constraints
    for key in assignment.keys():
        key_value = assignment[key]

        # We have to be careful about the order we store them in so we can find the specific key in the dictionary as a
        # tuple. Thought about using sets as keys but sets are mutable.
        if key < var:
            key_constraint = (key, var)
            val = (key_value, value)
        else:
            key_constraint = (var, key)
            val = (value, key_value)

        if key_constraint in csp.constraints.keys() and val not in csp.constraints[key_constraint]:
            return False

    return True


# Selects an unassigned variable from the CSP
def select_unassigned_variable(csp, assignment):
    # If we are using the minimum remaining values heuristic, then we want to select var with the least remaining values
    if csp.mrv:
        # Get the maximum domain length
        min_domain = csp.max_domain_len
        variable_to_return = None
        for variable in csp.variables:
            if variable not in assignment and len(csp.working_domains[variable]) <= min_domain:
                variable_to_return = variable
                min_domain = len(csp.working_domains[variable])
        return variable_to_return

    # If we are using the degree heuristic, then we want var with highest degree
    elif csp.degree:
        min_degree = 0
        variable_to_return = None
        for variable in csp.variables:
            if variable not in assignment and csp.degree_dictionary[variable] >= min_degree:
                min_degree = csp.degree_dictionary[variable]
                variable_to_return = variable
        return variable_to_return

    # Selects a random variable to assign
    else:
        for variable in csp.variables:
            if variable not in assignment:
                return variable


# Orders the domain values based on heuristic if heuristic is provided.
def order_domain_values(var, assignment, csp):

    # If using the least constraining value heuristic, then we have to order in a way such that the value that is
    # is selected is the variable that will constrain others the least.
    def lcv_func(value):
        num_constraining = 0
        for neighbor in neighbors:
            if value in csp.working_domains[neighbor]:
                num_constraining += 1
        return num_constraining

    if csp.lcv:
        neighbors = csp.neighbors[var]
        csp.working_domains[var].sort(key=lcv_func)

    return csp.working_domains[var]


# Adds to our assignment, decreases our domains
def add_to_assignment(assignment, var, value, csp):
    assignment[var] = value
    # Set the working domains values to just a singular value
    csp.working_domains[var] = [value]


# Remove from assignment, reset the domain of the var
def remove_from_assignment(assignment, var, value, csp, inferences=None):
    # Delete the assignment
    del assignment[var]
    # Reset domain
    csp.working_domains[var] = csp.domains[var]

    # Delete inferences
    if inferences:
        for key in inferences:
            del assignment[key]
            csp.working_domains[var] = csp.domains[var]


# inferences via arc consistency. Will check if we can manipulate the domain and if so, return a list of additions where
# the domain is just one.
def inference(csp, assignment):
    # The AC-3 algorithm
    # Initial queue of arcs
    arc_queue = csp.arcs.copy()

    # While the queue is not empty
    while len(arc_queue) != 0:
        (xi, xj) = arc_queue.pop(0)
        if revise(csp, xi, xj):
            # If our len of domain is 0, then it is a failure
            if len(csp.working_domains[xi]) == 0:
                return False, None
            arc_queue.extend(csp.get_arcs(xi))
    # Create an inference list to possibly delete later
    inference_list = []
    for key in csp.working_domains.keys():
        if key not in assignment and len(csp.working_domains[key]) == 1:
            assignment[key] = csp.working_domains[key][0]
            inference_list.append(key)
    if not inference_list:
        inference_list = None
    return True, inference_list


# Revise returns true iff we revise the domain of xi
def revise(csp, xi, xj):
    key_constraint = (min(xi, xj), max(xi, xj))
    revised = False
    for x in csp.working_domains[xi]:
        satisfy = False
        for y in csp.working_domains[xj]:
            if key_constraint[0] == xi:
                tuple_to_check = (x, y)
            else:
                tuple_to_check = (y, x)
            if tuple_to_check in csp.constraints[key_constraint]:
                satisfy = True
                break
        if not satisfy:
            csp.working_domains[xi].remove(x)
            revised = True
    return revised






