def add(a, b):
    return a + b

print(add(3, 7))

def add(a, b):
    print('result: ', a + b)

add(3, 7)

add(b = 7, a = 3)

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# lambda express
print('lambda: ', (lambda a, b: a + b)(3, 7))
