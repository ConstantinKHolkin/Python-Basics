import pandas as pd
import random

# Генерация исходного DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one hot кодирования
one_hot_encoded = pd.concat([
    pd.Series(1, index=data.index[data['whoAmI'] == 'robot'], name='robot'),
    pd.Series(1, index=data.index[data['whoAmI'] == 'human'], name='human')
], axis=1).fillna(0).astype(int)

# Вывод результата
print(one_hot_encoded.head())
