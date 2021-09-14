"""
- Python hỗ trợ kahi báo hàm nực danh thông qua Lambda expression:
    lambda parameterlist: expression
- lambda: là từ khóa
- parameterlist: tập hợp các parameter ta muốn định nghĩa
- expression: biểu thức đơn trong Python (không nhập complex)
"""


def handle(f, x):
    return f(x)


kq1 = handle(lambda x: x % 2 == 0, 9)
print(kq1)
kq2 = handle(lambda x: x % 2 == 0, 4)
print("kq2 = ", kq1)

def SoChan(x):
    return x % 2 == 0


kq3 = handle(SoChan, 4)
print("kq3 = ", kq3)
kq4 = handle(SoChan, 5)
print("kq4 = ", kq4)
kq5 = handle(lambda x: SoChan(x), 7)
print("kq5 = ", kq5)

