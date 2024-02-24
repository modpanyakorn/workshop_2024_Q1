'''
ในไฟล์นี้เราจะมาเรียนรู้การใช้งาน matplotlib ในการสร้างกราฟต่างๆ โดยเราจะใช้ข้อมูลจาก numpy ในการสร้างกราฟ
'''
import numpy as np
import matplotlib.pyplot as plt


x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2 # y is now a list with elements of x to the power 2

plt.plot(x, y, 'r')
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show()


x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2
plt.subplot(1,2,1) # subplot(nrows, ncols, plot_number)
plt.plot(x, y, 'r--') # r-- meaning colour red with -- pattern
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-') # g*- meaning colour green with *- pattern
plt.show()

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)
# possible lines type options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')
# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10])# format:line length,space length,..
# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.',..
ax.plot(x, x+9, color='b', lw=3,ls='-', marker='+', markersize=2)
ax.plot(x, x+10, color='b', lw=3, ls='--', marker='o', markersize=4)
ax.plot(x, x+11, color='b', lw=3, ls='-', marker='s', markersize=8)
ax.plot(x, x+12, color='b', lw=3, ls='--', marker='1',markersize=8)
plt.show()

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")
axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")
axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range")
plt.show()

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend()
plt.show()

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
y = x ** 2
fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

plt.show()
fig.savefig('plot.png')