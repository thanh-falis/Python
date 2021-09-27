from QLSV import *
lst = ReadFile("Class.txt")
ReturnData(lst)
print("")
data = input("Nhập từ khóa: ")
Find("Class.txt", data)

print("")
lst1 = ReadFile("Student.txt")
ReturnData(lst1)
print("")
data = input("Nhập từ khóa: ")
Find("Student.txt", data)
