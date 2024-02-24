'''
ในไฟล์นี้เราจะมาเรียนรู้การใช้งาน pandas ในการจัดการข้อมูล 
'''
import pandas as pd

data = {
    'Country': ['Belgium',  'India',  'Brazil'],
    'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
    'Population': [11190846, 1303171035, 207847528]
}
df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])
print(df)

df.to_csv('myDataFrame.csv')
pd.read_csv('myDataFrame.csv')

df.iloc[0, 0] # by position

df.loc[0,  'Country'] # by label

df[df['Population']>1200000000]

df.drop('Country', axis=1) 
print(df)

df.sort_index()

df.sort_values(by='Population') 

df.rank()