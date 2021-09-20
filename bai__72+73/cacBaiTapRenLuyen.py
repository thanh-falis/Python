"""
Câu 1: Trình bày một số hàm quan trọng trong xử lý chuỗi của Pyhton:

-Các hàm xử lý chuỗi:
    upper, lower:       Xử lý in hoa, in thường
    rjust:              Căn lề phải
    ljust:              căn lề trái
    center:             Căn giữa
    strip:              Xóa khoảng trắng due thừa
    startswith:         Kiểm tra chuỗi có phải bắt đầu là ký tự?
    endswith:           Kiểm tra chuỗi có phải kết thúc là ký tự?
    count:              Đếm số lần xuất hiện trong chuỗi
    find:               Tìm kiếm chuỗi
"""
import string

"""
Câu 2: Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ in hoa
- Bao nhieu chữ in thường
- Bao nhiêu là chữ số
- Bao nhiêu là ký tự đặc biêt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là nguyên âm
- Bao nhêu chữ là phụ âm
"""
import re


def checkString(s):
    print("Ký tự in hoa: ", sum(1 for c in s if c.isupper()))
    print("Ký tự thường: ", sum(1 for c in s if c.islower()))
    print("Chữ số: ", sum(1 for c in s if c.isnumeric()))
    special_char(s)
    check_space(s)
    CountVO(s)
    CountCon(s)


def special_char(s):
    count = 0
    for i in range(0, len(s)):
        if s[i].isalpha():
            continue
        elif s[i].isdigit():
            continue
        elif s[i] == ' ':
            continue
        else:
            count += 1
    if count >= 1:
        print("Ký tự đặc biệt", count)
    else:
        print("Không có ký tự đặc biệt")


def check_space(s):
    count = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            count += 1
    return count


def CountVO(s):
    char = ["a", "ă", "â", "e", "ê", "i", "o", "ô", "ơ", "u", "ư", "y"]
    count = 0
    for i in range(0, len(s)):
        for j in char:
            if s[i] == j:
                count += 1
    print("Nguyên âm: ", count)


def CountCon(s):
    char = ["b", "c", "d", "đ", "g", "h", "h", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x"]
    c = 0
    for a in range(0, len(s)):
        for b in char:
            if s[a] == b:
                c += 1
    print("Phụ âm: ", c)


def main():
    print("Nhập chuỗi: ")
    s = input()
    checkString(s)


main()

"""
Câu 3: 
"""


def NegativeNumberInString(s):
    result = [int(d) for d in re.findall(r'-?\d+', s)]
    num = []
    for i in result:
        if i < 0:
            num.append(i)
    return num


def main():
    s = 'abc-5xyz-12k9l--p'
    print(NegativeNumberInString(s))


main()
