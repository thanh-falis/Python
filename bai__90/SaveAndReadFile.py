"""
- Viết chương trình nhập vào thông tin của 1 sản phẩm với:
    Mã: Chuỗi
    Tên: Chuỗi
    Đơn giá: Số
- Mỗi 1 sản phẩm sau khi nhập thành công sẽ lưu nối đuôi vào File theo quy tắc:
    MSSP; Tên; Đơn giá
1) Xuất danh sách sản phẩm từ File
2) Sắp xếp sản phẩm theo đơn giá giảm dần
"""


def SaveFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def ReadFile(path):
    arrProduct = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct


def returnProduct(dssp):
    for row in dssp:
        for element in row:
            print(element, end='\t')
        print()
    print()


def sortProduct(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a = dssp[i]
            b = dssp[j]
            if a[2] > b[2]:
                dssp[i] = b
                dssp[j] = a


