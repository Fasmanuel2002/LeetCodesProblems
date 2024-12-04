numbers = []


x = int(input("What number do you want to see in decrease: "))
for _ in range(x):
    x -= 1
    numbers.append(x)
    
for number in numbers:
    print(number)
    