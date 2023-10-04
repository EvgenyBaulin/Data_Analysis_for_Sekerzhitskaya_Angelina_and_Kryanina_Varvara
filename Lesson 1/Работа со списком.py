a = [1, 100, 2, 3, 4, 5, 6, 7]

for i in [100, 20, 30, 40]:
	a.append(i)

print(a)

while 100 in a:  # убрать все 100
	a.remove(100)

print(a)

a.pop(1)

print(a)
