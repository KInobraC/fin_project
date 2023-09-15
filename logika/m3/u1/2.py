class Students():
    def __init__(self, surname, name, grade):
        self.surname = surname
        self.name = name
        self.grade = grade


students = []

with open('1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(" ")
        obj = Students(data[0], data[1], int(data[2]))
        students.append(obj)

for n in students:
    if n.grade == 5:
        print(n.surname)