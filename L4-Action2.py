import pandas as pd

# 数据加载
dataset = pd.read_csv('D:/Python/TEST/Market_Basket_Optimisation.csv', header=None)

transactions=[]
#按行遍历
for i in range(0, dataset.shape[0]):
    temp = []
    #按列遍历
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != 'nan':
            temp.append(dataset.values[i, j])
    transactions.append(temp)

from efficient_apriori import apriori

itemsets, rules = apriori(transactions, min_support=0.02, min_confidence=0.3)
print(itemsets)
print(rules)
