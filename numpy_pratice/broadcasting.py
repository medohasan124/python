import numpy as np

grades = np.array([
    [80, 90, 70, 85],
    [60, 75, 88, 92],
    [95, 60, 70, 80]
])

bonus = 5

result = grades + 5

weights = np.array([1, 2, 1.5, 1])

w_result = grades * weights

print(result)
print(w_result)