"""
Câu 4:
a) Viết hàm cho phép lưu tập tin dưới dạng text file, yêu cầu khởi tạo là 10
dòng, mỗi dòng có 10 số ngẫu nhiên cách nhau bởi dấu ;

b) Tiếp theo viết hàm cho phép đọc tập tin từ câu a, xuất ra tổng giá trị
của các phần tử trên mỗi dòng
"""

from random import randrange


def CreateMatrix(path):
    file = open(path, 'a', encoding='utf-8')
    matrix = []
    rowSize = 10
    columnSize = 10
    for i in range(rowSize):
        oneRow = []
        for j in range(columnSize):
            oneRow.append(randrange(-100, 100))
        matrix.append(oneRow)

    with open(path, "a"):
        for row in matrix:
            for item in row:
                file.write(str(item) + ";")
            file.write("\n")


def ReadFile(path):
    lst = []
    a = 0
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        for i in range(len(line)):
            a += i
        lst.append(a)
    file.close()
    return lst


def ReturnData(data):
    for row in data:
        print(row, end='\t')
    print()

