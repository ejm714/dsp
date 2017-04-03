# Matrix Algebra

import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([1, 8, 0, 5])
w = np.reshape(w, (4,1))

A.shape
# (2, 3)
B.shape
# (2, 2)
C.shape
# (3, 2)
D.shape
# (2, 3)
u.shape
# (1, 4)
w.shape
# (4, 1)

u + v
# [ 9,  7, -4,  9]
u - v
# [ 3, -3, -2,  1]
6*u
# [ 36,  12, -18,  30]
np.dot(u, v)
# 51
np.linalg.norm(u)
# 8.60

A + C
# not defined
A - C.transpose()
# [-4, -7, -3],
# [ 3,  6,  4]
C.transpose() + 3*D
# [14,  3,  3],
# [ 2,  7,  9]
B @ A
# or np.dot(B, A)
# [-1, -5, -1],
# [ 2,  7,  4]
B @ A.transpose()
# not defined

B @ C
# not defined
C @ B
# [ 5, -6],
# [ 9, -8],
# [ 6, -6]
np.linalg.matrix_power(B, 4)
# [ 1, -4],
# [ 0,  1]
A @ A.T
# [14, 28],
# [28, 69]
D.T @ D
# [10, -4,  0],
# [-4,  8,  8],
# [ 0,  8, 10]

# testing for github
