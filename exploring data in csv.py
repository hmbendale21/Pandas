import pandas as pd
df = pd.read_csv("students.csv")
# print(df)
# print(df.shape)         # number of rows and columns
# print(df.columns)      # column names
# print(df.dtypes)       # data types of each column
# print(df.head())        #frist 5 rows

# print(df["Marks"])
print(df[df["Marks"] > 80])

