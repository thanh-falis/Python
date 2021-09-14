"""
- Python hỗ trợ parameter mặc định khi khai báo hàm
- Hàm print() thường dùng cũng có parameter mặc định
"""

def fl(n, m = 0):
    s = 0
    for i in range(1, n + m, 1):
        s += 1
    return s
print(fl(5))
print(fl(5, 1))

def fl2(n, m = 1, k = 2):
    s = 0
    for i in range(1, m+n+k, 1):
        s += i
    return s
print("*"*30)
print(fl2(5))
print(fl2(5, 3))
print(fl2(5, 3, 1))
print(fl2(5, k=4))
