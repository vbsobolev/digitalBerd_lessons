a = 3
if ((a>2) and (1 == 1)) or (1!=2):
    print('a > 2')
    if a > 10:
        print('a > 10')
elif a == 1:
    print('a = 1')
elif a == 2:
    print('a = 2')
else:
    print('a < 2')

l1 = [1, 2, 3]
if a in l1:
    print('a inside l1')
if len(l1) == a:
    print(a, ' elements in l1')