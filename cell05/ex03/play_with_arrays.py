x = [2, 8, 9, 48, 8, 22, -12, 2]
y = []
z = []

for i in x:
    if x.count(i) == 1:
        y.append(i)

for i in y:
    a = i + 2
    b = abs(a)
    z.append(b)

print(x)
print(z)