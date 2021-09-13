from random import randrange
while True:
    machine = randrange(1, 100)
    count = 0
    win = False
    while count < 7:
        count += 1
        human = int(input("Máy đoán [1...100], mời bạn đoán số: "))
        print("Số lần đoán sai của bạn: ", count)
        if machine == human:
            print("Bạn đoán đúng, số máy là: ", machine)
            win = True
            break
        if machine > human:
            print("Bạn đoán sai, số máy > số bạn đoán")
        elif machine < human:
            print("Bạn đoán sai, số máy < số bạn đoán")
    if win == False:
        print("Game over!")
    ask = input("Tiếp tục hay không?")
    if ask == "k":
        break
print("Cảm ơn bạn đã chơi game!")