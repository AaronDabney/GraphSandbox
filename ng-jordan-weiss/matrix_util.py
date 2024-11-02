import numpy as np
import math 
import copy

def affinityMatrix(adjacencyMatrix, sigma=1):
    shape = adjacencyMatrix.shape
    numRows, numCols = shape

    maxAbsValue = max(adjacencyMatrix.max(), abs(adjacencyMatrix.min()))

    output = np.ones(shape)
    for rowIndex in range(numRows):
        for columnIndex in range(numCols):
            if columnIndex != rowIndex:
                output[rowIndex][columnIndex] = 1 - (adjacencyMatrix[rowIndex][columnIndex] / maxAbsValue)

    for rowIndex in range(numRows):
        for columnIndex in range(numCols):
            if columnIndex != rowIndex:
                output[rowIndex][columnIndex] = math.exp(-0.5 * (output[rowIndex][columnIndex]**2) / sigma ** 2)
            else:
                output[rowIndex][columnIndex] = 0

    return output

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

def degreeMatrixAlt(inputMatrix):
    shape = inputMatrix.shape
    numRows, numCols = shape

    if numRows != numCols:
        raise Exception("-- Input matrix must be square --")

    rowTallys = []
    for i in range(numRows):
        tally = 0
        for j in range(numCols):
            tally += inputMatrix[i, j]
        rowTallys.append(tally)

    output = np.zeros(shape)
    for i in range(numRows):
        output[i][i] = rowTallys[i]

    return output


# If two eigen vectors share an eigenvalue remove the one that occurs later 
# preserving earliest occurence
def orthogonalizedEigenMatrix(eigenData, threshold = 0.01):
    eigenValues, eigenMatrix = eigenData
    removeIndices = set()

    for i in range(len(eigenValues)):
        for j in range(i + 1, len(eigenValues)):
            difference = abs(eigenValues[i] - eigenValues[j])
            if difference < threshold:
                removeIndices.add(j)

    removeIndices = list(removeIndices)
    removeIndices.sort(reverse=True)

    output = copy.deepcopy(eigenMatrix)

    for index in removeIndices: 
        output = np.delete(output, index, axis=1)

    return output

# Start and end inclusive [start, end]
# zero indexed
def sampleRangeOfColumns(matrix, start, end):
    return matrix[:,start:end + 1]


def normalizeMatrixRows(matrixInput):
    matrix = np.zeros(matrixInput.shape)#copy.deepcopy(matrixInput)
    
    for y, row in enumerate(matrixInput):
        length = np.linalg.norm(row)
        for x, item in enumerate(row):
            matrix[y][x] = item / length

    return matrix

