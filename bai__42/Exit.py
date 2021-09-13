'''
Hàm exit() dùm để thoát phần mềm
'''
while True:
    s = input("Tên bạn là gì: ")
    print(s)
    ask = input("Bạn có muốn tiếp tục?(c/k):")
    if ask == "k":
        exit()
print("Tạm biệt")