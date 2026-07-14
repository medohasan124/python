import numpy as np

np.random.seed(5)

dgree = np.random.randint(15,40 , size=8)
calibration =  1.5

new_dgree = dgree + calibration
mean = dgree.mean()

more_than_mean = dgree[dgree > mean]
print(dgree)
print(mean)
print(more_than_mean)
print(new_dgree)