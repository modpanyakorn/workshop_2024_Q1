'''
ในไฟล์นี้เราจะเรียนรู้เกี่ยวกับฟังก์ชัน ซึ่งเป็นส่วนสำคัญของการเขียนโปรแกรม
ฟังก์ชันเป็นการรวมคำสั่งที่เราต้องการใช้งานซ้ำ ๆ ในโปรแกรมเดียวกันเป็นกลุ่มเดียวกัน
ซึ่งเราสามารถเรียกใช้งานได้โดยการเรียกชื่อฟังก์ชันนั้น ๆ โดยไม่ต้องเขียนคำสั่งทุกครั้ง
และเราสามารถส่งค่าเข้าไปในฟังก์ชันและรับค่าออกมาจากฟังก์ชันได้ด้วย

และคลาส ซึ่งเป็นการรวมฟังก์ชันหลาย ๆ ฟังก์ชันที่สัมพันธ์กันเป็นกลุ่มเดียวกัน
ซึ่งเราสามารถเรียกใช้งานได้เช่นเดียวกับฟังก์ชัน
แต่คลาสสามารถเก็บค่าตัวแปรได้ด้วย และสามารถเรียกใช้งานฟังก์ชันที่อยู่ภายในคลาสได้ด้วย
และสามารถสร้างคลาสอื่น ๆ ที่สืบทอดคุณสมบัติจากคลาสหนึ่ง ๆ ได้ด้วย
'''

'''
ในโปรแกรมขนาดใหญ่มักจะมีกระบวนการซ้ำ ๆ กันเป็นรูทีน(Routine)
เราสามารถนำงานเหล่านั้นมาเขียนให้อยู่ในฟังก์ชันเดียวเพื่อประหยัดบรรทัดใน code 
และลดความสับสนของคนเขียน(และคนอ่าน code)
โดยที่หากภายในฟังก์ชันมีการใช้ค่าตัวแปรซึ่งอยู่นอกฟังก์ชันเราจำเป็นต้องเขียนให้ฟังก์ชันรับค่า 
Argument(s) ดังตัวอย่างสองและสามด้านล่าง

#################################################
def myfunc():
    Statement(s)

-------------------------------------------------
def myfunc(argument):
    Statement(s)

-------------------------------------------------
def myfunc(argument_1, argument_1, ...,argument_n):
    Statement(s)

#################################################
'''

def func_display():
    print('displays Python !!!')
    
def func_p(n):
    print('The value is',n)
    
def func_ab(a,b):
    if a<b: 
        print('max is', b)
    else:
        print('max is', a)
        
def func_c(a):
    c = 0
    if a<c: 
        print('The value is less than ',c)
    else:
        print('The value is greater than or equal to',c)

def func_p(n):
    if (n%2==0):
        print('The value is', n)
    else:
        print('The value is', 2*n)

'''
การเรียกใช้ฟังก์ชัน ให้พิมพ์ชื่อฟังก์ชันที่กำหนดไว้ตามด้วยวงเล็บและใส่ค่าตัวแปรในวงเล็บ(ถ้ามี)
เช่น myfunc() หรือ myfunc(p) หรือ myfunc(p_1,p_2,...,p_n) เป็นต้น
ซึ่งการใส่ค่า argument ต้องใส่เรียงลำดับตามการนิยามในฟังก์ชัน
'''
func_display()

print() # เว้นบรรทัด

func_p(404)

print() # เว้นบรรทัด

p = -101
func_c(p)

print() # เว้นบรรทัด

func_ab(99,999)


'''
การเรียกฟังก์ชัน โดยใส่ค่า argument(s) โดยปรกติต้องเรียงลำดับที่นิยามไว้
แต่เราก็สามารถใส่แบบไม่เรียงลำดับได้โดยการพิมพ์ชื่อแบบเจาะจง
และนอกจากนี้เราสามารถกำหนดค่า argument(s) ล่วงหน้าเป็นมาตรฐานไว้ได้หากไม่ต้องการใส่ใหม่ทุกครั้ง
#################################################
def funct(argument_1 = value_1, argument_2=value_2):
    statment(s)

-------------------------------------------------
funct()
หรือ
funct(argument_2=a)
หรือ
funct(argument_2=a, argument_1=b)
#################################################
'''

def funct(a_1 = 1, a_2 = -1):
    m = (a_1+a_2)/2
    print(m)

funct()

print() # เว้นบรรทัด

funct(a_1=3)

print() # เว้นบรรทัด

funct(a_2=404,a_1=101)


'''
ในบางครั้งการทำงานของเราต้องการผลลัพธ์เป็นค่าอะไรบางอย่างเพื่อนำไปใช้คำนวณหรือใช้งานอื่น ๆ ต่อไป
การนิยามฟังก์ชันเราสามารถนิยามให้คืนค่าบางอย่างออกมาได้ 
ซึ่งในการเรียกใช้ฟังก์ชันจะต้องมีการนำตัวแปรมารับค่าด้วย
เราสามารถคืนออกมาได้มากกว่าหนึ่งค่า แต่ก็ต้องนำตัวแปรมารับค่าให้มีจำนวนเท่ากันด้วย
#################################################
def func(argument):
    statment(s)
    return value

v = func(a)
-------------------------------------------------
def func(argument):
    statment(s)
    return value_1,value_2
    
u, v = func(a)
#################################################
'''
def func_v(argument):
    value = argument**10
    return value

v = func_v(2)
print(v)

print() # เว้นบรรทัด

def func_uv(argument):
    value_1 = argument**10
    value_2 = -argument**10
    return value_1,value_2

u, v = func_uv(2)
print(u)
print(v)


'''
เราสามารถนำฟังก์ชันหลาย ๆ ฟังก์ชันที่สัมพันธ์กันรวมเข้าด้วยกันเป็นกลุ่มเดียวกันได้เรียกว่า class
ข้อดีของการทำแบบนี้เราจะสามารถสร้างสิ่งที่เรียกว่า module(s) และ package(s) 
ซึ่งเป็นการรวมหลาย ๆ class เข้ามาทำให้เราสามารถนำ code ไปใช้ซ้ำหลาย ๆ ครั้งได้
โดยไม่จำเป็นต้องเขียนใหม่
#################################################
class myClass():
    def myfunc_1()
        statement(s)
        return value
        
    def myfunc_2()
        statement(s)
        return value
        
        ...
    
    def myfunc_n()
        statement(s)
        return value

#################################################
'''

class myClass():
    def func_display():
        print('my class function')
    
    def func_p(n):
        print('The value is',n)
    
    def func_ab(a,b):
        if a<b: 
            print('max is', b)
        else:
            print('max is', a)
        
    def func_c(a):
        c = 0
        if a<c: 
            print('The value is less than ',c)
        else:
            print('The value is greater than or equal to',c)
    
    def func_ca(self, a):
        c = 0
        if a<c: 
            print('The value is less than ',c)
        else:
            print('The value is greater than or equal to',c)

'''
การใช้งาน class ให้เรียกใช้โดยนำชื่อ class ขึ้นต้นและตามท้ายด้วยชื่อฟังก์ชันที่ต้องการใช้เช่นเดียวกับการเรียกฟังก์ชันปรกติ
เช่น myClassName.myfunctionName(argument)
'''

myClass.func_display()

print() # เว้นบรรทัด

myClass.func_p(404)

print() # เว้นบรรทัด

p = -101
myClass.func_c(p)

print() # เว้นบรรทัด

myClass.func_ab(99,999)

mc = myClass()
mc.func_ca(99999)