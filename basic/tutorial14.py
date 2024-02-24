'''
ในไฟล์นี้เราจะเรียนรู้เกี่ยวกับการใช้ boardcasting ใน numpy
ซึ่งเป็นการทำให้ array ขนาดเล็กสามารถดำเนินการกับ array ขนาดใหญ่ได้โดยที่ไม่ต้องเขียน loop
'''

'''
Operator ทางคณิตศาตร์สำหรับ vecotor กับ matrix
broadcasting rule
array ขนาดเล็กจะถูกดำเนินการซ้ำกับ array ขนาดใหญ่กว่าจนกว่าจะเท่ากัน
'''
import numpy as np

a =np.array([[1,2],[3,4],[5,6]],dtype=float)
b =np.array([-1,3],dtype=float)
print(a)
print(b)
print()
print(a+b)