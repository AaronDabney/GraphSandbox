import numpy as np
import scipy

def degreeMatrix(adjacencyMatrix):
    width, height = adjacencyMatrix.shape
    if width != height:
        raise Exception("-- Input matrix must be square --")
    
    output = np.zeros((width, height))

    for y, row in enumerate(adjacencyMatrix):
        for x, cell in enumerate(row):
            if x != y:
                output[y][y] += adjacencyMatrix[y][x]
    
    return output

def laplacianMatrix(adjacencyMatrix):
    dMatrix = degreeMatrix(adjacencyMatrix)
    laplacian = dMatrix - adjacencyMatrix
    return laplacian

def fiedlerPair(laplacian):
    eigenValues, eigenVectors = scipy.linalg.eigh(laplacian)
    return (eigenValues[1], eigenVectors[:, 1])
