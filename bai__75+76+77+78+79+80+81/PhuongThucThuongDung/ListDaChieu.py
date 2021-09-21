"""
Python hỗ trọ list đa chiều
"""
from random import randrange

lst = [
    [4, 2, 10],
    [7, 10, 5],
    [-7, 9, 2],
]

print(lst)
print("*"*30)
# Xuất theo collection
for row in lst:
    for colum in row:
        print(colum, end='\t')
    print()

print("*"*30)
# Xuất theo vị trí
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end='\t')
    print()

arr2D = []
rowSize = int(input("Nhập số dòng: "))
columnSize = int(input("Nhập số cột: "))
for i in range(rowSize):
    oneRow = []
    for j in range(columnSize):
        oneRow.append(randrange(-100, 100))
    arr2D.append(oneRow)

print("Ma trận do máy nhập là:")
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j], end='\t')
    print()
