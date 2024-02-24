'''
ในไฟล์นี้เราจะมาเรียนรู้เกี่ยวกับการใช้งาน module(s) และ package(s) ใน Python
โดย module(s) คือการรวมหลาย ๆ class หรือ function(s) ให้เป็นกลุ่มเดียวกัน
และ package(s) คือการรวมหลาย ๆ module(s) ให้เป็นกลุ่มเดียวกัน
'''

'''
หลาย ๆ functions รวมเป็น a class [บางครั้ง class ก็มี a function ได้]
หลาย ๆ classes รวมเป็น a module  
หลาย ๆ modules รวมเป็น a package

ในการทำ Machine Learning ด้วย Python มี package(s) หลาย ๆ อันที่ถูกสร้างขึ้นมาให้ใช้งาน
เช่น numpy scipy sklearn pandas seaborn เป็นต้น
โดยการจะใช้งาน package(s)เหล่านี้เราต้องนำเข้า(import)ก่อน และเมื่อจะใช้ฟังก์ชันใด ๆ ให้มอง module(s) เป็นเสมือน class อย่างหนึ่ง

การนำเข้า module(s) และ package(s)  
import [packageName] 
หรือกำหนด shortName เพื่อประหยัดเวลาในการเรียกใช้
import [packageName] as [shortName] 
หรือเราจะนำเข้าเพียง a module ที่เราต้องการก็ได้
from [packageName] import [moduleName]
หรือจะนำเข้าเข้าเพียง a function/a class ที่เราต้องการก็ได้
from [packageName.moduleName] import [functionName/className]
'''

import numpy
import numpy as np
from numpy import linalg
from numpy import linalg as la
from numpy.linalg import multi_dot


'''
NumPy เป็น module Python สำหรับการจัดการ NumPy Array/nArray(matrices) และการคำนวณคณิตศาสตร์

Array เป็นข้อมูลประเภทหนึ่งลักษณะคล้าย list แต่ข้อมูลใน array ต้องเป็นชนิดเดียวกันทั้งหมด
'''
import numpy

aray = numpy.array(range(3,7))          # สร้าง vector จาก range(3,7)={3,4,5,6}
araya = numpy.array([ [1,2], [3,4] ])   # สร้าง matrix ที่แถวแรกเป็นเวกเตอร์ [1,2]
                                        # และแถวที่สองเป็นเวกเตอร์ [3,4]
print(aray)
print(araya)


'''
เราสามารถเข้าถึงข้อมูลใน array โดยการใช้คำสั่งคล้ายกับที่ทำกับ list หรือ string
------------------------------
 :  เอาทุกตำแหน่ง
a:  เลือกเฉพาะ index ตั้งแต่ a เป็นต้นไป
 :b เลือกเฉพาะ index 0 ไปจนถึง b-1
a:b เลือกเฉพาะ index = a,a+1,a+2,...,b-1
------------------------------
'''

print(aray[0]) # สมาชิก index 0 ใน aray
print(aray[1:3]) # สมาชิก index 1,2 ใน aray

print(araya[0]) # เวกเตอร์แถวที่ index 0 ใน araya
print(araya[0,1]) # สมาชิกแถวที่ index 0 และคอลัมน์ที่ index 1 ใน araya [สมาชิกตำแหน่ง(0,1)]
print(araya[:,1]) # เวกเตอร์คอลัมน์ที่ index 1 ใน araya


'''
shape   รูปร่างของarray
size    จำนวนสมาชิกในarray
ndim    จำนวนมิติของarray
'''

print(aray.shape) # ได้ (4,)
print(aray.size) # ได้ 4
print(aray.ndim) # ได้ 1

print(araya.shape) # ได้ (2, 2)
print(araya.size) # ได้ 4
print(araya.ndim) # ได้ 2


'''
การเขียนทับข้อมูลใน
เหมือนกับ list arrayก็สามารถเขียนทับแก้ข้อมูลข้างในเมื่อไหร่ก็ได้ด้วยการใส่ค่าทับลงไป 
'''

aruy = np.array([[1,1,1],[2,2,2],[3,3,3]])
print(aruy)

print()

aruy[1,1] = 0
print(aruy)