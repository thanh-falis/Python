"""
Viết code hiển thị các loại style của button trong python
"""
from tkinter import *

root = Tk()

root.title("frame 2")
root.resizable(height=True, width=True)
root.minsize(height=160, width=420)

btns_frame = Frame(root, width=210, height=272.5)
btns_frame1 = Frame(root, width=210, height=272.5)

btns_frame.pack(side=LEFT)
btns_frame1.pack(side=LEFT)

# Frame 1

a = Button(btns_frame, text="borderwidth=0", borderwidth=0, width=12).grid(row=1, column=1, padx=5, pady=5)
b = Button(btns_frame, text="raised", width=5, borderwidth=0).grid(row=1, column=2, padx=5, pady=5)
c = Button(btns_frame, text="sunken", width=5, borderwidth=0).grid(row=1, column=3, padx=5, pady=5)

d = Button(btns_frame, text="borderwidth=1", borderwidth=0, width=12).grid(row=2, column=1, padx=5, pady=5)
e = Button(btns_frame, text="raised", width=5, borderwidth=1).grid(row=2, column=2, padx=5, pady=5)
f = Button(btns_frame, text="sunken", width=5, borderwidth=1).grid(row=2, column=3, padx=5, pady=5)

g = Button(btns_frame, text="borderwidth=2", borderwidth=0, width=12).grid(row=3, column=1, padx=5, pady=5)
h = Button(btns_frame, text="raised", width=5, borderwidth=1).grid(row=3, column=2, padx=5, pady=5)
i = Button(btns_frame, text="sunken", width=5, borderwidth=1).grid(row=3, column=3, padx=5, pady=5)

j = Button(btns_frame, text="borderwidth=3", borderwidth=0, width=12).grid(row=4, column=1, padx=5, pady=5)
k = Button(btns_frame, text="raised", width=5, borderwidth=1).grid(row=4, column=2, padx=5, pady=5)
l = Button(btns_frame, text="sunken", width=5, borderwidth=1).grid(row=4, column=3, padx=5, pady=5)

m = Button(btns_frame, text="borderwidth=4", borderwidth=0, width=12).grid(row=5, column=1, padx=5, pady=5)
n = Button(btns_frame, text="raised", width=5, borderwidth=1).grid(row=5, column=2, padx=5, pady=5)
o = Button(btns_frame, text="sunken", width=5, borderwidth=1).grid(row=5, column=3, padx=5, pady=5)

# Frame 2

p = Button(btns_frame1, text="flat", borderwidth=0, width=5).grid(row=1, column=1, padx=2, pady=2)
q = Button(btns_frame1, text="ridge", width=5, borderwidth=1).grid(row=1, column=2, padx=5, pady=5)
r = Button(btns_frame1, text="groove", width=5, borderwidth=1).grid(row=1, column=3, padx=5, pady=5)
s = Button(btns_frame1, text="solid", width=5, borderwidth=1).grid(row=1, column=4, padx=5, pady=5)

t = Button(btns_frame1, text="flat", borderwidth=0, width=5).grid(row=2, column=1, padx=5, pady=5)
u = Button(btns_frame1, text="ridge", width=5, borderwidth=1).grid(row=2, column=2, padx=5, pady=5)
v = Button(btns_frame1, text="groove", width=5, borderwidth=1).grid(row=2, column=3, padx=5, pady=5)
w = Button(btns_frame1, text="solid", width=5, borderwidth=1).grid(row=2, column=4, padx=5, pady=5)

x = Button(btns_frame1, text="flat", borderwidth=0, width=5).grid(row=3, column=1, padx=5, pady=5)
y = Button(btns_frame1, text="ridge", width=5, borderwidth=1).grid(row=3, column=2, padx=5, pady=5)
z = Button(btns_frame1, text="groove", width=5, borderwidth=1).grid(row=3, column=3, padx=5, pady=5)
na = Button(btns_frame1, text="solid", width=5, borderwidth=1).grid(row=3, column=4, padx=5, pady=5)

nb = Button(btns_frame1, text="flat", borderwidth=0, width=5).grid(row=4, column=1, padx=5, pady=5)
nc = Button(btns_frame1, text="ridge", width=5, borderwidth=1).grid(row=4, column=2, padx=5, pady=5)
nd = Button(btns_frame1, text="groove", width=5, borderwidth=1).grid(row=4, column=3, padx=5, pady=5)
ne = Button(btns_frame1, text="solid", width=5, borderwidth=1).grid(row=4, column=4, padx=5, pady=5)

nf = Button(btns_frame1, text="flat", borderwidth=0, width=5).grid(row=5, column=1, padx=5, pady=5)
ng = Button(btns_frame1, text="ridge", width=5, borderwidth=1).grid(row=5, column=2, padx=5, pady=5)
nx = Button(btns_frame1, text="groove", width=5, borderwidth=1).grid(row=5, column=3, padx=5, pady=5)
ny = Button(btns_frame1, text="solid", width=5, borderwidth=1).grid(row=5, column=4, padx=5, pady=5)


root.mainloop()
