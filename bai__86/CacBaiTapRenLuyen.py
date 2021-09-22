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


