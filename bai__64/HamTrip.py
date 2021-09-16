"""
Để xóa khoảng trắng dư thừa, python hỗ trợ hàm trip
"""

s1 = " Hello my friend "
print(s1, len(s1))
s2 = s1.strip()
print(s1, len(s2))

s3 = "***Thanh***"
s3 = s3.strip('*')
print(s3)

'''
Lưu ý trip chỉ xóa trừ trái và từ phải xóa vào, 
nếu gặp ký tự đầu tiên không phải ký tự tự muốn xóa thì sẽ dừng
'''