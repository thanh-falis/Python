n = int(input("Nhập chiều cao: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i == j or i == n-1:
            print("*", end='')
        else:
            print(' ', end='')
    print()

print("#"*30)
i = 0
while i < n:
    j = 0
    while j < n:
        if j is 0 or i is j or j is n-1:
            print("#", end='')
        else:
            print(' ', end='')
        j += 1
    i += 1
    print()