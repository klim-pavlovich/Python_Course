import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.DataFrame(columns=['robot', 'human'])

for item in data['whoAmI']:
    if item == 'robot':
        one_hot_data = one_hot_data._append({'robot': 1, 'human': 0}, ignore_index=True)
    elif item == 'human':
        one_hot_data = one_hot_data._append({'robot': 0, 'human': 1}, ignore_index=True)

print(one_hot_data.head(10))