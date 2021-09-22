""" Python hỗ trợ hàm reverse để đảo danh sách """
lst = [2, 0, 2, 1]
print(lst)
#lst.reverse()
#print(lst)

for i in range(len(lst)-1, -1, -1):
    print(lst[i], end='\t')
print()
print("*"*30)
lst = [8, 0, 2, 100]
print(lst)

lst1 = reversed(lst)
for item in lst1:
    print(item)

print(lst)

lst = ["Thanh", "Nguyễn", "Văn", """Trương
       Phúc
       Lộc
       """]

print(lst)
lst.reverse()
print(lst)