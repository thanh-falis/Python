"""
Thiết kế giao diện công trừ nhân chia
"""

from tkinter import *


def Cong():
    a = float(SoA.get())
    b = float(SoB.get())
    Eq.set(a+b)


def Tru():
    a = float(SoA.get())
    b = float(SoB.get())
    Eq.set(a-b)


def Nhan():
    a = float(SoA.get())
    b = float(SoB.get())
    Eq.set(a*b)


def Chia():
    a = float(SoA.get())
    b = float(SoB.get())
    Eq.set(a/b)


root = Tk()

SoA = StringVar()
SoB = StringVar()
Eq = StringVar()

root.title("PBT2")
root.resizable(height=True, width=True)
root.minsize(height=160, width=205)
Label(root, text="Calculator ", fg="red", font=("tahoma", 16), justify=CENTER).grid(row=0, columnspan=2)

frameButton = Frame()
Button(frameButton, text="Cộng", command=Cong).pack(side=TOP, fill=X)
Button(frameButton, text="Trừ", command=Tru).pack(side=TOP, fill=X)
Button(frameButton, text="Nhân", command=Nhan).pack(side=TOP, fill=X)
Button(frameButton, text="Chia", command=Chia).pack(side=TOP, fill=X)
frameButton.grid(row=1, column=0, rowspan=4)

Label(root, text="Số a:").grid(row=1, column=1)
Entry(root, width=15, textvariable=SoA).grid(row=1, column=2)

Label(root, text="Số B:").grid(row=2, column=1)
Entry(root, width=15, textvariable=SoB).grid(row=2, column=2)

Label(root, text="Kết quả:").grid(row=3, column=1)
Entry(root, width=15, textvariable=Eq).grid(row=3, column=2)

Button(root, text="Thoát", command=root.quit).grid(row=4, column=2)

root.mainloop()