"""
- ROI (Return On Investment) là tỉ lệ lợi nhuận so với chi phí ban đầu
- Viết chương trình cho phép người dùng nhập vào Doanh Thu và Chi Phí
và cuất ra tỉ lệ ROI cho người dùng, đồng thời cho biết nên hay không nên
đầu tu dự án khi biết ROI (giả sử tối thiểu là 0.75 thì mới đầu tư)
"""

def ROI(Doanhthu, Chiphi):
    return (Doanhthu - Chiphi)/Chiphi


def Tips(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

print("Chương trình tính ROI")
doanhthu = int(input("Nhập doanh thu: "))
chiphi = int(input("Nhập chi phí: "))
roi = ROI(doanhthu, chiphi)
print("Tỉ lệ ROI: ", roi)
print("==>", Tips(roi))