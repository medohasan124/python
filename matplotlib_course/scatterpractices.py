import matplotlib.pyplot as plt

temperature = [10, 15, 20, 25, 30, 35, 5, 12, 28, 18]
ice_cream_sales = [20, 35, 55, 80, 110, 140, 10, 25, 95, 45]
plt.scatter(temperature, ice_cream_sales)
plt.title("Shoe Size vs Typing Speed")
plt.xlabel("Shoe Size")
plt.ylabel("Typing Speed (WPM)")
plt.show()