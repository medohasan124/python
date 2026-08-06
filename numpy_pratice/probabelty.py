import numpy as np
import seaborn as sns

data = sns.load_dataset("tips")

days = data["day"].unique()
for x in days:

    day_count = (data["day"] == x).sum()
    bill_count = data["tip"].count()
    probability_data = day_count / bill_count
    print(f"{x }  - { probability_data * 100} %")





# list of days 
# loop this days
