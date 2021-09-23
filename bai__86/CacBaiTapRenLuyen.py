import random
"""
Câu 1: Cho list: lst = [3,0,1,5,2]
x = 2
Hãy cho biết kết quả
    (a)lst[0]               -> 3
    (b)lst[3]               -> 5
    (c)lst[x]               -> 1
    (d)lst[-x]              -> 5
    (e)lst[x+1]             -> 1
    (f)lst[x] + 1           -> 2
    (g)lst[lst[x]]          -> 0
    (h)lst[lst[lst[x]]]     -> 3

Câu 2: Cho list: lst = [20, 1, -34, 40, -8, 60, 1, 3]
    Hãy cho biết kết quả:

    (a) lst             -> [20, 1, -34, 40, -8, 60, 1, 3]
    (b) lst[0:3]        -> [20, 1, -34]
    (c) lst[4:8]        -> [-8, 60, 1, 3]
    (d) lst[4:33]       -> [-8, 60, 1, 3]
    (e) lst[-5:-3]      -> [40, -8]
    (f) lst[-22:3]      -> [20, 1, -34]
    (g) lst[4:]         -> [-8, 60, 1, 3]
    (h) lst[:]          -> [20, 1, -34, 40, -8, 60, 1, 3]
    (i) lst[:4]         -> [20, 1, -34, 40]
    (j) lst[1:5]        -> [1, -34, 40, -8]
    (k) -34 in lst      -> True
    (l) -34 not in lst  -> False
    (m) len(lst)        -> 8
"""
"Câu 3: Nhập 1 list có N số ngẫu nhiên không trùng nhau"

print("Nhập số phần tử: ")
n = int(input())
lst = random.sample(range(100), n)
print(lst)

"""
Câu 4: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách
thì yêu cầu nhập lại. In dãy số sau khi nhập xong.
"""
print("*"*30)


def List(a):
    ls = []
    for i in range(1, a+1):
        print("Nhập phần tử thứ ", i)
        j = int(input())
        ls.append(j)
    return ls


def is_sorted(ls):
    asc = None
    for i in range(len(ls)-1):
        a, b = ls[i], ls[i+1]
        if a == b:
            continue
        if asc is None:
            asc = (a < b)
        if (a < b) != asc:
            return False
    return True


def main():
    num = int(input("Nhập số phần tử:"))
    lst1 = List(num)
    print(lst1)

    flag = 0
    if all(lst1[i] <= lst1[i + 1] for i in range(len(lst1) - 1)):
        flag = 1

    if flag:
        print("List đã sort.", lst1)
    else:
        print("List chưa sort, nhập tăng dần.")
        lst3 = List(num)
        print(lst3)


main()
"""
Câu 5: Viết chương trình nhập vào một dãy n số thực M[0], M[1],... M[n-1],
Hãy sắp xếp theo thứ tự giảm dần và xuất ra màn hình 
"""
print("*"*30)


def main():
    num = int(input("Nhập số phần tử của dãy số: "))
    lst2 = List(num)
    print(lst2)
    print("Sắp xếp giảm dần")
    lst2.sort(reverse=True)
    print(lst2)


main()
