"""
Viết chương trình cho phép:
    - Khởi tạo list
    - Thêm phần tử vào list
    - Nhập K, kiểm tra K xuât hiện bao nhiêu lần trong list
    - Tính tổng các số nguyên tố trong list
    - Sắp xếp
    - Xóa list
"""
from random import randrange

print("Chương trình xử lý list")
n = int(input("Nhập só phần tử: "))
lst = [0] * n
for i in range(n):
    lst[i] = randrange(-100, 100)
print("List đa chiều ngẫu nhiên:")
print(lst)
print("Mời bạn nhập thêm số mới:")
value = int(input())
lst.append(value)
print(lst)
print("Bạn muốn đếm số nào")
k = int(input())
cnt = lst.count(k)
print(k, "Xuất hiện trong list: ", cnt, "lần")


def CheckPrime(n):
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2


cnt = 0
snt = 0
for j in lst:
    if CheckPrime(j):
        cnt += 1
        snt += j
print("Có ", cnt, "số nguyên tố trong list")
print("Tổng =", snt)
lst.sort()
print("List sau khi sort")
print(lst)

del lst
print("List sau khi xóa")
print(lst)
