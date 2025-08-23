import random


x = random.randint(1, 10)

print(x)

pop = True
while(pop != False):
    
    y = int(input("What's is the number: "))    
    if x > y:
        print(f"your number {y} is lower that the random number")
        
    elif x < y:
        print(f"your number {y} is greater that the random number")
        if y > 10:
            print(f"The number {y} is bigger than 10, so dont put it")
    else:
        print(f"Hooray, the number was {x}")
        pop = False
        break
    