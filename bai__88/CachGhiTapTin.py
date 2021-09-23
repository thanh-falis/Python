"""
- Để ghi tập tin ta dùng hàm:
    open('myfile.txt','w') mở tập tin để ghi mới
    open('myfile.txt','a') mở tập tin để nối đuôi

vd:
    def LuuFile():
        file = open('csdlsv.txt', 'w', encoding='utf-8')
        file.writelines("sv1; Nguyễn Văn A; 9,5\n")
        ....
        file.close()
    LuuFile()
"""


def LuuFile(path):
    file = open(path, 'w', encoding='utf-8')
    file.writelines("sv1; Nguyễn Văn A; 20/7/1993\n")
    file.writelines("sv2; Pham Văn Ngọc; 5/6/1994\n")
    file.writelines("sv3; Lương Đức Thuận; 22/9/1993\n")
    file.close()


LuuFile("csdlsinhvien.txt")