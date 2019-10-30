import unittest
from collections import defaultdict
import pprint
def adjacency_matrix_to_adjacency_list(matrix):
    adjacency_list = defaultdict(list)
    row_len = len(matrix[0])
    nums_cols_to_iter = row_len
    for row_index, row in enumerate(matrix):
        start_from_col = row_len - nums_cols_to_iter
        for col_index, col_val in enumerate(row[start_from_col:],
                                            start_from_col):
            if row_index == col_index:
                continue
            if col_val:
                adjacency_list[row_index].append(col_index)
                adjacency_list[col_index].append(row_index)
        nums_cols_to_iter -= 1
    return dict(adjacency_list)


def adjacency_list_to_incident_matrix(adjacency_list):
    list_len = len(adjacency_list)
    # Calculate the max number of edges in a graph of n vertices n*(n-1)/2
    max_edges = (list_len * (list_len - 1)) / 2
    incident_matrix = [[0] * list_len for _ in xrange(max_edges)]
    current_row = 0
    for parent_vertex, vertices in adjacency_list.iteritems():
        for child_vertex in vertices:
            # Since the graph is undirected we can ignore duplicating the edge.
            if child_vertex < parent_vertex:
                continue
            incident_matrix[current_row][parent_vertex] = 1
            incident_matrix[current_row][child_vertex] = 1
            current_row += 1
    return incident_matrix


def incident_matrix_to_adjacency_list(matrix):
    adjacency_list = defaultdict(list)
    def add_edge(x, y):
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    for vertices in matrix:
        pairs = []
        for index, v in enumerate(vertices):
            if v:
                pairs.append(index)
        add_edge(*pairs)
    return dict(adjacency_list)
def adjacency_list_to_adjacency_matrix(aux1):
    matrix=[]
    n=len(aux1)
    l = [x for x in range(0, n)]
    for line in aux1.values():
        

        aux = []
        for key in l:
    #   for key, value in enumerate(l):
            if key in line:
                aux.append(1)
            else:
                aux.append(0)
        matrix.append(aux)
    return matrix
def adjacency_matrix_to_Incidence_matrix(matrix):
    adjacency_list = adjacency_matrix_to_adjacency_list(matrix)
    Incidence_matrix = adjacency_list_to_incident_matrix(adjacency_list)
    return Incidence_matrix
def incident_matrix_to_adjacency_matrix(matrix):
    adjacency_list = incident_matrix_to_adjacency_list(matrix)
    adjacency_matrix = adjacency_list_to_adjacency_matrix((adjacency_list))
    return adjacency_matrix

