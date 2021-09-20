"""
Hàm find() trả về giá trị tìm thấy đầu tiên, hàm rfind trả về giá trị cuối tìm thấy.
Nếu không tìm thấy thì trả về -1
"""
s = "c:/music/bolero/doithonghaimo.mp3"
p1 = s.find("/")
p2 = s.rfind("/")
print("p1: ", p1)
print("p2: ", p2)

c =s.count("o")
print("o xuất hiện: ", c)

c1 = s.count("o", 16)
print("o xuất hiện: ", c1, "từ vị trí số 16")

c2 = s.count("o", 16, 20)
print("o xuất hiện: ", c2, "từ vị trí 16 đến 20")