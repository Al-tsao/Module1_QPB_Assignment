#import module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data
df = pd.read_csv("PakWheelsDataSet.csv")
# print(df)

#number summary
print(df.describe())

#export hnumber summary to excel
df.describe().to_excel("output.xlsx")

