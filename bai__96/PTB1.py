"""
Thiết kế màn hình giải phương trình bậc nhất
"""

from tkinter import *


def NextAction():
    stringHSA.set("")
    stringHSB.set("")
    stringEq.set("")


def EqAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    if a == 0 and b == 0:
        stringEq.set("Vô số nghiệm")
    elif a == 0 and b != 0:
        stringEq.set("Vô nghiệm")
    else:
        stringEq.set("x ="+str(-b/a))

root = Tk()

stringHSA = StringVar()
stringHSB = StringVar()
stringEq = StringVar()

root.title("PBT1")
root.resizable(height=True, width=True)
root.minsize(height=140, width=260)
Label(root, text="Phương trình bậc 1", fg="red", font=("tahoma", 16), justify=CENTER).grid(row=0, columnspan=2)

Label(root, text="Hệ số a:").grid(row=1, column=0)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

frameButton = Frame()
Button(frameButton, text="Giải", command=EqAction).pack(side=LEFT)
Button(frameButton, text="Tiếp", command=NextAction).pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=3, column=1)

Label(root, text="Kết quả:").grid(row=4, column=0)
Entry(root, width=30, textvariable=stringEq).grid(row=4, column=1)

root.mainloop()