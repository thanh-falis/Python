while True:
    s = int(input("Nhập một số: "))
    print(s, "Là số chắn" if s%2 ==0 else "là số lẻ")
    ask=input("Bạn muốn tiếp tục?(c/k)")
    if ask == "k":
        break;
print("Cảm ơn bạn đã dùng")