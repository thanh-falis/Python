"""
Thiết kế màn hình giải phương trình bậc 2
"""
from math import sqrt
from tkinter import *


def Next():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringEq.set("")


def Result():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    c = float(stringHSC.get())
    if a == 0:
        if b == 0 and c == 0:
            stringEq.set("Vô số nghiệm")
        elif b == 0 and c != 0:
            stringEq.set("Vô nghiệm")
        else:
            x = -c/b
            stringEq.set("x= "+str(x))
    else:
        delta = b**2-4*a*c
        if delta < 0:
            stringEq.set("Vô nghiệm")
        elif delta == 0:
            stringEq.set("Nghiệm kép: "+str(-b/(2*a)))
        else:
            x1 = (-b - sqrt(delta)) / (2*a)
            x2 = (-b + sqrt(delta)) / (2*a)
            stringEq.set("x1="+str(x1)+"; x2="+str(x2))


root = Tk()
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringEq = StringVar()

root.title("PBT2")
root.resizable(height=True, width=True)
root.minsize(height=150, width=250)
Label(root, text="Phương trình bậc 2", fg="red", font=("tahoma", 16), justify=CENTER).grid(row=0, columnspan=2)

Label(root, text="Hệ số a:").grid(row=1, column=0)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

Label(root, text="Hệ số c:").grid(row=3, column=0)
Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1)

frameButton = Frame()
Button(frameButton, text="Giải", command=Result).pack(side=LEFT)
Button(frameButton, text="Tiếp", command=Next).pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=4, column=1)

Label(root, text="Kết quả:").grid(row=5, column=0)
Entry(root, width=30, textvariable=stringEq).grid(row=5, column=1)

root.mainloop()