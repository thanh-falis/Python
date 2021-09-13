# Tương tự như While Else, sau khi for thực hiện nhưng không vào câu lệnh break thi sau đó else sẽ thực hiện

a = int(input("Nhập số nguyên: "))
s = 0
for n in range(5, 10):
    if 4 % a is 1:
        print("Ngừng lặp")
        break
    s += n
else:
    print("sum = ", s)