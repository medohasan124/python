import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

print(data.groupby("smoker")["total_bill"].sum())
print(data["smoker"].value_counts())