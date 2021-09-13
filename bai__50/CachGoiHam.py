'''
Để gọi hàm cần phải kiểm tra hàm đó được định nghĩa như thế nào
có đối số hay không có đối số.

nếu có kết quả trả về: Result = FuntionName([parameter])
khoogn có kết quả trả về: FuntionName([parameter])
'''
def ptb1(a, b):
    if a == 0 and b == 0:
        return "Vố số nghiệm"
    elif a == 0 and b !=0:
        return "Vô nghiệm"
    else:
        return "x={0}".format(-b/a)

def xuatdulieu(data):
    print(data)

kq1 = ptb1(0, 0)
print(kq1)
kq2 = ptb1(0, 1)
print(kq2)
kq3 = ptb1(6, 7)
print(kq3)

kq4 = ptb1(3, 7)
xuatdulieu(kq4)

a = xuatdulieu(kq4)
print(a)