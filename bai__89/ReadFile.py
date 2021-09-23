"""
Cách đọc tập tin:
def readFile(path):
    file = open('file.txt', 'r', encoding='utf-8')
    for line in file:
        print(line.strip())
    file.close()
readFile()
"""


def readFile(path):
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        print(data)
    file.close()


readFile("csdlsinhvien.txt")
