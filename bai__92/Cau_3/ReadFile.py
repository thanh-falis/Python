from QLSV import *
print("Danh sách Lớp học \n")
cls = ReadFile("Class.txt")
ReturnData(cls)

print("*"*30)
print("Danh sách sinh viên \n")
student = ReadFile("Student.txt")
ReturnData(student)