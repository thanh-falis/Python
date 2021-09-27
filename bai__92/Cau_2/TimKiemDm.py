from QLSP import *

data = input("Nhập từ khóa muốn tìm kiếm:")
file = DocFile("danhmucSanpham.txt")
print(file)

print("*"*30)
print("Kết quả tìm kiếm:")
TimKiemDanhMuc(data)