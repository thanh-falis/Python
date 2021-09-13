'''
Hàm clock() trả về số giây ngay thời điểm hiện tại
Hàm sleep() giúp tạm dừng chương trình trong một đơn vị thời gian nào đó
'''

from time import *
start = clock()
print("Nhập 1 giá trị: ")
x = input()
print("Bạn nhập: ", x)
end = clock()
duration = end-start
print("duration = ", duration)

start = clock()
for x in range(100):
    print(x, end='')
end = clock()
durationfor = end-start
print("duration for = ", durationfor)


# sleep

for x in range(10):
    print(x)
    sleep(1)