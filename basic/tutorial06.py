'''
ในไฟล์นี้เราจะเรียนรู้เกี่ยวกับสายอักขระ (String) และการดำเนินการเกี่ยวกับ String
'''

Name = 'Alphabet' #  python มองว่าเป็น string (ตัวอักษรที่มาเรียงกัน)
print(type(Name)) # ประเภทข้อมูล
print(Name) # ค่าของตัวแปร

print(Name[0]) # character ที่มี index 0 (ตำแหน่งแรก) ของ string ที่มีชื่อว่า Name
print(Name[1:5]) # character ที่มี index 1 จนถึง index'ก่อน'5 (index 4) ของ string ที่มีชื่อว่า Name
print(Name[:]) # character ทุกตำแหน่ง
print(Name[:-1]) # character ตั้งแต่ index 0 จนถึง index'ก่อน'-1 (ตำแหน่ง'แรก'สุดจาก'ด้านหลัง') นั้นคือทุกตำแหน่งยกเว้นตำแหน่งสุดท้าย
print(Name[::2]) # character ตำแหน่งที่ 2, 4, 6 (กระโดดที่ละ 2)
print(Name[2:6:2]) # character ตำแหน่งที่ 2, 4 (กระโดดที่ละ 2 อยู่ในช่วง index 2 ถึงก่อน index 6)

s_1 = '18' # python มองว่าเป็น string ที่มีอักษรสองตัว ตัวแรก(index 0)คือ 1  ตัวที่สอง(index 1)คือ 8 
print(s_1)

gap = ' ' # python มองว่าเป็น character ที่เป็นช่องไฟ/ช่องว่าง(gap)
print('a'+gap+'b')

blank = '' #  python มองว่าเป็น string ที่ว่างอยู่(ไม่มีค่าภายใน)
print(blank) #  เทียบเท่ากับการเว้นบรรทัด

# เราสามารถแก้ไขค่าในตัวแปรได้ โดยการกำหนดค่าใหม่ให้
str_short = 'sol' # กำหนดค่า
print(str_short)
str_short = 'solution' # แก้ไขค่า
print(str_short)

'''
เรา 'ไม่สามารถ' แก้ไขค่าของตัวแปร string ที่ละตัวอักษร(character)โดยการกำหนดค่าใหม่ได้
แต่ 'สามารถ' แก้ไขผ่าน .replace(สิ่งที่ต้องการแก้ไข,สิ่งที่อยากให้เป็น)
'''
str_long = 'optimization' # กำหนดค่า
print(str_long)
str_long = str_long.replace('z','s') # เปลี่ยน z ทุกตำแหน่ง ใน string ให้เป็น s
print(str_long)

# แปลงค่า string เป็น integer
s = '44'
print(type(s))
print(s)
n = int(s)
print(type(n))
print(s)

print() # เว่นหนึ่งบรรทัด

# แปลงค่า string เป็น float
s = '112'
print(type(s))
print(s)
n = float(s)
print(type(n))
print(s)

s_1 = 'He'
s_2 = 'is'
s_3 = 'a'
s_4 = 'man'
print(s_1+s_2+s_3+s_4) # ต่อ string เข้าด้วยกัน

print('฿'*50) # สำเนา string ฿ จำนวน 50 ตัว

print('e' in s_1) # ตรวจสอบว่ามี 'e' อยู่ใน s_1 หรือไม่

print('e' not in s_1) # ตรวจสอบว่า[ไม่มี] 'e' อยู่ใน s_1 หรือไม่