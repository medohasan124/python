import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

data = sns.load_dataset("tips")



print(data.head())
print(data.shape)




# لحساب فيمه متوسط الفاتوره 
print(f"Mean -", data["total_bill"].mean())
print(f"Median -", data["total_bill"].median())

print(f"min bill -" , data["total_bill"].min())
print(f"exp bill -" , data["total_bill"].max())


print(f"Q1 = ", np.percentile(data["total_bill"],25))
print(f"Median = ", np.percentile(data["total_bill"],50))
print(f"Q3 = ", np.percentile(data["total_bill"],75))


print("--------- smoker ----------------------")
print(data.groupby("smoker").size())
print("--------- smoker & bill ----------------------")
print(data.groupby("smoker")["total_bill"].mean())

print("--------- smoker & tips ----------------------")
print(data.groupby("smoker")["tip"].mean())
print("------------ sex numbers ----------------------")
print(data.groupby("sex").size())
print("------------ sex & smoker ----------------------")
print(data.groupby("sex")["smoker"].size())
print("------------ sex & bill ----------------------")
print(data.groupby("sex")["total_bill"].mean())
print("------------ sex & tips ----------------------")
print(data.groupby("sex")["tip"].mean())
#Mean - 19.78594262295082
#Median - 17.795
#min bill - 3.07
#exp bill - 50.81
#Q1 =  13.3475
#Median =  17.795
#Q3 =  24.127499999999998