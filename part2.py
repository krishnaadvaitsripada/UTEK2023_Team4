import re

def tsp(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    memo = {}

    def tsp_helper(mask, pos):
        if mask == (1 << n) - 1:
            cost = graph[nodes[pos]].get(nodes[0], float('inf'))
            return cost, [nodes[pos]] if cost != float('inf') else []

        if (mask, pos) in memo:
            return memo[(mask, pos)]

        best_cost = float('inf')
        best_path = []

        for next_pos in range(n):
            if (mask >> next_pos) & 1 == 0 and nodes[next_pos] in graph[nodes[pos]] and graph[nodes[pos]][nodes[next_pos]] > 0:
                new_mask = mask | (1 << next_pos)
                cost, path = tsp_helper(new_mask, next_pos)
                total_cost = graph[nodes[pos]][nodes[next_pos]] + cost

                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = [nodes[pos]] + path

        memo[(mask, pos)] = (best_cost, best_path)
        return best_cost, best_path

    # Start from node 'a' (assuming 'a' is in the graph)
    start_node = 'a'
    start_pos = nodes.index(start_node)
    _, optimal_path = tsp_helper(1 << start_pos, start_pos)

    return optimal_path

from part2 import parse_input_string
from part1 import adjacency_list_to_matrix

input_str = "a->b ($4), b->c ($5), c->d ($3), d->b ($4), a->c ($4), d->a ($1)"
filtered_str = re.sub(r'\(\$[0-9]+\)', '', input_str)
adjacency_dict = adjacency_list_to_matrix(filtered_str)

parse_input_string(adjacency_dict, input_str)
print(adjacency_dict)

# Example usage with your adjacency dictionary

def calc_cost(path):
    cost = 0
    for i in range(0, len(path)-1):
        cost += adjacency_dict[path[i]][path[i+1]]
    return cost

optimal_path = tsp(adjacency_dict)
print("Optimal Cost:", calc_cost(optimal_path))
print("Optimal Path:", optimal_path)