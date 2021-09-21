"""
VD: ta có:
lst = [2, 4, 6, 8] tham chiếu tới List
lst[2] -> tham chiếu tới phần tử thứ 2 (giá trị bằng 6)

- 2 ô nhớ khác nhau sẽ quản lý tập giá trị khác nhau dù 2 tập giá trị giống nhau.
- Nếu thay đổi 1 giá trị của 1 trong 2 ô nhớ như trêm thì chỉ ô nhớ đó bị ảnh hưởng.
- giả dụ có a = [10, 20, 30, 40], khi gán b = a thì trên b sẽ trỏ tới ô nhớ mà a đang quản lý.
Khi thay đổi giá trị của trong ô nhớ thì cả a và b đều bị ảnh hưởng.
"""

a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
b[2] = 35
print("a[2] = ", a[2])

'b trỏ tới vùng nhớ a đang quản lý => 1 trong 2 đổi thì cả 2 thay đổi'
b = a
b[2] = 113
print("a[2] = ", a[2])
a[2] = 115
print("b[2] = ", b[2])

'Nhiều đối tượng cùng tham gia quản lý 1 vùng nhớ (Alias)'
c = b
c[3] = 999
print("b[3] = ", b[3])
print("a[3] = ", a[3])
