import pandas as pd


data = pd.read_csv("data.csv" , index_col="first_name")

#print(data.head()) #first 5 rows


print(data.shape) # 20 rows - 5 cols

print(data[data["price"] >= 30 ])


print(data["price"].mean())


print(data[data["price"] == data["price"].max()])

name = input("inter your name")

print(data.loc[name])
