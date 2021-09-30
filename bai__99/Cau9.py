# Thiết kế màn hình tính BMI

from tkinter import *


def TinhBMI():
    #BMI
    w = float(weight.get())
    h = float(tall.get())
    eq = w/(h**2)
    BMI.set(eq)

    # Tình trạng
    if eq < 18.5:
        Tinhtrang.set("Gầy")
    elif eq <= 24.9:
        Tinhtrang.set("Bình thường")
    elif eq <= 29.9:
        Tinhtrang.set("Hơi béo")
    elif eq <= 34.9:
        Tinhtrang.set("Béo phì cấp độ 1")
    elif eq <= 39.9:
        Tinhtrang.set("Béo phì cấp độ 2")
    else:
        Tinhtrang.set("Béo phì cấp độ 3")

    #Nguy cơ
    if eq < 18.5:
        NguyCo.set("Thấp")
    elif eq <= 24.9:
        NguyCo.set("Trung bình")
    elif eq <= 29.9:
        NguyCo.set("Cao")
    elif eq <= 34.9:
        NguyCo.set("Hơi Cao")
    elif eq <= 39.9:
        NguyCo.set("Rất cao")
    else:
        NguyCo.set("Nguy hiểm")


root = Tk()

tall = StringVar()
weight = StringVar()
BMI = StringVar()
Tinhtrang = StringVar()
NguyCo = StringVar()

root.title("9")
root.resizable(height=True, width=True)
root.maxsize(height=250, width=230)
root.minsize(height=250, width=230)
Label(root, text="Nhập chiều cao:").grid(row=1, column=1, padx=10, pady=10)
Entry(root, width=15, textvariable=tall).grid(row=1, column=2, padx=5, pady=10)

Label(root, text="Nhập cân nặng:").grid(row=2, column=1, padx=10, pady=10)
Entry(root, width=15, textvariable=weight).grid(row=2, column=2, padx=5, pady=10)

Button(root, text="Tính BMI", width=12, command=TinhBMI).grid(row=3, column=2, padx=5, pady=5)

Label(root, text="BMI của bạn:").grid(row=4, column=1, padx=10, pady=10)
Entry(root, width=15, textvariable=BMI).grid(row=4, column=2, padx=5, pady=10)

Label(root, text="Tình trạng:").grid(row=5, column=1, padx=10, pady=10)
Entry(root, width=15, textvariable=Tinhtrang).grid(row=5, column=2, padx=5, pady=10)

Label(root, text="Nguy cơ bệnh:").grid(row=6, column=1, padx=10, pady=10)
Entry(root, width=15, textvariable=NguyCo).grid(row=6, column=2, padx=5, pady=10)

root.mainloop()