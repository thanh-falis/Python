"""
- Một chuỗi được gọi là tối ưu khi: không chứa khoảng trắng dư thừa,
các từ cách nhau bằng 1 khảng trắng
"""

def ToiUuChuoi(s):
    s1 = s
    s1 = s1.strip()
    arr = s1.split(' ')
    s2 = ""
    for x in arr:
        word = x
        if len(word.strip()) != 0:
            s2 = s2+word+" "
    return s2.strip()

s = " Nguyễn  Văn   Thanh  "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))