import numpy as np
import pandas as pd
import glob

files=glob.glob('*.xlsx')
col=1

dfs=[]

column='水  泥'

for file in files:
    year = file.replace('.xlsx', '')

    df = pd.read_excel(file, index_col=0,header=1)
    print(df,year)

    df = df['{0}'.format(column)]
    df.name=year
    print(df)
    dfs.append(df)

result = pd.concat(dfs, axis=1)
result=result.T
result.to_excel('D:\PyCharm 2025.3.2.1\project\pyoffice\data\{0}.xlsx'.format(column), index=True)