'''
ในไฟล์นี้เราจะมาเรียนรู้วิธีการเขียนข้อมูลลงในไฟล์ Excel และการอ่านข้อมูลจากไฟล์ Excel ด้วยภาษา Python โดยใช้ไลบรารี pandas และ openpyxl
ซึ่ง openpyxl จะต้องทำการติดตั้งก่อนด้วยคำสั่ง
pip install openpyxl
'''
import pandas as pd

data = {
    'Country': ['Belgium',  'India',  'Brazil'],
    'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
    'Population': [11190846, 1303171035, 207847528]
}
df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])
print(df)

df.to_excel('./myDataFrame.xlsx',  sheet_name='Sheet1')
xlsx = pd.ExcelFile('myDataFrame.xlsx')
df = pd.read_excel(xlsx,  'Sheet1')