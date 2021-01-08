import numpy as np 
from numpy.linalg import norm
from math import inf

x = np.array([2,3,5]) 
y = np.array([3,4])

#norm funtion in Linear Regression module 
#L2 Norm
len_y = norm(y)
print(len_y)

len_x = norm(x)
print(len_x)

#L1 Norm
x = np.array([1,2,-4,-2])
l1_norm = norm(x,ord = 1) #L1 norm has order=1
print(l1_norm)

#p-Norm 
'''p=1 then L1 norm ; p=2 then L2 norm ; p=3 then p3 norm etc'''
z = [1,2,-4,-5]
z = np.array(z)
p1 = norm(z,1)
print("P1 -", p1)

z = [1,2,-4,-5]
z = np.array(z)
p2 = norm(z,2)
print("P2 -",p2)

z = [1,2,-4,-5]
z = np.array(z)
p3 = norm(z,3)
print("P3 -",p3)

z = [1,2,-4,-5]
z = np.array(z)
p4 = norm(z,4)
print("P4 -",p4)

#Vector Max Norm
'''returns max value from the vector when p is set as infinity so order is infinity; '''
x = np.random.randint(0,1000,10)
print("X - ", x)

max_norm = norm(x,ord = inf)
print("Max norm of Vector X - ", max_norm)







