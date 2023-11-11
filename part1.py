"""
Graph Construction

This part takes an input of intersections, and organizes it an adjacency matrix fashion
"""

def remove_spaces(input_string):
    return input_string.replace(" ", "")

def adjacency_list_to_matrix(adj_list):
    adj_list = adj_list.split(',')
    intersections = []
    intersection_pairs = []
    for intersection_pair in adj_list:
        intersection_pair = intersection_pair.split("->")
        if len(intersection_pair) == 2:
            intersection_pairs.append(intersection_pair)
            for intersection in intersection_pair:
                intersections.append(intersection.strip())
    
    intersections = set(intersections) # Remove duplicates
    matrix = {}
    for intersection in intersections:
        matrix[intersection] = {}

    for intersection_i in intersections:
        for intersection_j in intersections:
            matrix[intersection_i][intersection_j] = 0
    
    for intersection_pair in intersection_pairs: 
        matrix[intersection_pair[0].strip()][intersection_pair[1].strip()] = 1
    
    return matrix
        
def display_adjacency_matrix(adjacency_matrix):
    headers = list(adjacency_matrix.keys())
    max_header_length = max(len(header) for header in headers)

    # Print headers
    print(f"{' ' * (max_header_length + 2)}|", end="")
    for header in headers:
        print(f" {header} |", end="")
    print("\n" + "-" * (max_header_length + 2) + "+---" * len(headers))

    # Print matrix
    for row in headers:
        print(f"{row} {' ' * (max_header_length - len(row))} |", end="")
        for col in headers:
            print(f" {adjacency_matrix[row][col]} |", end="")
        print()

# matrix_1 = adjacency_list_to_matrix("a->b, b->c, c->d, d->b")
# display_adjacency_matrix(matrix_1)

matrix_2 = adjacency_list_to_matrix("e->fn, dx->abc, dx->e,")
display_adjacency_matrix(matrix_2)
