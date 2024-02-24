'''
ในไฟล์นี้เราจะมาเรียนรู้การสร้าง
การสร้างตัวแปรสุ่มจากการใช้ฟังก์ชัน
random.normal และ random.normal ในไลบรารี numpy
'''
import numpy as np

rv = np.random.normal(0,1,1) # rv ~ N(0,1)
print(rv)

n = 100
rv_vec = np.random.normal(0,1,n)
rv_vec

print('The mean is', np.mean(rv_vec))
print('The SD is', np.std(rv_vec))