print("Введите положительное число: ")
a = float(input())
b = str(a)
d = a

if a < 1:
    print("Первая цифра:", 0)
else:
    c = a
    while c > 10:
        c //= 10
    print("Первая цифра:", int(c))

while a % 1 != 0:
    a *= 10
print("Последняя цифра:", int(a % 10))

if d == int(d):
    print("Количество цифр:", len(b) - 2)
else:
    print("Количество цифр:", len(b) - 1)

sum = 0
e = len(b)
for i in range (e):
    sum += a % 10
    a //= 10
print(int(sum))
