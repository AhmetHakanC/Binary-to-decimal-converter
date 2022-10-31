son = 0
a = 0

while True:
    girdi = input("Sayiyi giriniz (0 veya 1)")
    for i in range(len(girdi)):
        if i == 0:
            a = int(girdi[-1])
            son += a * (2 ** i)
        elif i >= 1:
            a = int(girdi[-i-1])
            son += a * (2**i)
    print(girdi)
    print(son)
    son = 0
    a = 0
