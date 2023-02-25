# with open('work_log.txt', 'a') as file:
#     file.write('\n25.02')

import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')


for (index, row) in data.iterrows():
    print(type(row))