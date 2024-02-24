'''
ในไฟล์นี้เราจะมาดูการใช้งาน pandas ในการอ่านไฟล์ csv และทำการตรวจสอบข้อมูลในไฟล์ csv ว่ามีข้อมูลที่เป็น null หรือไม่ และทำการตรวจสอบข้อมูลที่เป็น unique และทำการตรวจสอบข้อมูลที่เป็นค่าสถิติเช่น mean, std, min, max และอื่นๆ
'''
import pandas as pd

# Read file Transaction.csv then assign it into df_transac
df_transac = pd.read_csv("Transactions.csv")

df_transac.head()

df_transac.info()

df_transac.isnull().sum()

df_transac.nunique()

df_transac["Store_type"].value_counts()

df_transac.describe()