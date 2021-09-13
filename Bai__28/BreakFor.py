n = int(input("Nhập n: "))
s = 0
for x in range(1, n+1, 1):
    s = s + 1
    if s >= 15:
        break
print("s= ", s)