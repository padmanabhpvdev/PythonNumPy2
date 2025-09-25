import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
cos_sim=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
print("vector A:\n",a)
print("vector B:\n",b)
print("cosine similarity:",cos_sim)