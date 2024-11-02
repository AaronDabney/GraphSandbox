import numpy as np
import scipy
from sklearn.cluster import KMeans

import test_matrices
import matrix_util as mut


a_matrix = test_matrices.c
affinity_matrix = mut.build_affinity_matrix(a_matrix)
degree_matrix = mut.build_degree_matrix(affinity_matrix)
d_i = scipy.linalg.fractional_matrix_power(degree_matrix, -0.5)
laplacian = np.matmul(d_i, np.matmul(affinity_matrix, d_i))
eigen_data = np.linalg.eigh(laplacian)

print("a_matrix")
print(a_matrix, '\n')

print("affinity_matrix")
print(affinity_matrix, '\n')

print("degree_matrix")
print(degree_matrix, '\n')

print("d_i")
print(d_i, '\n')

print("laplacian")
print(laplacian, '\n')

print("Eigendata")
print(eigen_data)


num_clusters = 2
ortho_eigen_matrix = mut.build_orthogonal_eigen_matrix(eigen_data)
row_num, col_num = ortho_eigen_matrix.shape

sampled_eigen_matrix = mut.sample_range_of_columns(ortho_eigen_matrix, col_num - num_clusters, col_num)
normalized_eigen_matrix = mut.normalized_matrix_rows(sampled_eigen_matrix)

print(normalized_eigen_matrix)

kmeans = KMeans(n_clusters=num_clusters).fit(normalized_eigen_matrix)
print(kmeans.labels_)

# To do: 
# Sample intertia from kmeans clustering for range of cluster values. 
# Identify elbow position and magnitude
# Using elbow data list, determine definitive number of clusters
