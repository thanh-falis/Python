"""
-Với Python chúng ta có thể duyệt list theo nhiều cách. Bài học hướng dẫn 2 cách sau:
    Duyệt theo collection
    Duyệt theo chỉ số index

"""
from random import randrange

print("Mời bạn nhập số phần tử:")
n = int(input())
lst = [0]*n
for i in range(n):
    lst[i] = randrange(-100, 100)
print(lst)

print("Duyệt theo collection:")
for x in lst:
    print(x, end='\t')

print("\n Duyệt theo Index:")
for i in range(len(lst)):
    print("Vị trị ", i, "có giá trị = ", lst[i])

print("\n Duyệt ngược danh sách:")
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end='\t')
