#import module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data
df = pd.read_csv("PakWheelsDataSet.csv")
# print(df)

#number summary
# print(df.describe())

#export hnumber summary to excel
# df.describe().to_excel("output.xlsx")

#Capacity(CC)
df.sort_values('Engine Capacity(CC)')

sns.set()
g = sns.histplot(x = 'Engine Capacity(CC)', data = df, bins = 30)
g.ticklabel_format(style='plain')
plt.show()