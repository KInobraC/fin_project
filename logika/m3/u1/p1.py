with open('prob.txt', 'r', encoding='utf-8') as file:
    print(file.read())

with open('prob.txt', 'a', encoding='utf-8') as file:
    file.write(input("Введи автора цитати"))
    print("Автор успішно додан")
