"""
Câu 1: Cho 3 hàm dưới đây:
def sum1(n):             def sum2():                def sum3():
    s = 0                   global val                  s = 0
    while n>0:              s = 0                       for i in range(val,0, -1):
        s += 1              while val > 0:                  s += 1
        n -= 1                  s += 1                  return s
    return s                    val -= 1
                            return s

Hãy cho biết kết quả sau khi gọi các lệnh trên

Câu a:                      Câu b:                  Câu c:
def main():                 def main():                 def main():
    global val                  global val                  global val
    val = 5                     val = 5                     val = 5
    print(sum1(5))              print(sum1(5))              print(sum2())
    print(sum2())               print(sum3())               print(sum1(5))
    print(sum3())               print(sum2())               print(sum2())

Kq: 5                            5 5                        rỗng
"""
"""
Câu 2: Viết hàm tính tổng ước số đẻ áp dụng chung cho 2 bài dưới đây:
    - Kiểm tra số nguyên dương n có phải là số hoàn thiện hay không?.
    Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
    - Kiểm tra số nguyên dương n có phải là số thịnh vượng hay không?.
    Số thịn vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn nó.
"""


def TongUocSo(n):
    s = 0
    if n <= 0:
        return "Phải là số nguyên dương"
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return n, "Là số hoàn thiện"
    elif s > n:
        return n, "Là số thịnh vượng"


print(TongUocSo(6))
print(TongUocSo(12))

