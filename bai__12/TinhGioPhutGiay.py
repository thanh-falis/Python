t = int(input("Nhập Số Giây"))
h = t//3600 % 24
m = (t % 3600)//60
s = (t % 3600) % 60
if h <= 12:
    print(h, ":", m, ":", s, ": AM")
elif h > 12:
    print(h, ":", m, ":", s, ": PM")

