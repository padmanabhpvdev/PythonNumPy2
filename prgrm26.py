import numpy as np
v=np.array([2,3])
alpha=4
beta=5
lhs=alpha*v+beta*v  
rhs=(alpha+beta)*v
print("vector v:\n",v)
print("alpha=",alpha,"beta=",beta)
print("alphav+betav=",lhs)
print("(alpha+beta)v=",rhs)
print("linearity holds?",np.array_equal(lhs,rhs))