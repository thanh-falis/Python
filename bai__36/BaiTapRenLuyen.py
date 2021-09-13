'''
Câu 1: Cho biết bao nhiêu dấu * được in ra màn hình
    a = 0
    while a<100:
        print('*', end='')
    print()

   - Có 100 dấu * được in ra màn hình (từ 0 đến 99)

Câu 2: Cho biết bao nhiêu dấu * được in ra màn hình
    a = 0
    while a < 100:
        b = 0
        while b < 40:
            if (a+b) % 2 == 0:
                print('*', end='')
            b += 1
        print()
        a += 1

    - Có 2000 dấu * được in ra màn hình

Câu 3: Giải thích cách chạy các dòng lệnh range():

    (a) range(5)                 -> chạy từ 0 -> 4, bước nhảy là 1
    (b) range(5, 10)             -> chạy từ 5 đến 9
    (d) range(5, 20, 3)          -> chạy từ 5 đến 19 , bước nhảy là 3
    (e) range(20, 5, -1)         -> chạy từ 20 về 5, bước nhảy là -1
    (f) range(20, 5, -3)         -> chạy từ 20 về 5, bước nhảy là -3
    (g) range(10, 5)             -> trả về 1 chuổi rỗng
    (h) range(0)                 -> trả về 1 chuỗi rỗng
    (i) range(10, 101, 10)       -> chạy từ 10 đến 100, bước nhảy là 10
    (j) range(10, -1, -1)        -> chạy từ 10 về -1, bước nhảy là -1
    (k) range(0, 10, 1)          -> chạy từ 0 đến 9, bước nhảy là 1

Câu 4: Bao nhiêu dấu * được in ra màn hình
    for a in range(20, 100, 5):
        print('*', out='')
    print()

    - có 16 dấu * được in ra màn hình

Câu 5: Viết lại coding dưới đây bằng cách dùng tù khóa break thay thế cho biến done:
    done = False
    n, m = 0, 100
    while not done and n != m:
        n = int(input())
        if n < 0:
            done = True
        print("n = ", n)
'''

done = False
n, m = 0, 100
while not done and n != m:
    n = int(input("Nhập n: "))
    if n < 0:
        break
    print("n = ", n)


# Câu 6: vẽ hình
# hình vuông rỗng
n = 4
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == n-1:
            print("*", end='')
        else:
            print(' ', end='')
    print()


