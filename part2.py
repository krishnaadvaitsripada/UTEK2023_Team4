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
    lowest_costs = [float('inf')] * num_intersections
    lowest_costs[source] = 0
    visited_inter = [False] * num_intersections
    prev_inter = [-1] * num_intersections

    for _ in range(num_intersections - 1):
        curr_source = -1

        for inter in range(num_intersections):
            if not visited_inter[inter]:
                if (curr_source == -1 or lowest_costs[inter] < lowest_costs[curr_source]):
                    curr_source = inter

        visited_inter[curr_source] = True

        for curr_target in range(num_intersections):
            if matrix[curr_source][curr_target] != 0 and not visited_inter[curr_target]:
                new_distance = lowest_costs[curr_source] + matrix[curr_source][curr_target]
                if new_distance < lowest_costs[curr_target]:
                    lowest_costs[curr_target] = min(lowest_costs[curr_target], new_distance)
                    prev_inter[curr_target] = curr_source
                
    return lowest_costs, prev_inter

def visited_intersectionsd_optimal_path(matrix, start_inter, end_inter, input_string):
    parse_input_string(matrix, input_string)
    lowest_costs, prev_inter = dijkstra_algorithm(matrix, start_inter)
    
