import numpy as np
import seaborn as sns

data = sns.load_dataset("tips")
#1------------------------------
# p = probsbility
#p(a) = a / s
#get all male
p_a1 = (data["sex"] == "Male").mean()
p_a2 = (data["sex"] == "Male").sum() / len(data)

#2--------------------

# p = AND
#p(a) = a and b
#get all smoke AND male
#p(a and b) = p(ab) / p(b)

p_a_and_p_b1 = ((data["smoker"] == "Yes") & (data["sex"] == "Male")).sum() / len(data)
p_a_and_p_b2 = ((data["smoker"] == "Yes") & (data["sex"] == "Male")).mean()

male = data[data["sex"] == "Male"]
p_a_and_p_b3 = (male["smoker"] == "Yes").sum() / len(data)


print(p_a_and_p_b3)
#3-----------------------------

# p = if | Conditional
#p(a) = a if b
#get all smoker if male
#p(a | b) = p(ab) / p(b)



p_b = (data["sex"] == "Male").mean()
p_ab = ((data["smoker"] == "Yes") & (data["sex"] == "Male")).mean()
a_if_b = p_ab / p_b



#4-----------------------------

# p = Multiplication 

#get all smoker and male 
# P(AB) = P(a | b ) * p(b)

p_b = (data["sex"] == "Male").mean()
p_ab = ((data["smoker"] == "Yes") & (data["sex"] == "Male")).mean()
a_if_b = p_ab / p_b

a_and_b = a_if_b * p_b

print(a_and_b)


#5-----------------
#p = OR
# get male or female = 1  Mutually Exclusive
# p(a or b) = p(a) + p(b) - p(ab) 

p_a = (data["sex"] == "Male").mean()
p_b = (data["sex"] == "Female").mean()
p_ab = ((data["sex"] == "Male") & (data["sex"] == "Female")).mean()

print( (p_a+p_b) - p_ab)


