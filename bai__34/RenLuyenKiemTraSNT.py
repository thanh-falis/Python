while True:
    n = int(input("Nhập 1 số nguyên dương: "))
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, "Là số nguyên tố")
    else:
        print(n, "Không phải là số nguyên tố")
    ask = input("Bạn có muốn tiế tục?(c/k):")
    if ask is "k":
        break
    print("Chào tạm biệt")