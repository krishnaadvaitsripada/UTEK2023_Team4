"""
Optimal Path Finding with Time Constraint

This part takes an input of intersections (with costs of edges and cooldown time), start intersection,
end intersection, max time limit
and finds an optimal path between the two given intersections which has a cooldown time less than max limit
"""

from part1 import adjacency_list_to_matrix, remove_spaces
import re
import copy
import itertools

def tsp_part3(costs, times, start_node, end_node, max_time):
    # Get the list of nodes from the keys of the matrix
    nodes = list(costs.keys())
    
    # Generate all possible permutations of nodes excluding start and end nodes
    nodes.remove(start_node)
    nodes.remove(end_node)
    permutations = itertools.permutations(nodes)
    
    # Add start and end nodes to the permutations
    permutations = [(start_node,) + path + (end_node,) for path in permutations]
    
    # Initialize variables to store the minimum cost and corresponding path
    min_cost = float('inf')
    min_path = None
    
    # Iterate through all permutations
    for path in permutations:
        # Calculate the total cost and time for the current path
        cost = 0
        time = 0
        for i in range(len(path) - 1):
            cost += costs[path[i]][path[i+1]]
            time += times[path[i]][path[i+1]]  # Assuming time is stored in the adjacency_matrix
        
        # Check if the current path satisfies the time constraint
        if time <= max_time:
            # Update minimum cost and path if the current path is better
            if cost < min_cost:
                min_cost = cost
                min_path = path
    
    return min_path, min_cost


def parse_input_string_part3(matrix_cost, matrix_time, input_string):
    input_string = remove_spaces(input_string)

    edges_with_cost = input_string.split("),")

    for edge in edges_with_cost:
        
        # Find source node, target node, cost and cooldown time
        source, target_with_cost = edge.split("->")
        target, cost_with_cooldown = target_with_cost.split("($")
        cost, cooldown = cost_with_cooldown.split(",")
        cost = int(cost[:])
        cooldown = cooldown.replace("mincooldown", "")
        if ')' in cooldown:
            cooldown = cooldown[:-1]
        cooldown = int(cooldown[:])  
        
        assert matrix_cost[source][target] == 1
        
        # Update matrix_cost and matrix_cost -- both are 2d dicts holding cost and cooldown values respectively
        matrix_cost[source][target] = cost
        matrix_time[source][target] = cooldown

def find_optimal_path_part3(start_inter, end_inter, max_time, input_string):
    # Remove everything but the intersection pair from the string
    filtered_str = re.sub(r'\(\$[0-9]+, [0-9]+ min cooldown\)', '', input_string)

    # Unweighted adjacency matrices
    matrix_cost = adjacency_list_to_matrix(filtered_str)
    # Deepcopy so modifying one matrix doesn't impact the other
    matrix_time = copy.deepcopy(matrix_cost)

    # Update the above two matrices to be weighted
    parse_input_string_part3(matrix_cost, matrix_time, input_string)

    # Find the best possible cost and path given start intersection, end intersection and max time
    best_path, best_cost = tsp_part3(matrix_cost, matrix_time, start_inter, end_inter, max_time)
    return best_cost, best_path