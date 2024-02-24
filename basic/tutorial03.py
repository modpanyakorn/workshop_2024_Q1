'''
ในไฟล์นี้จะเป็นการสร้างตัวแปรและกำหนดค่าให้กับตัวแปร

กำหนดค่าคงที่/ตัวแปร; ชื่อ = ค่าที่ต้องการ
โดยการตั้งชื่อนั้นมีข้อกำหนดเล็กน้อย เช่น
ขึ้นต้นชื่อเป็นอักษรภาษาอังกฤษเท่านั้น,
ต้องเขียนติดกัน, ใสัญลักษณ์พิเศษได้แค่ underscore "_",
ตัวอักษรพิมพ์ใหญ่-เล็กถือว่าเป็นคนละชื่อ,
ห้ามใช้คำสงวนเช่น if, for, max, sum เป็นต้น,
ความยาวชื่อไม่เกิน 255 ตัวอักษร
'''

Me = 'metoo'
You = 'look nice'
Our = 1
VAT = 7
vat = 0.07
print(Me, You, Our, VAT, vat)
print(type(Me), type(You), type(Our), type(VAT), type(vat))

'''
กำหนดคำใบ้ให้กับตัวแปรที่กำหนดไว้ด้านบน เพื่อให้เข้าใจง่ายขึ้น
'''
Me: str = 'metoo'
You: str = 'look nice'
Our: int = 1
VAT: int = 7
vat: float = 0.07
print(Me, You, Our, VAT, vat)
print(type(Me), type(You), type(Our), type(VAT), type(vat))
