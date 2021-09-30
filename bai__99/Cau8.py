#Thiết kế màn hình chuyển độ F thành độ C

from tkinter import *


def ChuyenDoi():
    F = float(DoF.get())
    C = (F - 32)/1.8
    DoC.set(C)


root = Tk()

DoF = StringVar()
DoC = StringVar()

root.title("8")
root.resizable(height=True, width=True)
root.maxsize(height=120, width=250)
root.minsize(height=120, width=250)
Label(root, text="Nhập độ F:").grid(row=1, column=1, padx=10, pady=10)
Entry(root, width=25, textvariable=DoF).grid(row=1, column=2, padx=5, pady=10)

Button(root, text="Chuyển", width=12, command=ChuyenDoi).grid(row=2, column=2, padx=5, pady=5)

Label(root, text="Độ C:").grid(row=3, column=1, padx=10, pady=10)
Entry(root, width=25, textvariable=DoC).grid(row=3, column=2, padx=5, pady=10)

root.mainloop()
