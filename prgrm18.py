import numpy as np
matrix=np.array([[0,0,3],[4,0,0],[0,0,0]])
total_elements=matrix.size
zero_count=np.count_nonzero(matrix==0)
sparsity=zero_count/total_elements
print("matrix:")
print(matrix)
print(f"sparsity:{sparsity:2f}")