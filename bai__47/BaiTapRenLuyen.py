'''
Câu 1: Những giá trị nào có thê xuát hiện khi chạy lệnh randrange(0, 100)
4.5, 34, -4, 100, 0, 99

    - Những giá trị có thể xuất hiện: 34, 0, 99

Câu 2: Nhập tọa độ 2 điểm  A(xa, ya), B(xb, yb), tính và xuất độ dài đoạn AB

    from math import *
    xa, ya = eval(input("Nhập tọa độ xa, ya:"))
    xb, yb = eval(input("Nhập tọa độ xb, yb:"))

    d = sqrt((xb - xa)**2 + (yb - ya)**2)
    dai  = round(d,2)
    print("Độ dài đoạn AB = ", dai)

Câu 3: Viết chương trình tính logax với a, x là các số thực nhập từ bàn phím,
và x>0, a>0, a!=1.

    from math import *
    print("Chương trình tính Log")
    a = float(input("Nhập a:"))
    x = float(input("Nhập x:"))
    if x<0 or a<0:
        print("Nhập số lớn hơn 0")
        if a is 1:
            print("Cơ số a phải khác 1")
    else:
        logax = log(e, x)/log(e, a)

    print(logax)

'''
