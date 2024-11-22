import pandas as pd
import numpy as np

data = pd.read_csv('shopping_behavior_updated.csv')
print(data.columns)

#headlines
all_age = round(np.average(data['Age']), 2)
all_gender_male = (data['Gender'] == "Male").sum()/len(data['Gender'])*100
#all_amount = round(np.average('Purchase Amount (USD)'), 2)

categories = set()
for x in data['Category']:
    if x not in categories:
        categories.add(x)

print(categories)

#dataframe separation

by_categs = {}
for x in categories:
    by_categs[x] = data[data['Category'] == x]

def ave_age(x):
    ave_age = round(np.average(by_categs[x]['Age']), 2)
    ave_age_text = f"Average age: {ave_age} | ({round(ave_age-all_age, 2)}) from mean"
    return ave_age_text

def ave_gender(x):
    ave_gender = round((by_categs[x]['Gender'] == "Male").sum()/len(by_categs[x]['Gender']), 2)*100
    ave_gender_text = f"Male percentage: {ave_gender}% | {round(ave_gender-all_gender_male, 2)} PPs from mean"
    return ave_gender_text

def purch(x, y):
    if y == 0:
        ave_purch = round(np.average((by_categs[x]['Purchase Amount (USD)'])), 2)
        purch_text = f"{x} Average Purchase Size: ${ave_purch}"
        return ave_purch
    else:
        temp = [by_categs[x]][by_categs[x]['Gender'] == y]
        temp_purch = round(np.average(temp['Purchase Amount (USD)']), 2)
        return temp_purch

# for x in by_categs:
#     print(f"{x} : {ave_gender(x)})")

print(purch('Outerwear', ))