def usc(a, b):
    """Hàm này dùng để tìm ước số chung lớn nhất
        Ví dụ: a=9, b=6 thì Ước lớn nhất = 3
    """
    min = a if a < b else b
    for i in range(min, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

uoc = usc(9,6)
print(uoc)