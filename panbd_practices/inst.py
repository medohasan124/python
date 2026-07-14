import pandas as pd

data = [144,567,32,67]

series = pd.Series(data , index=["A","B","C","D"])

print(series[series > 200])