import numpy as np

temps = np.array([28, 35, 22, 31, 19, 33, 25])

result1 = temps[temps > 30]
result2 = temps[(temps >= 25) & (temps <= 32)]
result3 = np.where(temps > 30)

print(result1)
print(result2)
print(result3)