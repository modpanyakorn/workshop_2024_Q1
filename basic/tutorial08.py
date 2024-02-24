'''
ในไฟล์นี้จะเป็นการสรุปการควบคุมทิศทางและการวนรอบใน python
'''

'''
การควบคุมทิศทางแบบ if 
ถ้า condition เป็นจริงให้ทำ statement(s)
###################
if condition:
    statement(s)

###################
'''

val = 8

if val > 7:
    print('This value is over 7')
    print('It is ')
    print(val)


'''
การควบคุมทิศทางแบบ if ... else
ถ้า condition เป็นจริงให้ทำ statement_1(s)
แต่ถ้า condition เป็นเท็จให้ทำอีก statement_2(s)
###################
if condition:
    statement_1(s)
else:
    statement_2(s)

###################
'''

val = 5
if val >7:
    print('This value is over 7')
    print('It is ')
    print(val)
    
else:
    print('This value is under 7')
    print('It is ')
    print(val)


'''
การควบคุมทิศทางแบบ if ... elif
ถ้า condition_1 เป็นจริงให้ทำ statement_1(s)
แต่ถ้า condition_1 ไม่จริงและ condition_2 เป็นจริงให้ทำอีก statement_2(s)
...
แต่ถ้า condition_n ไม่จริงและ condition_n เป็นจริงให้ทำอีก statement_n(s)
แต่ถ้า condition เป็นเท็จทั้งหมดให้ทำอีก statement_0(s)
###################
if condition_1:
    statement_1(s)
elif condition_2:
    statement_2(s)
    ...
elif condition_n:
    statement_n(s)
else:
    statement_0(s)

###################
'''
var = 79
mss = "your grade is "
if var >= 80:
    print (mss+'A')
elif var >= 70:
    print (mss+'B')
elif var >= 60:
    print (mss+'C')
elif var >= 50:
    print (mss+'D')     
else:
    print (mss+'F')

print('FYI')

'''
การควบคุมทิศทางแบบ nested if
คือการใช้เงื่อนไขซ้อนเงื่อนไข
'''

var = 100
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
elif var < 50:
    print("Expression value is less than 50")
else:
    print ("Could not find true expression")
print("Good bye!")

'''
การควบคุมทิศทางแบบวนรอบ หรือทำซ้ำ While loop
เมื่อ condition จริงให้ทำ statement(s)
#######################################
while condition:
    statement(s)
    
#######################################
'''
k=0
print('BEGIN!')
while k<10:
    print('k is',k)
    print('k is updated')
    k += 1
    
print('DONE')

'''
การควบคุมทิศทางแบบวนรอบ หรือทำซ้ำ for loop
ทำคำสั่ง statement(s) ซ้ำไปเรื่อย ๆ จนกว่าจะจบ loop
โดย index จะเป็นตัวที่รัน และ sequence(ลำดับ)จะเป็นตัวกำหนดค่าของ index 
sequence อาจเป็นอะไรก็ได้เช่น string list tupels range เป็นต้น

ถ้า sequence เป็น string => ค่า index จะมีค่าเป็น char แต่ละตัวโดยเรียงตามลำดับใน string
เช่น string = python แล้ว index = p ในรอบการวนซ้ำแรก แล้ว index = y ในรอบการวนซ้ำถัดมา 
    และเป็นเช่นนี้จนถึงรอบวนซ้ำสุดท้าย index = n
    
ถ้า sequence เป็น lis ค่าของ index จะเป็นของใน list เรียงตามลำดับ และเปลี่ยนไปแต่ละรอบการวนซ้ำจนครบ

ถ้า sequence เป็น range ค่าของ index จะเป็นค่าในช่วงที่กำหนด เช่น
    range(n) = {0,1,2,3,...,n-1} ; [n > 0]  
    range(a,b) = {a,a+1,a+2,...,b-2,b-1} ;[a<b เสมอ]  
    
################################################################
for index in sequence:
    statement(s)

################################################################    
'''
print('BEGIN!')
for i in range(10): # range(10) = {0,1,2,3,4,5,6,7,8,9} 
    print('i =',i)
    print('update!')

print('DONE!')

'''
การใช้คำสั่ง break เพื่อจบการวนซ้ำก่อนครบจำนวนรอบ สำหรับ while
ออกจาก while loop โดยใช้คำสั่ง break
################################################################
while condition:
    statement(s)
    if condition:
        break

################################################################

'''

k=0
print('BEGIN!')
while k<10:
    print('k is',k)
    if k == 5 : 
        break
        
    print('k is updated')    
    k += 1    
    
print('DONE') 

'''
การใช้คำสั่ง break เพื่อจบการวนซ้ำก่อนครบจำนวนรอบ สำหรับ for
ออกจาก for loop โดยใช้คำสั่ง break
################################################################
for index in squence:
    statement(s)
    if condition:
        break

################################################################
'''

print('BEGIN!')
for i in range(10):
    print('i =',i)
    if i == 5:
        break
    
    print('update!')
    
print('DONE!')

'''
การใช้คำสั่ง else ร่วมกับ while
สำหรับ python เราสามารถใช้คำสั่ง else ร่วมกับคำสั่ง loop ได้
โดยการใช้ else ร่วมกับ while คำสั่งหลัง else จะทำงานเมื่อ while เป็นเท็จ
################################################################
while condition:
    statement(s)

################################################################
'''

k = 10
print('BEGIN!')
while k < 10:
    print('k is',k)
    print('k is updated')
    k += 1

else:
    print('k is current greater than or equal to 10')
    
print('DONE')  

'''
การใช้คำสั่ง else ร่วมกับ for
สำหรับ python เราสามารถใช้คำสั่ง else ร่วมกับคำสั่ง loop ได้
โดยการใช้ else ร่วมกับ for คำสั่งหลัง else จะทำงานเมื่อทำงานใน for ครบหมดแล้ว
################################################################
for index in squence:
    statement(s)
else:
    statement(s)

################################################################
'''
print('BEGIN!')
for i in range(10):
    print('i =',i)
    print('update!')
    
else:
    print('END!')

print('DONE!')

'''
การใช้คำสั่ง continue ร่วมกับ while
หลักการคือเมื่อเจอคำสั่ง continue โปรแกรมจะไม่ทำคำสั่งหลังจากนั้นทั้งหมด 
และเริ่ม loop ใหม่(ซึ่งต่างจาก break ที่ออกจาก loop ไปเลย)
################################################################
while condition:
    statement_1(s)
    if condition:
        continue
    
    statement_2(s)
    
################################################################
'''
print('BEGIN!')
k=0
while k<10:
    k+=1
    if k%2==1:
        continue
    else:
      print('value is',k)

print('DONE!')

'''
การใช้คำสั่ง continue ร่วมกับ for
หลักการคือเมื่อเจอคำสั่ง continue โปรแกรมจะไม่ทำคำสั่งหลังจากนั้นทั้งหมด 
และเริ่ม loop ใหม่(ซึ่งต่างจาก break ที่ออกจาก loop ไปเลย)
################################################################
for index in squence:
    statement_1(s)
    if condition:
        continue
    
    statement_2(s)
    
################################################################
'''
print('BEGIN!')
for i in range(10):
    if i%2==0:
        continue
    
    print('it is', i, 'it is odd!')

print('DONE!')

