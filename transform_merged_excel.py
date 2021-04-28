'''
Read xlsx file with merged data and transform it to a dataframe with duplicated key for unmerged data:
    A   B  
  +---+---+
1 | a | 0 |
  |   | 1 |
  |   | 2 |
  +---+---+
2 | b | 3 |
  +---+---+

Becomes the following dataframe:
  
    A   B  
  +---+---+
1 | a | 0 |
  +---+---+
2 | a | 1 |
  +---+---+
3 | a | 2 |
  +---+---+
4 | b | 3 |
  +---+---+

'''

import xlrd
import pandas as pd
import numpy as np

num_merged_col = 1  # index of column with merged data
num_dupl_col = 0    # index of column with data to duplicate

excel = xlrd.open_workbook('test.xlsx')
sheet_0 = excel.sheet_by_index(0)

# Reading fisrt xlsx sheet and transfer it to a dataframe
data = []
for ligne_idx in range(sheet_0.nrows):
    ligne = [sheet_0.cell(rowx=ligne_idx,colx=col_idx).value for col_idx in range(sheet_0.ncols)]
    data.append(ligne)
df = pd.DataFrame(data[1:],columns=data[0])
df['id'] = df.index

# Separation of merged data to list
name_merged = list(df)[num_merged_col]
name_dupl = list(df)[num_dupl_col]
df[name_merged] = df[name_merged].apply(lambda x: x.split('\n'))

# Adding new lines
new_lines = []
for idx in range(df.shape[0]):
    if len(df.iloc[idx][name_merged]) > 1:
        for elt in df.iloc[idx][name_merged][1:]:
            new_lines.append({
                name_dupl: df.iloc[idx][name_dupl], 
                name_merged: [elt],
                'id': df.iloc[idx]['id']
            })
df = df.append(new_lines)

# Keeping only first element of lists and sort by id to retrieve initial order
df[name_merged] = df[name_merged].apply(lambda x: x[0] if len(x)>0 else np.nan)
df = df.sort_values('id').drop('id',axis=1).reset_index(drop=True)
print(df)