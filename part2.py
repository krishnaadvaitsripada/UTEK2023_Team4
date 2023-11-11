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


def find_optimal_path(matrix, start_intersection, end_intersection, input_string):
    parse_input_string(matrix, input_string)