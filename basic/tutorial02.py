'''
ในไฟล์นี้จะเป็นการแสดงเวอร์ชันของ Python ที่กำลังใช้งานอยู่
โดยการนำเข้าโมดูล sys และใช้ฟังก์ชัน version เพื่อแสดงเวอร์ชันของ Python ที่กำลังใช้งานอยู่
และใช้ฟังก์ชัน python_version จากโมดูล platform เพื่อแสดงเวอร์ชันของ Python ที่กำลังใช้งานอยู่
'''
import sys
print(sys.version)

from platform import python_version
print("Python Version: ", python_version()) 