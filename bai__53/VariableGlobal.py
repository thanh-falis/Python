"""
- Tất cả các biến khai báo trong hàm chỉ có phạm vi ảnh hưởng trong hàm,
các biến này gọi là biến local. Khi thoát khỏi hàm thì biến này sẽ không còn truy xuất được nữa.
- Biến Global cho phape tham chiếu đến biến toàn cục
"""
g = 5
def increment():
    global g
    g = 2
    g = g+1
increment()
print(g)


def decrement():
    global x
    x=2
    x-=1
decrement()
print("x = ", x)