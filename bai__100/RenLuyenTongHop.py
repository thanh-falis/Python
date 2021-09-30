from tkinter import *
from XưLyFile import *


def Add():
    line = Ma.get()+";"+Ten.get()+";"+Nam.get()
    SaveFile(line)
    Ma.set("")
    Ten.set("")
    Nam.set("")
    ShowBook()


def ShowBook():
    arrBook = ReadFile()
    lstBox.delete(0, END)
    for item in arrBook:
        lstBox.insert(END, item)


def Sort():
    arrBook = ReadFile()
    for i in range(len(arrBook)):
        for j in range(len(arrBook)):
            a = arrBook[i]
            b = arrBook[j]
            if a[2] > b[2]:
                arrBook[i] = b
                arrBook[j] = a

    lstBox.delete(0, END)
    for item in arrBook:
        lstBox.insert(END, item)


def Search():
    arrBook = ReadFile()
    ma = Ma.get()
    found = False
    for book in arrBook:
        if book[0] == ma:
            found = True
            break
    if found:
        print("Tìm thấy rồi")
    else:
        print("Sory")


root = Tk()

Ma = StringVar()
Ten = StringVar()
Nam = StringVar()

root.title("Quản lý sách")
root.resizable(height=True, width=True)
root.minsize(height=300, width=300)
Label(root, text="Quản lý sách ", fg="Blue", font=("cambria", 16), justify=CENTER).grid(row=1, columnspan=2)
lstBox = Listbox(root, width=50)
lstBox.grid(row=1, columnspan=2)
ShowBook()
Label(root, text="Mã sách").grid(row=2)
Entry(root, width=30, textvariable=Ma).grid(row=2, column=1)

Label(root, text="Tên").grid(row=3)
Entry(root, width=30, textvariable=Ten).grid(row=3, column=1)

Label(root, text="Năm xuất bản").grid(row=4)
Entry(root, width=30, textvariable=Nam).grid(row=4, column=1)

frameButton = Frame()
Button(frameButton, text="Thêm", command=Add).pack(side=LEFT)
Button(frameButton, text="Tìm", command=Search).pack(side=LEFT)
Button(frameButton, text="Sắp xếp").pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
