import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])
Q, R = np.linalg.qr(A)
print(np.dot(Q, R))
print(np.dot(np.transpose(Q), Q))
R1 = R[:2, :2]
print(R1)
B1 = np.dot(np.transpose(Q), B)[:2]
print(B1)
X1 = np.linalg.solve(R1, B1)
print(X1)
X = np.append(X1, 0)
print(X)
print(np.linalg.norm(X))
print(np.linalg.norm(np.dot(A, X) - B))
print(np.linalg.lstsq(A, B))
X2 = np.array([1.25, 0.5, -0.25])
print(np.linalg.norm(X2),  np.linalg.norm(np.dot(A, X2) - B))