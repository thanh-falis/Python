"""
- Đệ qui là cách mà hạm gọi lại chính nó.
- Nếu sử dụng đệ qui không khéo sẽ dẫn đến tràn bộ nhớ đệm.
- Khi quyết định giải quyết bài toán theo đệ qui cần lưu ý:
    + Điểm dừng của bài toán là gì
    + Quy luật thực hiện của bài toán
- Nếu không tìm ra được 2 ý trên thì không nên dùng đệ qui
"""

def factory(n):
    """
    Tính giai thừa
    """
    if n == 0:
        return 1
    return n*factory(n-1)


print(factory(6))