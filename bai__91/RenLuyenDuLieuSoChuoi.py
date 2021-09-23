"""
- Cho một tập tin có dữ liệu mỗi dòng như dưới đây:
    5,6,8,9,-5
    -9,5,4,7,8
    6,7,8,3,6,46,7,2,-6,-7

- Viết hàm đọc file, mỗi dòng khởi tạo 1 list và xuất ra màn hình.
- Xuất các số âm trên mỗi dòng ra màn hình
"""


def SaveFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def ReadFile(path):
    arrList = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(',')
        arrList.append(arr)
    file.close()
    return arrList


def outputNegativeNumbers(arr):
    for row in arr:
        for element in row:
            num = int(element)
            if num < 0:
                print(num, end='\t')
        print()