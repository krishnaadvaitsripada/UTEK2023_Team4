import part1
import re

def remove_spaces(input_string):
    return input_string.replace(" ", "")

def parse_input_string(matrix, input_string):
    input_string = remove_spaces(input_string)

    edges_with_cost = input_string.split(",")

    for edge in edges_with_cost:
        
        source, target_with_cost = edge.split("->")
        target, cost = target_with_cost.split("($")
        cost = int(cost[:-1])  

        assert matrix[source][target] == 1
        
        matrix[source][target] = cost

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

def find_optimal_path(start_inter, end_inter, input_string):
    filtered_str = re.sub(r'\(\$[0-9]+\)', '', input_string)
    matrix = part1.adjacency_list_to_matrix(filtered_str)

    parse_input_string(matrix, input_string)

    smallest_costs = {}
    best_paths = {}
    for source in matrix.keys():
        smallest_costs[source], best_paths[source] = dijkstra_algorithm(matrix, source)
    return smallest_costs, best_paths

s2 = "a->b ($4), b->c ($5), c->d ($3), d->b ($7), a->c ($4), d->a ($1)"
a, b = find_optimal_path('a', 'b', s2)