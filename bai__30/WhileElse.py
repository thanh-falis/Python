# Else giống như 1 kết luận sau khi lệnh while thực hiện xong nhưng không vào break

count = sum = 0
print("Nhập 5 số >= 0")
while count < 5:
    val = int(input("Nhập giá trị: "))
    if val < 0:
        print("Nhập sai quy tắc")
        break
    sum += val
    count += 1
else:
    print("Trung bình bằng: ", sum/count)