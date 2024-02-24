'''
ในไฟล์นี้เราจะเรียนรู้เกี่ยวกับการใช้งาน pandas ในการจัดการข้อมูล
'''
import pandas as pd

data = {
    'Country': ['Belgium',  'India',  'Brazil'],
    'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
    'Population': [11190846, 1303171035, 207847528]
}

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])
print(df)


df.shape
df.index
df.columns
df.info()
df.sum()
df.cumsum()
df['Population'].min()/df['Population'].max()
df['Population'].idxmin()/df['Population'].idxmax()
df.describe()
df.mean()
df.median()

f = lambda x: x*2
'''
This is the same as 
def f(x):
  return x*2
'''

df.apply(f)
df.applymap(f)