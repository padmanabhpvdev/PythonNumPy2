import numpy as np
A=np.array([[1,2],[3,4]])
rank=np.linalg.matrix_rank(A)
print(rank)