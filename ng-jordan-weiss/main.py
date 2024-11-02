import numpy as np
import scipy.linalg
import testMatrices
import matrix_util as mut
import scipy
from sklearn.cluster import KMeans

aMatrix = testMatrices.c
affinityMatrix = mut.affinityMatrix(aMatrix)
degMatrix = mut.degreeMatrixAlt(affinityMatrix)
d_i = scipy.linalg.fractional_matrix_power(degMatrix, -0.5)
laplacian = np.matmul(d_i, np.matmul(affinityMatrix, d_i))
eigData = np.linalg.eigh(laplacian)

print("aMatrix")
print(aMatrix, '\n')

print("affinityMatrix")
print(affinityMatrix, '\n')

print("diagMatrix")
print(degMatrix, '\n')

print("d_i")
print(d_i, '\n')

print("laplacian")
print(laplacian, '\n')

print("Eigendata")
print(eigData)


numClusters = 2
orthoEigenMatrix = mut.orthogonalizedEigenMatrix(eigData)
rowNum, colNum = orthoEigenMatrix.shape

sampledEigenMatrix = mut.sampleRangeOfColumns(orthoEigenMatrix, colNum - numClusters, colNum)
normalizedEigenMatrix = mut.normalizeMatrixRows(sampledEigenMatrix)

print(normalizedEigenMatrix)

kmeans = KMeans(n_clusters=numClusters).fit(normalizedEigenMatrix)
print(kmeans.labels_)

# To do: 
# Sample intertia from kmeans clustering for range of cluster values. 
# Identify elbow position and magnitude
# Cluster number assosciated with strongest elbow is selected as definitive cluster
