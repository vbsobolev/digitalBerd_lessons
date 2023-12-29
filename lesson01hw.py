#создайте проект и файл.py, присвойте переменной любое значение, выведите её через print(), запустите файл
a='hello python'
print(a)

# Создайте несколько переменных каждого типа: Numbers (числа), Strings (строки), Boolean (логический тип данных))
int1 = 2
int2 = 1
flt1 = 4.0
flt2 = 3.0
str1 = 'hi'
str2 = 'hello'
boo1 = True
boo2 = False

"""
Сделайте все возможные операции (сложение, вычитание, умножение, деление, найдите остаток от деления на числа) над этими переменными:

- явное преобразование типов - например float 1.3 преобразуйте в int
"""

print(int1+int2)
print(int1-int2)
print(int1*int2)
print(int2/int1)
print(int2%int1)

print(flt1+flt2)
print(flt1-flt2)
print(flt1*flt2)
print(flt2/flt1)
print(flt2%flt1)

print(str1+str2)

print(boo1+boo2)
print(boo1-boo2)
print(boo1*boo2)

print(float(int1))

"""
Попробуйте поработать с типом list()
- создайте переменную
- внесите туда какие-то значения
- добавьте туда ещё значений при помощи функции .append()
- добавьте один list внутрь другого
- сложите 2 разных list
"""

list1=[5,6,7,8,9,10]
list1.append(24)
list2=[100,101]
list1.append(list2)
list3=[222,'duck']
print(list1+list3)