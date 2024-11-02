import numpy as np

def degree_matrix(adjacency_matrix):
    width, height = adjacency_matrix.shape
    if width != height:
        raise Exception("-- Input matrix must be square --")
    
    output = np.zeros((width, height))

    for y, row in enumerate(adjacency_matrix):
        for x, cell in enumerate(row):
            if x != y:
                output[y][y] += adjacency_matrix[y][x]
    
    return output

def laplacian_matrix(adjacency_matrix):
    deg_matrix = degree_matrix(adjacency_matrix)
    laplacian = deg_matrix - adjacency_matrix
    return laplacian

def fiedler_pair(laplacian):
    eigen_values, eigen_vectors = np.linalg.eigh(laplacian)
    return (eigen_values[1], eigen_vectors[:, 1])
