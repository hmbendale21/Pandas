import pandas as pd

# s = pd.Series([1,5,9,4,6])
# print(s)

# Custom Index

# s = pd.Series([88, 95, 84], index=["AI", "DSA", "OS"])

# print(s)
# print(s["AI"])  


# DATAFRAME

# data = {
#     "Name": ["Himanshu","Krushna","Anushka"],
#     "Age":  [22,23,23],
#     "City": ["Jalgaon","Chalisgaon","Dhule"] 
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.shape)
# print(df.columns)


# Selecting Data

# data = {
#     "Name": ["Himanshu","Krushna","Anushka"],
#     "Age":  [22,23,23],
#     "City": ["Jalgaon","Chalisgaon","Dhule"] 
# }
# df = pd.DataFrame(data)
# # print (df["Name"])
# # print(df[["Name", "City"]])
# df.index = ["a", "b", "c"]
# print (df.iloc[0])         # Accessing row by index position
# print(df.loc["b"])          # Accessing row by index label


# Simple Condition
# “Give me all rows where Age > 20”

# data = {
#     "Name": ["Himanshu","Krushna","Anushka"],
#     "Age":  [22,19,23],
#     "City": ["Jalgaon","Chalisgaon","Dhule"] 
# }
# df = pd.DataFrame(data)
# print(df[df["Age"] > 20])


