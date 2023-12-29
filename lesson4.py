l1 = [1, 2, 3, 'hello']
l2 = [100, 200]

for one in l1:
    print(one)
    print(one * 10)
print(one)

v_sum = 0
for one in l2:
    v_sum = v_sum + one

print(v_sum)

d1 = {
    'one': 123,
    'two': 456
}

for one_key in d1.keys():
    print(one_key, d1.get(one_key))

i = 1
d2 = dict()

for one_element in l1:
    d2[i] = one_element
    i = i + 1

print(d2)

#цикл в цикле - это плохо
i = 0
import time
for one_element in [1, 2, 3]:
    for i in [1, 2, 3, 4]:
        print('hello', i)
        i += 1
        time.sleep(1)