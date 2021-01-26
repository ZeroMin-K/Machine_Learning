import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[-1, -2], [-3, -4], [-5, -6]])

C = np.dot(A, B)    # 행렬 곱 수행

# matrix A, B 형상 출력
print('A.shape ==', A.shape, ', B.shape ==', B.shape)
print('C.shape ==', C.shape)
print(C)
