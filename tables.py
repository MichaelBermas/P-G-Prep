import pandas as pd
import numpy as np
from collections import Counter

data = pd.read_csv('shopping_behavior_updated.csv')
pd.set_option('display.max_columns', None)

categories = set()
for x in data['Category']:
    if x not in categories:
        categories.add(x)

data_categ = {"Total": data}
for x in categories:
    data_categ[x] = data[data['Category'] == x]

def master(categ):
    ind = data_categ[categ]
    temp_list = []
    count = len(ind)
    age = round(np.average(ind['Age']), 2)
    m_perc = round((ind['Gender'] == 'Male').sum()/len(ind), 2)*100
    purch = round(np.average((ind['Purchase Amount (USD)'])), 2)
    count_freq = Counter(ind['Frequency of Purchases'])
    sorted_freq = count_freq.most_common()
    mode0 = (sorted_freq[0][0], round((sorted_freq[0][1]/count)*100, 2))
    mode1 = (sorted_freq[1][0], round((sorted_freq[1][1]/count)*100, 2))
    temp_list.extend((categ, count, age, m_perc, purch, mode0, mode1))
    return temp_list

cols = ['Category', 'Count', 'Ave. Age', 'Male %', 'Ave. Purchase Size (USD)', 'Top Purchase Frequency', '2nd Top Purchase Frequency']
rows = []
for x in data_categ:
    instance = master(x)
    rows.append(instance)

print(pd.DataFrame(rows, columns=cols))