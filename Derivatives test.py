

import pandas as pd
import numpy as np
import math
from datetime import datetime,timedelta, date
import csv
import re
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats



df=pd.read_csv("C:\\Users\\daniele\\Downloads\\stock_A.csv")
df1=pd.read_csv("C:\\Users\\daniele\\Downloads\\stock_B.csv")


#assume only buy 1 every period
#" In both these cases, we do the opposite trade when the price of B changes." assume we close in the period T.
df['price_change'] = df['price'] - df['price'].shift(1)
df1['price_change'] = df1['price'] - df1['price'].shift(1)
df1['timestampdif'] = df1['timestamp'] - df1['timestamp'].shift(1)
df['timestampdif'] = df['timestamp'] - df['timestamp'].shift(1)
len(df[(df['price_change'] > 0.015) & (df['timestampdif'] >=0.04)])
len(df[(df['price_change'] <- 0.015) & (df['timestampdif']>=0.04)])
df['timestampdif'].max()
df['timestampdif'].min()



portfolio=0

#our profit is the price change between t-1 and t "assume that at any given time T, you can buy or sell the stock at the last
#price that we had before T. & In both these cases, we do the opposite trade when the price of B changes."
for i in range(len(df)):
    if df['price_change'].iloc[i]>0.015 and df['timestampdif'].iloc[i]>=0.04:#then we buy
        portfolio+=df1['price_change'].iloc[i]

    elif df['price_change'].iloc[i]<-0.015 and df['timestampdif'].iloc[i]>=0.04:#then we sell b
            portfolio-=df1['price_change'].iloc[i] 

    else:
        pass
    


print("trade made sell 257, buy 236 times")
print("profit at end "+ str(portfolio))




print(sns.distplot(df['timestampdif'].dropna()))



#brute force method - may take a long time!!:

dicts = {}
for i in df['timestampdif'].dropna():
    if abs(df[(abs(df['price_change']) > 0.015) & (df['timestampdif']>=i)]['price_change']).sum()>0:
        dicts[i]=abs(df[(abs(df['price_change']) > 0.015) & (df['timestampdif']>=i)]['price_change']).sum()
print("first value is time, second is profit " + str( min(dicts.items(), key=lambda x: x[1]>0)))




# different approach not complete-------
# df2=df['timestampdif'].dropna().tolist()
# df2.sort()
# i=len(df2)//2
# j=len(df2)//2
# while i < len(df) and j>=0:
#     profit = abs(df[(abs(df['price_change']) > 0.015) & (df['timestampdif']>=i)]['price_change']).sum()
#     if abs(df[(abs(df['price_change']) > 0.015) & (df['timestampdif']>=i)]['price_change']).sum()>0
 

#     elif  > 0:
#         i += 1
#     else:
#         j -= 1

