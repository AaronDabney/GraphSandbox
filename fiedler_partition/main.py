import numpy as np
from sklearn.cluster import DBSCAN

import test_matrices
import matrix_util as mut
import vec_util as vut

a_matrix = test_matrices.b

laplacian = mut.laplacian_matrix(a_matrix)

fiedler_value, fiedler_vector = mut.fiedler_pair(laplacian)
eigen_values, eigen_vectors = np.linalg.eigh(laplacian)

print(laplacian, '\n')

print("Fiedler Value")
print(fiedler_value, '\n')

print("Fiedler Vector")
print(vut.round_vector(fiedler_vector, 4), '\n')

preprocessed_fiedler = vut.range_vector(fiedler_vector, 0).reshape(-1, 1)


max_group_distance = (2 / len(preprocessed_fiedler)) # More nodes --> More group selectivity
dbscan = DBSCAN(eps=max_group_distance, min_samples=1).fit(preprocessed_fiedler)

print(dbscan.labels_,'\n')
