'''
Cấu trúc hàm trong python
    def name (parameter list)

từ khóa def dùng để định nghĩa hàm
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