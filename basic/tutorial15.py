'''
ในไฟล์นี้จะเป็นการสอนการใช้งาน numpy สำหรับ linear algebra
'''

'''
ฟังก์ชันสาหรับแก้ปัญหาเกี่ยวกับ linear algebra สามารถใช้ได้โดยการเรียก sub-modules linalg
det()สำหรับหา determinant
inv()สำหรับหา inverse ของ matrix
cholesky() สำหรับหา Cholesky decomposition matrix
eig() สำหรับหา eigenvalues และ right eigenvectors โดยจะคืนค่ามาสองค่า 
norm()สำหรับหาค่า norm-2 ของ matrix หรือ vector
'''

import numpy as np
from numpy import linalg as la

a =np.array([[4,2,0],[9,3,7],[1,2,1]])
print(a)

print()
print(la.det(a))

print()
print(la.inv(a))

print()
e,E = la.eig(a)
print(e) # eigenvalues
print(E) # right eigenvectors

print()
print(la.norm(a))
print(la.norm(a, ord='fro')) # Frobenius norm
print(la.norm(a, ord='nuc')) # nuclear norm

print()
b = np.arange(9)-4
print(b)
print(la.norm(b, ord=1)) # norm-1
print(la.norm(b, ord=2)) # norm-2
print(la.norm(b, ord=3)) # norm-p กรณีนี้ p=3

a = np.array([[4,2,0],[9,3,7],[1,2,1]])
print(a)
print(la.inv(a))
e,E = la.eig(a)
print(e) # eigenvalues
print(E) # right eigenvectors

