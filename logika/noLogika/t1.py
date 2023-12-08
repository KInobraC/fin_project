default = 256
n = int(input("Скільки днів буде йти цикл"))
a = int(input("Скільки зубів витрачав"))
b = int(input("Скільки зубів виросотали"))
day = 0
while 1 <= n <= 10000000000 and 1 <= a <= b <= 100:
    if day != n:
        default-=a
        default+=b
        day+=1
print(default)