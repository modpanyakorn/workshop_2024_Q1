'''
ในไฟล์นี้เราจะมาเรียนรู้การใช้งาน matplotlib ในการสร้างกราฟต่างๆ โดยเราจะใช้ข้อมูลจาก numpy ในการสร้างกราฟ
'''

import numpy as np
import matplotlib.pyplot as plt
from random import sample


x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
y = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
plt.scatter(x,y)
plt.show()

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2
plt.scatter(x,y)
plt.show()

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2
plt.plot(x, y, "b") # 'b' = blue color
plt.show()

data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
# rectangular box plot
plt.boxplot(data,patch_artist=True)
plt.show()