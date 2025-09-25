import numpy as np
A=np.array([[1,2],[3,4]])
diag_vector=np.diag(A)
vector=np.array([5,10,15])
diag_matrix=np.diag(vector)
print("original matrix:\n",A)
print("diagonal vector:\n",diag_vector)
print("diagonal matrix from vector:\n",diag_matrix)