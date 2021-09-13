'''
Hàm eval() có thể tự tính toán chuỗi biểu thức toán học
'''
from math import *
s = "(5*6)-(7/2)+8+sin(0.5)"
x = eval(s)
print(x)


x1, x2 = eval(input("Nhập x1, x2:"))
print("x1= ", x1, "x2= ", x2)