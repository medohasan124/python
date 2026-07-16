import matplotlib.pyplot as plt

categories = ["Food", "Rent", "Transport", "Entertainment"]
amounts = [1500, 3000, 800, 700]

plt.pie(amounts , labels=categories , autopct='%0.1f%%', explode=[0,0.1,0,0])
plt.title("monthly amount")

plt.show()