import math
try:
    r = float(input("Mời bạn nhập bán kính đường tròn:"))
    cv = 2*math.pi*r
    dt = r**2
    print("Chu Vi = ", cv)
    print("Diên tích = ", dt)
except:
    print("Có lỗi xảy ra")