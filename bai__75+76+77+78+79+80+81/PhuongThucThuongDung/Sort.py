"""Python hỗ trợ hàm sort để sắp xếp list"""
from random import randrange

lst = [0]*10
for i in range(len(lst)):
    lst[i] = randrange(100)
print(lst)

lst.sort()
print(lst)
print("*"*20)
lst = [4, 2, 10, 8]
print(lst)

#sorted ko làm thay đổi bản chất của chuỗi

lst1 = sorted(lst)
print(lst1)
print(lst)
print("*"*20)
# Sắp xếp giản dần
lst = [2, 3, 8, 10]
print(lst)
lst.sort(reverse=True)
print(lst)
