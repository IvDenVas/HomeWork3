# Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input("Введите значение N: "))
list = []

for i in range(1, n + 1):
    list.append((int(input(f'Введите {i} элемент массива: '))))

print(list)

x = int(input("Введите значение X: "))
count = 0

for i in list:
    if (i == x):
        count += 1

print(f'-> {count}')