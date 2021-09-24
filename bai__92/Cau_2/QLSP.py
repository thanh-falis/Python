"""
Viết phần mềm quản lý sản phẩm
    - Mỗi danh mục có: Mã, tên; Một danh mục có nhiều sản phẩm.
    - Mỗi sản phẩm có: Mã , tên, đơn giá; mỗi sản phẩm thuộc về 1 danh mục
    - Cho phép: Lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc File
"""


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

