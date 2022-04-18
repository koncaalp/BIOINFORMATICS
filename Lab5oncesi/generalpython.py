import pandas as pd
import numpy as np
from numpy import where

distance_dict = {'Human':(0,1,3,7), 'Chimp':(1,0,2,6), 'Pig':(3,2,0,4), 'Cat':(7,6,4,0)}

df = pd.DataFrame(distance_dict,index=distance_dict.keys())
# print(df.index)
print(df.loc["Human"])
print(df.loc["Human","Cat"]) 
print(df.loc[["Human","Cat"],:]) # rows that have Human and Cat
print(df.loc[["Human","Cat"],:].sum()) # sum of all rows that have Human and Cat
print(df["Human"].nsmallest(2)) # smallest 2 values in column Human
print(df.iloc[0]) # first row
print(df.iloc[[0,2],[1,2]]) # first and third row, columns 2 and 3
