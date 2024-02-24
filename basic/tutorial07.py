'''
ในไฟล์นี้จะเป็นการอธิบายเกี่ยวกับ composite data types
- List
- Tuple
- Dictionary
- Set
'''

'''list เก็บข้อมูลหลาย ๆ ค่า ต่างชนิดกันคล้าย array (แต่ array เก็บได้ชนิดเดียว)'''

ls = [] # list ว่างเปล่า
print(type(ls))

print()

ls = [1,2,3]
print(type(ls))
print(ls)

# operators อื่นสามารถทำได้เหมือนกับ string

'''
เก็บข้อมูลได้หลายค่าหลายชนิดคล้าย list แต่มีขนาดคงที่คล้าย array
ทำให้เพิ่มหรือลบอะไรออกโดยตรงไม่ได้ มีข้อดีคือหาข้อมูลใน tuples ได้เร็ว
'''

tup = (12,5)
print(type(tup))
print(tup)

print()
tup = ('love you',3000)
print(type(tup))
print(tup)

print()
tup = (('I am','inevitable.'),('I am','iron man.'))
print(type(tup))
print(tup)

'''
เก็บข้อมูลได้หลายตัวแปรหลายชนิด และยืดหยุ่นมีขนาดเพิ่มขึ้นลดลงได้
โดยมีแนวคิดในการเก็บข้อมูลแบบใช้ key:value แทนการใช้ index อย่างเดียวแบบ list tuples หรือ array
ทำให้เข้าถึงข้อมูลได้จำเพาะกว่า 
ซึ่ง key จะต้องไม่ซ้ำกันใน dictionary เดียวกัน
'''

dic = {} # ดิกชันนารีว่างเปล่า
print(type(dic))
print(dic)

print()

dic = {'Me': 'me too'}
print(type(dic))
print(dic)

print()

dic = {'Thanos': 1, 'Avengers': 3000}
print(type(dic))
print(dic)

print()

dic = {'I therefore': 'you', 1: 3000}
print(type(dic))
print(dic)


''' 
เซตในทางคณิตศาสตร์ สามารถทำการดำเนินการทางคณิตศาสตร์ได้
ยูเนียน อินเตอร์เซคชัน ผลต่าง ผลต่างสมมาตร การเป็นสมาชิก
'''

X = set() # เซตว่าง เรา'ไม่'สามารถใช้ X = {} ได้ เพราะมันจะเป็นดิกชันนารี
print(type(X))
print(X)

print()

X = {'apple', 'papaya', 'banana', 'orange'}
print(type(X))
print(X)

print()

X = set(('apple', 'papaya', 'banana', 'orange')) # อีกวิธีในการเขียนเซต
print(type(X))
print(X)


S1=set((1,1,2,3,5,8,13))
S2=set((2,3,5,7,11,13))
print(S1,S2)

print()

print(S1|S2) # ยูเนียน
print(S1&S2) # อินเตอร์เซคชัน
print(S1-S2) # ผลต่าง
print(S1^S2) # ผลต่างสมมาตร (เอาทุกสมาชิกของทั้งสองเซตยกเว้นตัวที่ซ้ำกัน)

print()
print(1 in S1) #ตรวจสอบว่า 1 อยู่ใน set หรือไม่
print()
print(1 not in S1) #ตรวจสอบว่า 1 [ไม่]อยู่ใน set หรือไม่