# Sử dụng if else expression cho điều kiện đơn giản, tương tự toán tử 3 ngôi
a = 5
b = 7
"""
if a!=b:
    c = 113
else:
    c = 115
"""

c=113 if a!=b else 115
print(c)

x = int(input("Nhập một số:"))
print("Chẵn" if x%2 == 0 else "Lẻ")