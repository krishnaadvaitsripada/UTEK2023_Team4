"""
Optimal Path Finding

This part takes an input of intersections (with costs of edges), start intersection and end intersection
and finds an optimal path between the two given intersections
"""

import itertools
from part1 import remove_spaces, adjacency_list_to_matrix
import re

def parse_input_string(matrix, input_string):
    """
    Inputs: 
        matrix - Unweighted adjacency matrix (dict within a dict) 
        input_string - Adjacency list with costs (e.g. )
    
    Returns:
        A weighted matrix (the weights being the costs from the input_string adjacency list)
    """

    input_string = remove_spaces(input_string)

    edges_with_cost = input_string.split(",")

    for edge in edges_with_cost:

        # Split each edge into the source, target and cost
        source, target_with_cost = edge.split("->")
        target, cost = target_with_cost.split("($")
        cost = int(cost[:-1])

        # The cost should initially be 1 in the matrix
        assert matrix[source][target] == 1
        
        # Update cost
        matrix[source][target] = cost
        
def tsp_with_constraints(adjacency_matrix, start_node, end_node):
    """
    Given an adjacency matrix (e.g. from Part 1), and a starting node and an ending node,
    it returns the optimal path (in terms of cost) that traverses through everything, alongside the total
    cost of the optimal path.

    If there is no optimal path, it returns None, with the total cost being Infinite. 
    """
    if start_node not in adjacency_matrix or end_node not in adjacency_matrix:
        raise ValueError("Start or end node not in the adjacency matrix.")

    # Check if start_node and end_node are different
    if start_node == end_node:
        raise ValueError("Start and end nodes must be different.")

    # Get the list of nodes from the keys of the matrix
    nodes = list(adjacency_matrix.keys())

    # Check if start_node and end_node are valid nodes
    if start_node not in nodes or end_node not in nodes:
        raise ValueError("Start or end node not in the list of nodes.")
    
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
        # Calculate the total cost for the current path
        cost = 0
        for i in range(len(path) - 1):
            cost += adjacency_matrix[path[i]][path[i+1]]
        
        # Update minimum cost and path if the current path is better
        if cost < min_cost:
            min_cost = cost
            min_path = path
    
    return min_path, min_cost

def find_optimal_path(input_str, start, end):
    # Remove the '($Number)' from the input string
    filtered_str = re.sub(r'\(\$[0-9]+\)', '', input_str) 

    # Make unweighted adjacency matrix
    matrix = adjacency_list_to_matrix(filtered_str)

    # Convert to weighted matrix
    parse_input_string(matrix, input_str)

    min_path, min_cost = tsp_with_constraints(matrix, start, end)

    return min_path, min_cost
