import numpy as np
import seaborn as sns

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


