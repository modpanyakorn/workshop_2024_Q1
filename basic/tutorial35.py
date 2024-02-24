'''
ในไฟล์นี้เราจะมาเรียนรู้การใช้ pandas ในการอ่านข้อมูลจากไฟล์ .txt
'''
import pandas as pd

df = pd.read_table('uscrime.txt', delimiter=' ')
print(df)