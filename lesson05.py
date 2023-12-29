def func1():
    print('a')
    print('b')

for one_element in [1, 2, 3]:
    func1()

def func2(local_element):
    print(local_element, local_element*2)

for one_element in [1, 2, 3, 'hello']:
    func2(local_element=one_element)
def func3(name, surname='qwe'):
    print(f'name is {str(name)} ,surname is {str(surname)}')

func3(name='Иван')

def sum2(a, b):
    result = a + b
    return result

print(sum2(1, 2))

def func123(a: int):
    return a*2

func123('aa')

