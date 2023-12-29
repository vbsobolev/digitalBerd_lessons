# 1. Написать функцию без параметров
def print_something():
    print(f'\nsomething')


print_something()


# 2. Написать функцию с 1 параметром
def sort_string(sstring):
    slist = list()
    slist.extend(sstring)
    return sorted(slist)


ss = input(f'\nInput string to sort: ')
print(sort_string(ss))

# 8. Написать функцию, которая на вход получает список (list),
#    сортирует его пузырьком, после чего возвращает отсортированный список.
list_sort = [4, 7, 9, 1, 1, 2, 5, 3, 6, 8]
string_sort = '4, 7, 9, 1, 1, 2, 5, 3, 6, 8'


def sor_puz(l):
    if not type(l) == list:
        print('wrong input type')
        return None
    n = len(l) - 1
    iteration = 0
    while n > 1:
        for i in range(0, n):
            if l[i] > l[i + 1]:
                i_temp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = i_temp
            iteration += 1
            print(f'iteration #{iteration:02}: {l}')
        n -= 1
    return l


print(f'\noriginal list: {list_sort}')
sor_puz(list_sort)
print(f'\noriginal string: {string_sort}')
sor_puz(string_sort)
