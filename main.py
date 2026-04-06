import numpy as np
import pandas as pd
import glob

files=glob.glob('*.xlsx')
col=1
print(files)

dfs=[]

column='化学纤维'

for file in files:
    year = file.replace('.xlsx', '')

    df = pd.read_excel(file, index_col=0,header=1)

    df = df['{0}'.format(column)]
    df.name=year
    print(df)
    dfs.append(df)

result = pd.concat(dfs, axis=1)
print(result)
result.to_excel('{0}.xlsx'.format(column), index=True)