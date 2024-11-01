import numpy as np
import scipy
from sklearn.cluster import DBSCAN

import testMatrices
import matrix_Util as mut
import vec_util as vut


aMatrix = testMatrices.a

laplacian = mut.laplacianMatrix(aMatrix)

fiedlerValue, fiedlerVector = mut.fiedlerPair(laplacian)
eigenValues, eigenVectors = scipy.linalg.eigh(laplacian)

print(laplacian, '\n')

print("Fiedler Value")
print(fiedlerValue, '\n')

print("Fiedler Vector")
print(vut.roundVector(fiedlerVector, 4), '\n')

preprocessedFiedler = vut.rangeVector(fiedlerVector, 0).reshape(-1, 1)


maxGroupDistance = (2 / len(preprocessedFiedler)) # More nodes --> More group selectivity
dbscan = DBSCAN(eps=maxGroupDistance, min_samples=1).fit(preprocessedFiedler)

print(dbscan.labels_,'\n')
