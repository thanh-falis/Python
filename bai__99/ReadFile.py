
def ReadFile(path):
    arrType = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrType.append(arr)
    file.close()
    return arrType


def returnData(data):
    for row in data:
        for element in row:
            print(element, end='\t')
        print()
    print()


def GetCan(can, num):
    res = ""
    for i in range(len(can)):
        if i == num:
            res = can[i]
    return res


def GetChi(chi, num):
    res = ""
    for i in range(len(chi)):
        if i == num:
            res = chi[i]
    return res