import pandas as pd


data = {
    "product": ["milk", "bread", "eggs", "cheese"],
      "price": [7.5, 5.0, 3.0, 20.0],
    "quantity": [4, 2, 12, 1]
}

df = pd.DataFrame(data)

df["total"] = df["price"] * df["quantity"]

df["discount"] = df["price"] - 0.10
mor_than_three = df[df["quantity"] >= 3 ]

maximum =  df[df["price"] == df["price"].max()] 


print(maximum)
