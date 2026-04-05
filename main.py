import numpy as np
import pandas as pd
import glob

files=glob.glob('*.xlsx')
col=1
print(files)

dfs=[]

for file in files:
    year=file.replace('.xlsx','')

    df=pd.read_excel(file,index_col=0)

    df=df.iloc[:,[2]]
    df.iloc[0]=year
    print(df)
    dfs.append(df)

result=pd.concat(dfs,axis=1)
print(result)
result.to_excel('货 运 量.xlsx',index=True)