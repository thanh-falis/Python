print("mời bạn nhâp một giá trị")
s = input()
print("Bạn nhập", s)
print("Kiểu dữ liệu:", type(s))

# Muốn đưa về số int
print("mời bạn nhâp kiểu int")
a = int(input())
print("Bạn nhập", a)
print("Kiểu dữ liệu:", type(a))

# Muốn đưa về số float
print("mời bạn nhâp kiểu float")
x = float(input())
print("Bạn nhập", x)
print("Kiểu dữ liệu:", type(x))


# Muốn đưa về số boolean
# định nghĩa

def StrToBool(s):
    return s.lower() in ("yes", "true", "t", "1")


print("mời bạn nhâp kiểu bool")
x = StrToBool(input())
print("Bạn nhập", x)
print("Kiểu dữ liệu:", type(x))

# truyền chuỗi vào input

x = input("mời bạn nhập giá trị nào đó")
print("bạn nhập", x)

