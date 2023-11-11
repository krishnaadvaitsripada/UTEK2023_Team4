import part1
import part2
import re
import copy

def remove_spaces(input_string):
    return input_string.replace(" ", "")

def parse_input_string_v3(matrixCosts, matrixCooldowns, input_string):
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

        assert matrixCosts[source][target] == 1
        
        matrixCosts[source][target] = cost
        matrixCooldowns[source][target] = cooldown

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

def dijkstra_modified(matrix, cooldowns, source):
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
            if cooldowns[inter] == -1:
                continue
            if not visited_inter[inter]:
                if (curr_source == -1 or lowest_costs[inter] < lowest_costs[curr_source]):
                    curr_source = inter

        visited_inter[curr_source] = True

        for curr_target in matrix.keys():
            if cooldowns[curr_target] == -1 or curr_source == -1:
                continue
            if matrix[curr_source][curr_target] != 0 and not visited_inter[curr_target]:
                new_distance = lowest_costs[curr_source] + matrix[curr_source][curr_target]
                if new_distance < lowest_costs[curr_target]:
                    lowest_costs[curr_target] = min(lowest_costs[curr_target], new_distance)
                    best_path[curr_target] = curr_source
                
    return lowest_costs, best_path

def find_optimal_path_v3(start_inter, end_inter, max_time, input_string):
    filtered_str = re.sub(r'\(\$[0-9]+, [0-9]+ min cooldown\)', '', input_string)
    matrix_costs = part1.adjacency_list_to_matrix(filtered_str)
    matrix_cooldowns = copy.deepcopy(matrix_costs)

    parse_input_string_v3(matrix_costs, matrix_cooldowns, input_string)

    smallest_cooldowns = {}
    smallest_costs = {}
    best_paths_cool = {}
    best_paths_cost = {}
    for source in matrix_cooldowns.keys():
        smallest_cooldowns[source], best_paths_cool[source] = dijkstra_algorithm(matrix_cooldowns, source)

    for source in smallest_cooldowns.keys():
        for target in smallest_cooldowns[source].keys():
            if smallest_cooldowns[source][target] > max_time:
                smallest_cooldowns[source][target] = -1
            else:
                smallest_cooldowns[source][target] = matrix_costs[source][target]
                

    for source in matrix_costs.keys():
        smallest_costs[source], best_paths_cost[source] = dijkstra_modified(smallest_cooldowns, smallest_cooldowns[source], source)

    for source in smallest_cooldowns.keys():
        for target in smallest_cooldowns[source].keys():
            smallest_cooldowns[source][target] = smallest_costs[source][target]

    return smallest_cooldowns, smallest_costs



s2 = "a->b ($4, 1 min cooldown) , b->c ($5, 1 min cooldown) , c->d ($3, 3 min cooldown) , b->d ($7, 3 min" +\
" cooldown), a->c ($4, 3 min cooldown), d->a ($1, 4 min cooldown)"

a, b = find_optimal_path_v3('a', 'b', 5, s2)
part1.display_adjacency_matrix(a)
