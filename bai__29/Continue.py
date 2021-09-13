# Continue là lệnh dừng vòng lặp hện tại và nhảy tới vòng lặp tiếp theo
s = 0
n = 15
for x in range(1, n+1, 2):
    if x is 3 or x is 11:
        continue
    s = s+x
print("Tổng = ", s)