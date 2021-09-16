"""
- startswith kiểm tra chuỗi có bắt đầu bừng 1 chuỗi con nào đó hay không
- endswith kiếm tra chuỗi có kết thúc bằng 1 chuỗi con nào đó hay không
"""

s = "c:/music/bolero/bienman.mp3"

if s.endswith(".mp3"):
    print("Bài hát có đinh dạng mp3")
else:
    print("Bài hát này không phải đinh dạng mp3")

s1 = "***OBAMA###"
print(s1.startswith('*'))

def Fill_mobilephone(dauso):
    arr = ["0981574576", "0975746217", "0945874572", "0907380267"]
    for phone in arr:
        if(phone.startswith(dauso)):
            return phone
    return "<emty>"

dauso= input("Mời bạn nhập đầu số: ")
phone = Fill_mobilephone(dauso)
print(phone)

def FillAllPhone(dauso):
    arr = ["0981574576", "0985672314", "0975746217", "0945874572", "0907380267", "0903784579"]
    Found=[]
    for phone in arr:
        if (phone.startswith(dauso)):
            Found.append(phone)
    return Found


dauso = input("Nhập đầu số: ")
found = FillAllPhone(dauso)
print(found)