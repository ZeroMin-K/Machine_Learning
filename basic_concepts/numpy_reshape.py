import numpy as np

C = np.array([1, 2, 3])

# vector C 형상 출력
print('C.shape ==', C.shape)

# vector를 (1, 3) 행렬로 형 변환
C = C.reshape(1, 3)

print('C.shape ==', C.shape)
