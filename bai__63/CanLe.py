"""
- Hàm rjust se căn phải chuỗi, truyền vào 1 đối số, py thon sẽ chèn khoảng trắng,
nếu có đối số thứ 2 thì chèn nó vào trước chuỗi

- Hàm ljust se căn trái chuỗi, nếu truyền vào 1 đối số, python sẽ chèn khoảng trắng đằng sau chuỗi,
nếu có đối số thứ 2 thì chèn vào sau chuỗi

- Hàm center căn giữa chuỗi, nó tự đẩy khoảng trắng 2 bên sao cho tổng ký tự bằng giá trị muốn truyền vào.
nếu có đối số thứ 2 thì thay khoảng trắng bằng ký tự này
"""
print("Rjust", end='\n\n')
word = "ABCD"
print(word.rjust(10, "*"))
print(word.rjust(3, "*"))
print(word.rjust(15, ">"))
print(word.rjust(10))

'''
- Số lượng ký tự chèn nhỏ hơn chuỗi ký tự gốc thì không có gì thay đổi trừ rjust(3, '*')
'''
print("*"*30)
print("Ljust", end='\n\n')
word = "TRUMP"
print(word.ljust(1))
print(word.ljust(2))
print(word.ljust(3))
print(word.ljust(4))
print(word.ljust(5,))
print(word.ljust(10))
print(word.ljust(10, '*'))

print("*"*30)
print("Center", end='\n\n')

word = "McDonal"
print(word.center(10))
print(word.center(10, '*'))
print(word.center(21, '*'))

