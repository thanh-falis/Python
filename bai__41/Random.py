'''
Ramdom là một trong những hàm hữu dụng trong viết game, giả lặp dữ liệu và thống kê
'''
from random import randrange
count = 0
while True:
    x = randrange(1, 100)
    print(x, end=',')
    count += 1
    if x == 50:
        break

print("Bye")
print(count)