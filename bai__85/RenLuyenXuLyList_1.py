"""
Viết chương trình cho phép:
    - Viết lệnh khởi tạo ngâu nhiên n phần tử cho list
    - Gọi k là một số nhập từ bàn phím,
        hãy xóa tất cả các phần tử có giá trị k tồn tại trong list.
    - Kiểm tra list có đối xứng không
"""
from random import randrange

lst = []
print("Nhập số phần tử: ")
n = int(input())
for i in range(n):
    lst.append(randrange(0, 100))
print("List khởi tạo ngẫu nhiên:")
print(lst)
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print(lst)
k = int(input("Nhập phần số để xóa: "))
for i in lst:
    if i == k:
        lst.remove(i)
print("List sau khi xóa:")
print(lst)


def Check(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst)-i-1]:
            return False
    return True


check = Check(lst)

if check == True:
    print("List đối xứng")
else:
    print("List không đối xứng")


