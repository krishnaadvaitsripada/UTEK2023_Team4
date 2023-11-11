import re

def tsp(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    memo = {}

    def tsp_helper(mask, pos, end_node):
        if mask == (1 << n) - 1:
            if nodes[pos] == end_node:
                cost = 0
                return cost, [nodes[pos]]
            else:
                cost = graph[nodes[pos]].get(end_node, float('inf'))
                return cost, [nodes[pos]] if cost != float('inf') else []

        if (mask, pos) in memo:
            return memo[(mask, pos)]

        best_cost = float('inf')
        best_path = []

        for next_pos in range(n):
            if (mask >> next_pos) & 1 == 0 and nodes[next_pos] in graph[nodes[pos]] and graph[nodes[pos]][nodes[next_pos]] > 0:
                new_mask = mask | (1 << next_pos)
                cost, path = tsp_helper(new_mask, next_pos, end_node)
                total_cost = graph[nodes[pos]][nodes[next_pos]] + cost

                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = [nodes[pos]] + path

        memo[(mask, pos)] = (best_cost, best_path)
        return best_cost, best_path

    # Start from node 'a' (assuming 'a' is in the graph)
    start_node = 'a'
    end_node = 'c'
    start_pos = nodes.index(start_node)
    _, optimal_path = tsp_helper(1 << start_pos, start_pos, end_node)

    return optimal_path

from part1 import adjacency_list_to_matrix, display_adjacency_matrix

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

def calc_cost(matrix, path):
    cost = 0
    for i in range(0, len(path)-1):
        cost += matrix[path[i]][path[i+1]]
    return cost

def find_optimal_path(start_inter, end_inter, input_string):
    filtered_str = re.sub(r'\(\$[0-9]+\)', '', input_string)
    matrix = adjacency_list_to_matrix(filtered_str)

    parse_input_string(matrix, input_string)

    optimal_path = tsp(matrix)
    return calc_cost(matrix, optimal_path), optimal_path

input_str = "a->b ($4), b->c ($5), c->d ($3), d->b ($4), a->c ($4), d->a ($1)"
print(find_optimal_path('a', 'b', input_str))