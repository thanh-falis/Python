"""
Câu 1 cho x,y,z = 3,5,7 cho biết kết quả boolen Expression
    (a) x==3 -> True
    (b) x<y -> True
    (c) x>=y -> False
    (d) x<=y -> True
    (e) x!=y-2 -> False
    (f) x<10 -> True
    (g) x>=0 and x<10 -> True
    (h) x<0 and x<10 -> False
    (i) x>=0 and x<2 -> True
    (j) x<0 or x<10 -> True
    (k) x>0 or x>10 -> True
    (l) x<0 or x>10 -> False

Câu 2: cho biểu thức
if i<j:
    if j<k:
        i = j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print("i= ", i, "j= ", j, "k= ", k)
Cho biết kết quả in ra màn hình với giá trị i,j,k tương ứng

(a)i=3,j=5,and k=7
    i=5, j=5, k=7

(b)i=3,j=7,and k=5
    i=3, j=5, k=5

(c)i=5,j=3,and k=7
    i=7, j=3, k=7

(d)i=5,j=7,and k=3
    i=5, j=3, k=3

(e)i=7,j=3,and k=5
    i=5, j=3, k=5

(f)i=7,j=5,and k=3
    i=5, j=5, k=3
"""

# Câu 3: Nhập một số n có tối đa 2 chữ số, hãy cho biết cách đọc ra dạng chữ.
'''
number = int(input("Nhập số có 2 chữ số: "))

if number > 10 and number < 100:

    donvi = number % 10
    chuc = number // 10
    dv = ""
    c = ""
    if donvi == 1:
        dv = "mốt"
    elif donvi == 2:
        dv = "hai"
    elif donvi == 3:
        dv = "ba"
    elif donvi == 4:
        dv = "bốn"
    elif donvi == 5:
        dv = "năm"
    elif donvi == 6:
        dv = "sáu"
    elif donvi == 7:
        dv = "bảy"
    elif donvi == 8:
        dv = "tám"
    elif donvi == 9:
        dv = "chín"
    else:
        dv = ""

    if chuc == 1:
        c = "Mười"
    elif chuc == 2:
        c = "Hai mươi"
    elif chuc == 3:
        c = "Ba mươi"
    elif chuc == 4:
        c = "Bốm mươi"
    elif chuc == 5:
        c = "Năm mươi"
    elif chuc == 6:
        c = "Sáu mươi"
    elif chuc == 7:
        c = "Bảy mươi"
    elif chuc == 8:
        c = "Tám mươi"
    elif chuc == 9:
        c = "Chín mươi"

    print(c, dv)
else:
    print("Không đúng 2 số")

# Bài 4: Nhập vào một ngày (d,m,y), tìm ngày kế sau ngày vừa nhập
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) and (d == 29) and (m == 2):
    d_af = 1
    m_af = 3
    y_af = y
    print(d_af, m_af, y_af)
else:
    if (m == 2) and (d <= 28) and (m < 12):
        if d == 28:
            d_af = 1
            m_af = m + 1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d + 1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    elif (m == 4) or (m == 6) or (m == 9) or (m == 11) and (d <= 30) and (m < 12):
        if d == 30:
            d_af = 1
            m_af = m + 1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d + 1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    elif (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) and (d <= 31) and (m < 12):
        if d == 31:
            d_af = 1
            m_af = m + 1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d + 1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    elif (m == 12) and (d <= 31):
        if d == 31:
            d_af = 1
            m_af = 1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d + 1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    else:
        print("nhap sai")

#Câu 5: Nhập vào 2 gái trị a, b và phép toán + - * /. Xuất kết quả theo đúng phép tính đã nhập

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

pheptinh = input("Nhập phép tính: ")
if pheptinh == "+":
    print(a+b)
elif pheptinh == "-":
    print(a-b)
elif pheptinh == "*":
    print(a*b)
elif pheptinh == "/":
    print(a/b)
else:
    print("không đúng phép toán chỉ định")
'''

# Câu 6: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
month = int(input("Nhập tháng: "))
if month > 1 and month <= 12:
    if month in (1, 2, 3):
        print("Tháng ", month, "thuộc quý 1")
    elif month in (4, 5, 6):
        print("Tháng ", month, "thuộc quý 2")
    elif month in (7, 8, 9):
        print("Tháng ", month, "thuộc quý 3")
    elif month in (10, 11, 12):
        print("Tháng ", month, "thuộc quý 4")
else:
    print("Sai tháng")