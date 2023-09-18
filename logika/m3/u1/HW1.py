class Students():
    def __init__(self, grade):
        self.grade = grade


students = []

with open('1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(" ")
        obj = Students(int(data[2]))
        students.append(obj)
obschball = 0
lenstud = len(students)
for n in students:
    if n.grade == 5:
        obschball+=5
    if n.grade == 4:
        obschball+=4
    if n.grade == 3:
        obschball+=3
    if n.grade == 2:
        obschball+=2
    if n.grade == 1:
        obschball+=1
vso = obschball / lenstud
print(f"Середня оцінка класу: {int(vso)}")