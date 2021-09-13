'''
print("Nhập 1 số trong khoảng 1...10")
x=-1
while x<1 or x>10:
    x=int(input("Nhập trong khoảng 1...10"))
print(x**2)
'''
print("Nhập n: ")
n=int(input())
s = 0
i = 1
while i<=n:
    s=s+i
    i=i+1
print("Tổng = ",s)
