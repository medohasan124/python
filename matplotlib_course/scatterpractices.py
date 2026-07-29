import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [12000, 15000, 11000, 18000, 22000, 25000] # ربح

categories = ["Salaries", "Rent", "Marketing", "Supplies"]
expenses = [8000, 3000, 2000, 1000] #نفقات

ad_spend = [200, 400, 300, 600, 800, 500, 700, 900, 350, 450] # الانفاق الاعلاني
sales_generated = [1000, 1800, 1500, 2500, 3200, 2100, 2800, 3500, 1600, 1900] # المبيعات المحققه

customer_ages = [22, 25, 19, 34, 45, 28, 31, 40, 55, 23, 
                  29, 33, 41, 26, 38, 50, 27, 36, 44, 21]




fig , axes = plt.subplots(2,2)

#exam 1
axes[0,0].plot(months , revenue)
axes[0,0].set_title("months , revenue")
axes[0,0].set_xlabel("months")
axes[0,0].set_ylabel("revenue")


#exam 2 
axes[0,1].pie(expenses , labels=categories , autopct='%1.1f%%' , explode=[0.1,0,0,0])
axes[0,1].set_title("expenses , categories")


#exam 3 
axes[1,0].scatter(ad_spend ,sales_generated)
axes[1,0].set_title("ad_spend , sales_generated")
#exam 4
axes[1,1].hist(customer_ages , bins=4)
axes[1,1].set_title("customer_ages")
plt.show()
