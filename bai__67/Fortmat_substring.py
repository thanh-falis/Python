s = "D:/tailieu/python/baitap.pdf"
p = s.rfind('/')
print(s[p+1])
p2 = s.rfind('.')
print(s[p+1:p2])