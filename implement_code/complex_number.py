z = 5 + 12j # python มองว่าเป็น complex (จำนวนเชิงซ้อน) ในกรณีนี้คือ 5+12i หรือ (5,12) [ในกรณีเชิงขั่ว]
print(type(z)) # ประเภทข้อมูล
print(z) # ค่าของตัวแปร 
print(z.real) # ค่าส่วนจริง
print(z.imag) # ค่าส่วนจิตรภาพ
print(z.conjugate()) # conjugate ของ z