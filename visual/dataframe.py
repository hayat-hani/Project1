import pandas as pd
import numpy
import matplotlib.pyplot as plt


df = pd.read_csv('car data.csv')
#print(df.head())
# print(df["Car_Name"].head()) # print first 5 rows from Cr_Name column
# print(df.tail())
# print(df.loc[0]) # print first row
# dic = {
#     "colum1": [10, 20, 300],
#     "colum2": [30, 10, 100]
# }
# df2 = pd.DataFrame(dic)
# print(df2.head(2))
# print(df.shape)

df.info()
print(df.describe())

#df["Selling_Price"].plot() # matplot
df["Year"].hist()
df.plot.scatter(x="Year", y="Selling_Price")
plt.show()

