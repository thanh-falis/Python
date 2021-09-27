"""
Viết phần mềm quản lý sinh viên
    - Mỗi lớp có: Mã lớp, tên lớp; Mỗi lớp có nhiều sinh viên.
    - Mỗi sinh viên có: Mã, tên, năm sinh; Mỗi sinh viên thuộc 1 lớp.
    - Cho phép: Lưu mới, xóa, tìm kiếm, sắp xếp, lưu và đọc file
"""

import os


def AddClass(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def AddStudent(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def ReadFile(path):
    lst = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(',')
        lst.append(arr)
    file.close()
    return lst


def ReturnData(data):
    for row in data:
        for element in row:
            print(element, end='\t')
        print()
    print()


def Find(path, data):
    file = open(path, "r", encoding='utf-8')
    flag = 0
    index = 0

    for line in file:
        index += 1
        if data in line:
            flag = 1
            break
    if flag == 0:
        print('String', data, 'Not Found')
    else:
        print('String', data, 'Found In Line', index)
    file.close()


def Remove(path):
    os.remove(path)
    print("File Removed!")


def Sort(data):
    for i in range(len(data)):
        for j in range(len(data)):
            a = data[i]
            b = data[j]
            if a[3] < b[3]:
                data[i] = b
                data[j] = a
