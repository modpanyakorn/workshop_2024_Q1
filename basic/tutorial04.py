'''
ในไฟล์นี้จะเป็นการสร้างตัวแปรและกำหนดค่าให้กับตัวแปร
ตัวอย่างการกำหนดค่าของตัวแปรชนิดต่างๆ
ได้แก่ จำนวนเต็ม (integer) จำนวนจริง (float) จำนวนเชิงซ้อน (complex) และ จำนวนตรรกะ (boolean)
'''
i = 0 
print(type(i)) # ประเภทข้อมูล
print(i) # ค่าของตัวแปร 

f = 0.0000000001 # python มองว่าเป็น float (จำนวนจริง) มีค่าอยู่ระหว่าง  2.2250738585072014 x 10^308  ถึง 1.7976931348623157 x 10^308 
print(type(f)) # ประเภทข้อมูล
print(f) # ค่าของตัวแปร 
print(2*1e+10) # 10 ยกกำลัง 1
print(1e-1) # 10 ยกกำลัง -1

b = True # python มองว่าเป็น boolean (จำนวนตรรกะ:ค่าจริง[True]/เท็จ[False])
print(type(b)) # ประเภทข้อมูล
print(b) # ค่าของตัวแปร 

z = 5 + 12j # python มองว่าเป็น complex (จำนวนเชิงซ้อน) ในกรณีนี้คือ 5+12i หรือ (5,12) [ในกรณีเชิงขั่ว]
print(type(z)) # ประเภทข้อมูล
print(z) # ค่าของตัวแปร 
print(z.real) # ค่าส่วนจริง
print(z.imag) # ค่าส่วนจิตรภาพ
print(z.conjugate()) # conjugate ของ z