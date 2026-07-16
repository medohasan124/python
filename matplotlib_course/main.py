import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [5000, 7000, 6500, 8000, 9500]


plt.(months,revenue)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("monthly revenue")
plt.grid(True, linestyle='--',color='gray')
plt.show()