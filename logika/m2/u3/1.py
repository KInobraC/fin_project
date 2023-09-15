students = ['Симоненко', 'Косач', 'Павлюк', 'Ковальчук', 'Сидоренко', 'Гончар']
# сортування списку учнів
students.sort()
# всього учнів
amount_students = len(students)
i = 1
print('Список класу:')
for students in students:
     print (i, '-', students)
     i += 1
print ('Всього учнів:', amount_students)