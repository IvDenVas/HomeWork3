# Требуется найти в массиве A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. В 
# последующих  строках записаны N целых чисел Ai. Последняя строка 
# содержит число X
# 5
# 1 2 3 4 5
# 6

# -> 5

n = int(input("Введите значение N: "))
list = []

for i in range(1, n + 1):
    list.append(i)

print(list)

max = min = list[0]

for i in list:
    if (i < min):
        min = i
    elif (i > max):
        max = i

x = int(input("Введите значение X: "))

if (x in list):
    print(f'-> {x}')
elif (x < min):
    print(f'-> {min}')
elif (x > max):
    print(f'-> {max}')