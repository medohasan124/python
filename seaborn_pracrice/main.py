import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = sns.load_dataset("titanic")


week1 = np.array([25, 26, 24, 25, 26, 24, 25])
week2 = np.array([15, 35, 10, 40, 5, 45, 20])



def stand(arr):
    total = 0
    num = len(arr)
    for index, x in enumerate(arr) :
        total += x

    mean = total / num

    # minus all number with mean

    newarr = []
    newtotal = 0
    for x in arr :
        y = mean - x
        newarr.append(y ** 2)
        newtotal += y ** 2


    mymean = newtotal / num 

    gadr = np.sqrt(mymean)
    return gadr

department_a = [8000, 8200, 7900, 8100, 8000]
department_b = [3000, 15000, 5000, 20000, 2000]

print(stand(department_a))
print(stand(department_b))

