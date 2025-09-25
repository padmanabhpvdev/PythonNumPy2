import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
scalar_A=2
scalar_B=3
A_scaled=scalar_A*A
B_scaled=scalar_B*B
print("original matrix A\n",A)
print(f"matrix A after multipliyng by {scalar_A}:\n{A_scaled}")
print("original matrix B\n",B)
print(f"matrix B after multipliyng by {scalar_B}:\n{B_scaled}")
