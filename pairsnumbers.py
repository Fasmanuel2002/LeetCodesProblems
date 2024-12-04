numbers = []
x = 0
for _ in range(50):
    x += 1
    numbers.append(x)

for numb in numbers:
    if (numb % 2) == 0:
        print(numb)