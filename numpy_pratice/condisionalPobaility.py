import numpy as np
import seaborn as sns

data = sns.load_dataset("tips")


data = sns.load_dataset("tips")

days = data["day"].unique()
sex = data["sex"].unique()
time = data["time"].unique()


# p(smoker | Sat)
for x in days:
    smokerDay = data[data["day"] == x]

    PsmokerinDay = (smokerDay["smoker"] == "Yes").sum() / len(smokerDay)
    print(f"p(smoker | {x}) = {PsmokerinDay *100:.2f}%")

print("----------------")
for x in time:
    allTime = data[data["time"] == x]

    P_time_male = (allTime["sex"] == "Male").sum() / len(allTime)
    print(f"p(Male | {x}) = {P_time_male *100:.2f}%")

    P_time_male = (allTime["sex"] == "Female").sum() / len(allTime)
    
    print(f"p(Female | {x}) = {P_time_male *100:.2f}%")
    print("----------------")


