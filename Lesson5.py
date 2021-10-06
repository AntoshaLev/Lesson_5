# Задание 1

def odd_nums(max_val):
    n = 1
    while n <= max_val:
        yield n
        n += 2


odd_nums_15 = odd_nums(15)

# Задание 2
max_value = 3
odd_nums_generate = (i for i in range(1, max_value + 1, 2))
print(next(odd_nums_generate))

# Задание 3


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_of_people():
    i = 0
    j = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield None, klasses[i]
            i += 1
            j += 1
            break
        else:
            yield tutors[j], klasses[i]
            i += 1
            j += 1


for gen in gen_of_people():
    print(gen)

# Задание 4
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for i in range(len(src) - 1):
    if src[i] < src[i + 1]:
        result.append(src[i + 1])

print(result)

# Задание 5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])
