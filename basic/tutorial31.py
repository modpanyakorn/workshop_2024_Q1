'''
ในไฟล์นี้เราจะมาเรียนรู้เกี่ยวกับการใช้งาน Series ใน pandas
'''
import pandas as pd

s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
print(s)
print(s['b'])


s[~(s > 1)] # boolean indexing
s[(s < -1) | (s > 2)]


print(s)
s['a'] = 6 # setting
print(s)

s.drop(['a',  'c'])
print(s)

s3 = pd.Series([7, -2, 3],  index=['a',  'c',  'd'])
print(s3)
print(s + s3)

s.add(s3, fill_value=0)
s.sub(s3, fill_value=2)
s.div(s3, fill_value=4)
s.mul(s3, fill_value=3)