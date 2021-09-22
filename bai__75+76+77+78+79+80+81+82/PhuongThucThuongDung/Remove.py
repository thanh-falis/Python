"""
- Python hỗ trợ phương thức remove, xóa phần tử trong list
"""
lst = [113, 20, 30, 44, 25, 16, 27, 44]
lst.remove(20)
print(lst)
lst.remove(44)
print(lst)

del lst[0]
print(lst)
del lst[1:4]
print(lst)
lst = [15, 10, 20, 18]
del lst[1], lst[2]
"""
- Lệnh trên sẽ xóa lst[1] trước, ta còn lst = [15, 20, 18]
- Sau đó sẽ xóa tuần tự đến lst[2].
- Giá trị sau cùng sẽ là lst = [15, 20]
"""
print(lst)
