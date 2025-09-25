import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
upper=np.triu(A)
lower=np.tril(A)
print(f"Original : \n{A}")
print("upper \n",upper)
print("lower \n",lower)