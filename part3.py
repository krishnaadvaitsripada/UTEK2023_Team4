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
        
        source, target_with_cost = edge.split("->")
        target, cost_with_cooldown = target_with_cost.split("($")
        cost, cooldown = cost_with_cooldown.split(",")
        cost = int(cost[:])
        cooldown = cooldown.replace("mincooldown", "")
        if ')' in cooldown:
            cooldown = cooldown[:-1]
        cooldown = int(cooldown[:])  
        
        assert matrix_cost[source][target] == 1
        
        matrix_cost[source][target] = cost
        matrix_time[source][target] = cooldown

def dijkstra_algorithm(matrix, source):
    num_intersections = len(matrix)

    lowest_costs = {}
    for inter in matrix.keys():
        lowest_costs[inter] = float('inf')
    lowest_costs[source] = 0

    visited_inter = {}
    for inter in matrix.keys():
        visited_inter[inter] = False

    best_path = {}

    for _ in range(num_intersections - 1):
        curr_source = -1

        for inter in matrix.keys():
            if not visited_inter[inter]:
                if (curr_source == -1 or lowest_costs[inter] < lowest_costs[curr_source]):
                    curr_source = inter

        visited_inter[curr_source] = True

        for curr_target in matrix.keys():
            if matrix[curr_source][curr_target] != 0 and not visited_inter[curr_target]:
                new_distance = lowest_costs[curr_source] + matrix[curr_source][curr_target]
                if new_distance < lowest_costs[curr_target]:
                    lowest_costs[curr_target] = min(lowest_costs[curr_target], new_distance)
                    best_path[curr_target] = curr_source
                
    return lowest_costs, best_path

def find_optimal_path_part3(start_inter, end_inter, max_time, input_string):
    filtered_str = re.sub(r'\(\$[0-9]+, [0-9]+ min cooldown\)', '', input_string)
    matrix_cost = adjacency_list_to_matrix(filtered_str)
    matrix_time = copy.deepcopy(matrix_cost)


    parse_input_string_part3(matrix_cost, matrix_time, input_string)

    best_path, best_cost = tsp_part3(matrix_cost, matrix_time, start_inter, end_inter, max_time)
    return best_cost, best_path

s2 = "a->b ($4, 1 min cooldown) , b->c ($5, 1 min cooldown) , c->d ($3, 3 min cooldown) , b->d ($7, 3 min" +\
" cooldown), a->c ($4, 3 min cooldown), d->a ($1, 4 min cooldown)"

a, b = find_optimal_path_part3('a', 'd', 5, s2)
print(a,b)