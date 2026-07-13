import numpy as  np

price = np.array([445,32,656,234])
quant = np.array([35,6,3,22])

total = price * quant

print(total)
print(total.sum())

new_sales = np.array([100, 1500, 900, 2000, 1800, 2200, 1600])

after_discount = new_sales - (new_sales * 0.10)
print(new_sales.sum())
print(new_sales.mean())
print(after_discount)