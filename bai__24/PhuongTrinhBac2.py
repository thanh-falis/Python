# Phương trình bậc 2
from math import sqrt

print("Giải Phương trình bậc 2")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a==0:
    #bx+c=0
    if b == 0 and c == 0:
        print("Phương trình có vô số nghiệm")
    elif b == 0 and c != 0:
        print("Vô nghiệm")
    else:
        x = -c/b
        print("Ngiệm x= ", x)
else:
    delta = b**2-4*a*c
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("Nghiêm kép x1=x2=", x)
    else:
        x1 = (-b-sqrt(delta))/(2 * a)
        x2 = (-b+sqrt(delta))/(2 * a)
        print("X1 =", x1)
        print("X2 =", x2)
