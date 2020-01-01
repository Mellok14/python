import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[12, 2, 1]])
C = np.concatenate((A,B.T), axis=1)
print(C)
print(np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001))
B1 = np.array([[3, 2, 1]])
C1 = np.concatenate((A,B1.T), axis=1)
print(np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C1, 0.0001))
#Т.к. ранг матрицы равен рангу расширенной матрицы и ранг меньше числа
#неизвестных - система имеет бесконечное множество решений
