import numpy as np
import seaborn as sns

data = sns.load_dataset("tips")


# P(Saturday OR Sunday)

# p(a-b) = p(a) + p(b) - p(ab)

sat = (data["day"] == "Sat").sum()
sun = (data["day"] == "Sun").sum()

p_sat = sat / len(data)
p_sun = sun / len(data)
p_sat_sun = (p_sat + p_sun)

print(p_sat)
print(p_sun)
print(p_sat_sun)
print(p_sat + p_sun - p_sat_sun)
