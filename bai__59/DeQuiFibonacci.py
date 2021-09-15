"""
- Dãy số Fibonacci có dạng:
    1->1->2->3->5->8->13->21->34->59...
- Được định nghĩa thoe công thức đẹ qui như sau:
    Nếu N=1,N=2 ->Fn=1
    N>2: Fn = Fn-1 + Fn-2
- Hãy viết hàm
    Trả về số Fib tại vị trí thứ N bất kỳ
    Hàm trả về danh sách số Fib từ 1 tới N

"""

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


def ListFibo(n):
    for i in range(1, n+1):
        print(fibonacci(i), end='\t')


print(fibonacci(9))

print(ListFibo(6))