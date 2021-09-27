"""
Viết phần mềm quản lý sản phẩm
    - Mỗi danh mục có: Mã, tên; Một danh mục có nhiều sản phẩm.
    - Mỗi sản phẩm có: Mã , tên, đơn giá; mỗi sản phẩm thuộc về 1 danh mục
    - Cho phép: Lưu mới, xóa, tìm kiếm, sắp xếp, lưu và đọc File
"""
import os

def TaoDanhMuc(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def TaoSanPham(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def DocFile(path):
    lst = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(',')
        lst.append(arr)
    file.close()
    return lst


def Return(data):
    for row in data:
        for element in row:
            print(element, end='\t')
        print()
    print()


def TimKiemDanhMuc(data):
    file = open("danhmucSanpham.txt", "r", encoding='utf-8')
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


def remove_line(path):
    os.remove(path)
    print("File Removed!")


def SapXepSanPham(data):
    for i in range(len(data)):
        for j in range(len(data)):
            a = data[i]
            b = data[j]
            if a[3] > b[3]:
                data[i] = b
                data[j] = a
