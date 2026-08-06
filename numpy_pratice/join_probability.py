import numpy as np
import seaborn as sns

data = sns.load_dataset("tips")

days = data["day"].unique()
sex = data["sex"].unique()
time = data["time"].unique()


p_smoker = data["smoker"].value_counts() / data["tip"].count()
p_days = data["day"].value_counts() / data["tip"].count()

print(p_smoker)
print(p_days)



print("smoker &  days")
for x in days:
    smokerNum = ((data["smoker"] == "Yes") & (data["day"] == x)).sum()
    print(f"{x} - {smokerNum / len(data)}")

    
    psmokerDays = (data["smoker"] == "Yes").sum() / len(data[data["day"] == x])
    print(f"p(smoker | {x}) = {psmokerDays * 10 :.2f}%")
   
print("--------------------------------")
print("none smoker & days")
for x in days:
    nonsmokerNum = ((data["smoker"] == "No") & (data["day"] == x)).sum()
    print(f"{x} - {nonsmokerNum / len(data)}")

print("--------------------------------")
print("sex female & time")

for x in time:
    sexNum = ((data["sex"] == "Female") & (data["time"] == x)).sum()
    print(f"{x} - {sexNum / len(data)}")

print("sex male & time")
for x in time:
    sexNum = ((data["sex"] == "Male") & (data["time"] == x)).sum()
    print(f"{x} - {sexNum / len(data)}")
   