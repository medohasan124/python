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

# P(male OR smoke)

# p(a-b) = p(a) + p(b) - p(ab)

male = (data["sex"] == "Male").sum()
smoke = (data["smoker"] == "Yes").sum()

p_male = male / len(data)
p_smoke = smoke / len(data)

p_male_and_smoke = ((data["sex"] == "Male") & (data["smoker"] == "Yes")).sum() / len(data)

p_male_or_smoker = (p_male + p_smoke) - p_male_and_smoke








# P(female OR non-smoker)

# p(a-b) = p(a) + p(b) - p(ab)

p_female = (data["sex"] == "Female").sum() / len(data)
p_non_smoker = (data["smoker"] == "No").sum() / len(data)

p_female_and_non_smoker = ((data["sex"] == "Female") & (data["smoker"] == "No")).sum() / len(data)
p_female_or_non_smoker = p_female + p_non_smoker -p_female_and_non_smoker








# P(male OR  female)

# p(a-b) = p(a) + p(b) - p(ab)

p_male = (data["sex"] == "Male").sum() / len(data)
p_female = (data["sex"] == "Female").sum() / len(data)

p_male_and_female = p_male + p_female








# P(male OR  sat)

# p(a-b) = p(a) + p(b) - p(ab)

p_male = (data["sex"] == "Male").sum() / len(data)
p_sat = (data["day"] == "Sat").sum() / len(data)

p_male_and_sat = ((data["sex"] == "Male") & (data["day"] == "Sat")).sum() / len(data)

p_male_or_sat = p_male + p_sat - p_male_and_sat


print(p_male_or_sat)