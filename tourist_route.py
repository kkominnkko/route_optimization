n = int(input('Введіть кількість місць, які б Ви хотіли відвідати:'))

Str = []
Stb = []
matrix = []
matrix1 = []

# Масиви для збереження індексів
for i in range(n):
    Str.append(i)
    Stb.append(i)

# Введення матриці
print(
    "Матриця відстаней \nВідстанні вводяться в рядок через пробіл (в кілометрах) "
    "\nВідношення відстаней місця самого до себе позначається числом 0")
for i in range(n):
    matrix.append(list(map(float, input(f"Введіть відстані від {i + 1}-ого місця до усіх інших місць:\n").split())))

for i in range(n):
    matrix1.append(matrix[i].copy())

for i in range(n):
    matrix[i][i] = float('inf')

h = 0
path = 0
res = []
result = []


def min_el(lst, index):
    return min(x for idx, x in enumerate(lst) if idx != index)


def delete_s(matrix, index1, index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix


# Перетворення матриці
while True:

    for i in range(len(matrix)):
        temp = min(matrix[i])
        h += temp
        for j in range(len(matrix)):
            matrix[i][j] -= temp

    for i in range(len(matrix)):
        temp = min(row[i] for row in matrix)
        h += temp
        for j in range(len(matrix)):
            matrix[j][i] -= temp

    NullMax = 0
    index1 = 0
    index2 = 0
    tmp = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                tmp = min_el(matrix[i], j) + min_el((row[j] for row in matrix), i)
                if tmp >= NullMax:
                    NullMax = tmp
                    index1 = i
                    index2 = j

    res.append(Str[index1] + 1)
    res.append(Stb[index2] + 1)

    oldIndex1 = Str[index1]
    oldIndex2 = Stb[index2]
    if oldIndex2 in Str and oldIndex1 in Stb:
        NewIndex1 = Str.index(oldIndex2)
        NewIndex2 = Stb.index(oldIndex1)
        matrix[NewIndex1][NewIndex2] = float('inf')
    del Str[index1]
    del Stb[index2]
    matrix = delete_s(matrix, index1, index2)
    if len(matrix) == 1:
        break

# Створення шляху
for i in range(0, len(res) - 1, 2):
    if res.count(res[i]) < 2:
        result.append(res[i])
        result.append(res[i + 1])
for i in range(0, len(res) - 1, 2):
    for j in range(0, len(res) - 1, 2):
        if result[len(result) - 1] == res[j]:
            result.append(res[j])
            result.append(res[j + 1])

# Вивід
print("Ваш шлях виглядає наступним чином:")
for i in range(0, len(result) - 1, 2):
    print(f"{result[i]} -> {result[i + 1]}")
    if i == len(result) - 2:
        print(f"{result[i + 1]} -> {result[0]}")

# Підрахунок довжини шляху
for i in range(0, len(result) - 1, 2):
    if i == len(result) - 2:
        path += matrix1[result[i] - 1][result[i + 1] - 1]
        path += matrix1[result[i + 1] - 1][result[0] - 1]
    else:
        path += matrix1[result[i] - 1][result[i + 1] - 1]
print('Довжина усього шляху', path, 'км')
