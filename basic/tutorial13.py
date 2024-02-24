'''
ในไฟล์นี้เราจะมาดูการใช้งาน numpy ในการคำนวณทางคณิตศาสตร์
'''

'''
Operator ทางคณิตศาตร์สำหรับ vectors
สามารถทำได้เหมือนกับการคำนวณตัวเลขปรกติ แต่จะเป็นลักษณะ elementwise (สมาชิกต่อสมาชิก)
'''
import numpy as np

a =np.array([1,2,3],dtype=float)
b =np.array([5,1,8],dtype=float)
print(a,b)

print()

print(a+b)    # การบวกแบบ elementwise [การบวกปรกติของ vector]
print(a-b)    # การลบแบบ elementwise [การลบปรกติของ vector]
print(a*b)    # การคูณแบบ elementwise
print(a/b)    # การหารแบบ elementwise
print(a%b)    # การหารเอาเศษแบบ elementwise
print(a**b)   # การยกกำลังแบบ elementwise

'''
Operator ทางคณิตศาตร์สำหรับ matrices
ทำได้ในทำนองเดียวกันกับ vectors ให้ผลเป็นลักษณะ elementwise 
'''
a =np.array([[1,2],[3,4]],dtype=float)
b =np.array([[2,0],[1,3]],dtype=float)
print(a)
print(b)
print()
print(a*b) # การคูณแบบ elementwise สำหรับ matrices

print()

print(np.dot(a,b)) # การคูณ matries ปรกติ

print()

print(np.dot(np.array([1,2,3]),np.array([2,3,4]))) # ถ้าเป็น vectors จะเป็นการทำ inner product แทน

print()

print(np.cross(np.array([1,2,3]),np.array([2,3,4]))) # สามารถทำการ cross vectors ได้ผ่าน cross


'''
โดยทั่ว ๆ ไป
การใช้ operator(s) ทางคณิตศาสตร์สำหรับ narray จะเป็นการทำงานแบบ elementwise ทั้งหมด
ต่อไปนี้คือ operators ที่เราใช้งานได้
np.abc, ค่าสัมบูรณ์ 
np.sign, ถ้าค่ามากกว่า 0 ให้เปลี่ยนเป็น 1 น้อยกว่าให้เป็น -1
np.sqrt, รากที่ 2 
np.log, ค่า log ฐาน e
np.log10, ค่า log ฐาน 10
np.exp, e ยกกำลังด้วยของใน array
np.sin, 
np.cos, 
np.tan, 
np.arcsin, 
np.arccos, 
np.arctan, 
np.sinh, 
np.cosh, 
np.tanh, 
np.arcsinh, 
np.arccosh, 
np.arctanh, 
np.floor, 
np.ceil, 
np.rint, 
np.radians, แปลงมุมจากองศาเป็น radian
np.degrees, แปลงมุมจาก radian เป็นองศา
np.pi, ค่า pi
np.e ค่า e
'''

print(np.pi,np.e)

print()

ari1 = np.arange(1,9)
print(ari1)
print(np.sin(ari1))
print(np.log(ari1))
print(np.exp(np.log(ari1)))
print(np.log(ari1)/np.log(2))  # log ฐาน 2


'''
Operators ทางสถิติที่น่าสนใจ
sum(),
prod(),
mean(), 
var(),
std(),
max(),
min(),
argmax(), หาตำแหน่งที่มีค่ามากสุด
argmin(), หาตำแหน่งที่มีค่าน้อยสุด
'''
a =np.array([2,4,3],float)
print(a.sum())
print(a.prod())

c =np.array([[0,-2],[3,-1],[3,-5]],float)
print(c.sum())

print()
print(a.mean())
print(a.var())
print(a.std())

print()
print(a.max())
print(a.min())
print(a.argmax())
print(a.argmin())

a =np.array([2,4,3],float)
print(a.sum())
print(a.prod())
print(a.cumsum()) # cumulative sum
print(a.mean())
print(a.var())
print(a.std())

''' 
ในกรณีที่เป็น matrix เราสามารถกำหนดแกน(axis)ที่ต้องการคิดได้โดยผลที่ได้จะออกมาเป็น vactor แทนที่จะเป็นจำนวนเดียว
ซึ่ง axis=0 หมายถึงตามแนว column และ axis=1 หมายถึงตามแนว row 
'''
a =np.array([[0,-2],[3,-1],[3,-5]],float)
print(a)
print(a.mean(axis=0))
print(a.mean(axis=1))
print(a.min(axis=1))
print(a.max(axis=0))
print(a.argmin(axis=0))
print(a.argmax(axis=1))


'''
สำหรับการดำเนินการ matrices อื่น ๆ ที่น่าสนใจมีดังนี้
array.transpose()   สร้าง transpose matrix ของ array
array.flatten()     สร้าง array มิติเดียวโดยการตัดทุกแถวของ array มาต่อกัน
array.trace()       หาค่า trace ของ array
'''
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]],dtype=float)
print(a)
print(a.transpose())

print()

print(a.flatten())

print()
print(b)
print(np.trace(b))


