"Hàm jion dùng để nối chuỗi"

s = "sv014-Nguyễn Văn Thanh-05/07/1991"
arr = s.split('-')
for x in arr:
    print(x)

s2 = ","
s2 = s2.join(arr)
print(s2)

a = "Thanh "
b = "Nguyễn"
c = a + b
print(c)