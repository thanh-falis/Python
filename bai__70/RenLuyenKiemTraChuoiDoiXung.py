"""
- Dùng vòng lặp While vĩnh cửu, cho phép nhập chuỗi -> xuất chuỗi này có phải đối xứng hay không,
hỏi người sử dụng có tiếp tục phần mềm. Nếu tiếp tục thì nhập chuỗ mới else thoát và cảm ơn
"""

def check(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            flag = False
            break
        return flag

def main():
    print("Nhập chuỗi:")
    s = input()
    if check(s):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")


main()