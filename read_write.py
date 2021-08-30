# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:48:36 2021

@author: Srija Anitha
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:/Users/Srija Anitha/Downloads/python code/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:/Users/Srija Anitha/Downloads/python code/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users/Srija Anitha\Downloads/python code/User_Data(1).xlsx')

df1 = pandas.read_excel('C:/Users/Srija Anitha/Downloads/python code/User_Data(1).xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
