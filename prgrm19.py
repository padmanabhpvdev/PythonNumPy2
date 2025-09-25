import numpy as np
A=np.random.randint(0,21,(3,3))
B=np.random.randint(0,21,(3,3))
print("matrix A\n",A)
print("matrix B\n",B)
addition=A+B
print("\n matrix addition \n",addition)
multiplication=np.dot(A,B)
print("\n matrix multiplication\n",multiplication)
transpose_product=multiplication.T
print("\n transpose of the product matrix\n",transpose_product)
