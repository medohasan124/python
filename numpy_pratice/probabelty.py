import numpy as np
import seaborn as sns

data = sns.load_dataset("tips")

days = data["day"].unique()
bill_count = data["tip"].count()
for x in days:

    day_count = (data["day"] == x).sum()
    probability_data = day_count / bill_count
    print(f"{x }  - { probability_data * 100} %")

#------------------------------------------------
somker = (data["smoker"]).value_counts()
non_somker = (data["smoker"] == 'No').sum()

sm = somker / bill_count
nsm = non_somker / bill_count
print(sm + nsm)