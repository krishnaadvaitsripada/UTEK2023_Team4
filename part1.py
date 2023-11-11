"""
Graph Construction

This part takes an input of intersections, and organizes it an adjacency matrix fashion
"""

def remove_spaces(input_string):
    """
    Removes all spaces from input_string
    """
    return input_string.replace(" ", "")

def adjacency_list_to_matrix(adj_list):
    """
    Returns the adjacency matrix for the graph in the input string
    """
    adj_list = adj_list.split(',') # Obtain the individual node pairs

    intersections = []
    intersection_pairs = []
    
    # Extract the intersections and the intersection pairs
    for intersection_pair in adj_list:
        intersection_pair = intersection_pair.split("->")
        if len(intersection_pair) == 2:
            intersection_pairs.append(intersection_pair)
            for intersection in intersection_pair:
                intersections.append(intersection.strip())
    
    intersections = set(intersections) # Remove duplicates
    matrix = {}
    
    # Create an empty 2D matrix
    for intersection in intersections:
        matrix[intersection] = {}

    # Fill all the matrix values with infinity
    for intersection_i in intersections:
        for intersection_j in intersections:
            matrix[intersection_i][intersection_j] = float('inf')
    
    # Fill in the cells with '1' for the 'from' and 'to' nodes in the graph
    for intersection_pair in intersection_pairs: 
        matrix[intersection_pair[0].strip()][intersection_pair[1].strip()] = 1
    
    return matrix
        
def display_adjacency_matrix(adjacency_matrix):
    """
    Print the adjacency matrix in organized fashion
    """
    headers = list(adjacency_matrix.keys())
    max_header_length = max(len(header) for header in headers)

    # Find max_number_length
    max_number_length = max(
        max(len(str(value)) for value in row.values()) for row in adjacency_matrix.values()
    )

    # Determine the overall maximum length between headers and numbers
    max_combined_length = max(max_header_length, max_number_length)

    # Print headers
    print(f"{' ' * (max_combined_length + 1)}|", end="")
    for header in headers:
        print(f" {header.rjust(max_combined_length)} |", end="")
    print("\n" + "-" * (max_combined_length + 2) + "+---" * len(headers))

    # Print matrix
    for row in headers:
        print(f"{row.ljust(max_combined_length)} |", end="")
        for col in headers:
            print(f" {adjacency_matrix[row][col]:>{max_combined_length}} |", end="")
        print()

