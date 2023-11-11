"""
Graph Construction

This part takes an input of intersections, and organizes it an adjacency matrix fashion
"""



def adjacency_list_to_matrix(adj_list):
    adj_list = adj_list.split(',')
    intersections = []
    intersection_pairs = []
    for intersection_pair in adj_list:
        intersection_pair = intersection_pair.split("->")
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
    headers = list(sorted((adjacency_matrix.keys())))

    print("  |", end="")
    for header in headers:
        print(f" {header} |", end="")
    print()

    print("--+" + "---+" * len(headers))

    for row in headers:
        print(f"{row} |", end="")
        for col in headers:
            print(f" {adjacency_matrix[row][col]} |", end="")
        print()




# matrix = adjacency_list_to_matrix("a->b, b->c, c->d, d->b")
# display_adjacency_matrix(matrix)
