'''
Nhập điểm toán lý hóa theo chuỗi thứ tự,
Tính điểm trung bình lấy 2 số lẻ
'''

toan, ly, hoa = eval(input("Nhập điểm toán, lý, hóa:"))
print("Điểm Toán: ", toan)
print("Điểm Lý: ", ly)
print("Điểm Hóa: ", hoa)
diem = (toan+ly+hoa)/3
dtb = round(diem, 2)
print("Điểm trung bình = ", dtb)