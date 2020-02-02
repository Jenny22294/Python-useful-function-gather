# Important packages
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import bisect # binary search
import re # deal with strings
import random #random walk
import csv
import sqlite3 # interacting with database
from io import StringIO
from datetime import datetime



# Data description 
df.shape() # see the shape of data
df.sort() # sorting for array
np.array() # read data as an array
a = str(a) # convert to string
df[i:j] # slicing
enumerate() # sequence function
zip(a,b)
map() # to map lambda function ---
assign() 
unique() 
value_counts()
str.lower() # convert to lower strings
groupby()




# Functions in Python
def mean_distance(x,y): ## create new function in python
    nx = len(x)
    result = 0.0
    count = 0
    for i in range(nx):
        result += x[i] - y[i]
        count +=1
    return result/count


def unique_name(name1, name2): ## find unique name
    unique = []
    name1.extend(name2) # extend list
    for name in name1:
        if name not in unique:
            unique.append(name)
    return unique


def append_element(some_list, element): # append elements
    some_list.append(element) # remove is oposite to append 


for i in range(4): # elif condiction
    for j in range(4):
        if j>i:
            break
        print((i,j))


for i, j in enumerate(some_list):
    mapping[j] = i # mapping = {}


def cleaning_strings(strings): # clean strings
    result = []
    for value in strings:
        value = value.strip() # returns a copy of the string with both leading and trailing characters removed 
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


def fun(x):
    return x*2 # is equivalent to
equiv_non = lambda x: x*2
def apply_to_list(some_list, f):
    return [f(x) for x in some_list] #need to declare ints


with open(path) as f: # files and operating system
    lines = [x.rstrip() for x in f]




# Interacting with database

import sqlite3 
query = """
CREATE TABLE test (
    a varchar(20),
    b varchar(20),
    c real,
    d integer
); """
con = sqlite3.connect('your_database_name')
con.execute(query)
con.commit()



# Filtering out missing data

from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
data.drop() # drop NA is equal to:
data[data.notnull()] # OR
data.dropna(how = 'all')

data.fillna() # your choice of value in ()
data.fillna(data.mean()) # fill with means for numeric numbers

data.drop_duplicates() # dropping duplicates



# Transforming Data Using a Function or Mappin
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()
data['animal'] = lowercased.map(meat_to_animal) # is equal to:
data['food'].map(lambda x:meat_to_animal[x.lower()])


# Replacing values
data.replace(-999, np.nan)

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})
dummies = pd.get_dummies(df['key'], prefix = 'key')
df_with_dummies = df[['data1']].join(dummies) 
# for more, refer to: https://github.com/Jenny22294/pydata-book/blob/2nd-edition/ch07.ipynb



# Iterating over groups
for name, group in df.group('key1'):
    print(name)
    print(group)

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
group_mean1 = df['data1'].groupby(df['key1']).mean()
group_mean2 = df['data1'].groupby(df['key1'], df['key2']]).mean()



# String and Datetime
from datetime import datetime,date
df = pd.DataFrame({'date':['2011-07-06 12:00:00', '2011-08-06 00:00:00']})
df['date'] = pd.to_datetime(df['date']).dt.normalize()
## remove 00:00:00
### OR



# Converting Timestamps to Periods (and Back)
rng = pd.date_range('2000-01-01', periods=3, freq='M')