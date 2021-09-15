"""BMI là chỉ số cân đối cơ thể, yêu cầu nhạp chiều cao và cân nặng,
cho biết người này như thế nào
"""

def BMI(h, w):
    return w/h**2

def PhanLoai(BMI):
    if BMI < 18.5:
        return "Gầy"
    elif BMI <= 24.9:
        return "Bình thường"
    elif BMI <= 29.9:
        return "Hơi béo"
    elif BMI <= 34.9:
        return "Béo phì cấp độ 1"
    elif BMI <= 39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"

def NguyCo(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "Trung bình"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"


print("Nhập vào chiều cao:")
h = float(input())
print("Nhập vào cân nặng:")
w = float(input())
bmi = BMI(h, w)
print("BMI của bàn là: ", bmi)
print("Phân loại của bạn = ", PhanLoai(bmi))
print("Nguy cơ bệnh của bạn: ", NguyCo(bmi))

