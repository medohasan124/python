import matplotlib.pyplot as plt

customer_ages = [22, 25, 19, 34, 45, 28, 31, 40, 55, 23, 
                  29, 33, 41, 26, 38, 50, 27, 36, 44, 21]

plt.hist(customer_ages, bins=4)
plt.title("Customer Age Distribution")
plt.xlabel("Age Range")
plt.ylabel("Number of Customers")
plt.show()