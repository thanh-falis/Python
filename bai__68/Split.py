"""
- Hàm split dùng để tách chuỗi thành mảng các chuỗi con
"""


s = "sv014-Nguyễn Văn Thanh-05/07/1991"
arr = s.split('-')
for x in arr:
    print(x)


s = """
Obama
Trump
HoChiMinh
"""
arr = s.splitlines()
for line in arr:
    print(line)

s = """
sv014-Nguyễn Văn Thanh-05/07/1991
sv015-Nguyễn Thị Đào-02/09/1991
sv016-Hồ Đình Đức-12/05/1991
sv016-Ngô Văn An-7/06/1991
"""
arSv = s.splitlines()
for line in arSv:
    arrInfo = line.split('-')
    if len(arrInfo) == 3:
        print(arrInfo)