#Thiết kế màn hình chuyển năm dương thành năm âm

from tkinter import *
from ReadFile import *

dataCan = ReadFile("can.txt")
dataChi = ReadFile("chi.txt")


def ChuyenDoi():
    a = float(NamDuong.get())
    can = ((a-3) % 10)
    chi = ((a-3) % 12)
    ca = GetCan(dataCan, can)
    ci = GetChi(dataChi, chi)
    NamAm.set(ca+ci)


root = Tk()

NamDuong = StringVar()
NamAm = StringVar()

root.title("7")
root.resizable(height=True, width=True)
root.maxsize(height=120, width=300)
root.minsize(height=120, width=300)
Label(root, text="Nhập năm dương:").grid(row=1, column=1, padx=10, pady=10)
Entry(root, width=25, textvariable=NamDuong).grid(row=1, column=2, padx=5, pady=10)

Button(root, text="Chuyển", width=12, command=ChuyenDoi).grid(row=2, column=2, padx=5, pady=5)

Label(root, text="Năm Âm là:").grid(row=3, column=1, padx=10, pady=10)
Entry(root, width=25, textvariable=NamAm).grid(row=3, column=2, padx=5, pady=10)

root.mainloop()