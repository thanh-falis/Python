"""
Slicing dùng để trích lọc list
    list[begin : end :step]
    List: Là danh sách
    Begin: Vị trí bắt đầu cắt
    End: Vị trí cuối cùng cắt
    Step: Bước nhảy
"""

lst = [10, 20, 30, 40, 50]
print(lst)
print(lst[0:3])
print(lst[1:3])
print(lst[2::])
print(lst[::2])
print(lst[::3])
print(lst[::-1])
