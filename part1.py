"""
Graph Construction

This part takes an input of intersections, and organizes it an adjacency matrix fashion
"""

from random import sample


def adjacency_list_to_matrix(adj_list):
    adj_list = adj_list.split(',')
    intersections = []
    for intersection_pair in adj_list:
        for intersection in intersection_pair.split("->"):
            intersections.append(intersection.strip())
    
    intersections = set(intersections) # Remove duplicates
    print(intersections)




adjacency_list_to_matrix("a->b, b->c, c->d, d->b")


