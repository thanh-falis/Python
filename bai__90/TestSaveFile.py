from SaveAndReadFile import *
id = input("Nhập mã sản phẩm: ")
name = input("Nhập tên sản phẩm: ")
sal = float(input("Nhập đơn giá sản phẩm: "))
line = id+";"+name+";"+str(sal)
SaveFile("database.txt", line)