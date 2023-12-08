w = float(input("Фінальна координата Х:"))
h = float(input("Фінальна координата H:"))
a = float(input("Точка на координаті Х:"))
b = float(input("Точка на координаті H:"))
asek = 0
bsek = 0
prefering = False
while a != w:
    a += 0.5
    asek+=1
while b != h:
    b += 0.5
    bsek +=1
if asek > bsek:
    prefering = asek
elif asek < bsek:
    prefering = bsek
elif asek == bsek:
    prefering = asek

print(prefering)

#Я знаю що потрібно по три зміних але так удобніше зная що точка а на кординаті Х, а b на кординаті Н