def main():
    x = float(input("How many money do you want to change: "))
    y = input("And what type of money do you want to change it: ")
    match y:
        case "Europa":
            print(f"{europaMoney(x)} €")
        case "China":
            print(f"{chinaMoney(x)} ¥")
        case "UK":
            print(f"{ukMoney(x)} £")
        case "Japan":
            print(f"{JapanMoney(x)} ¥")
        case _:
            print("ERROR")
def europaMoney(x):
    diffEuropaVsAmerican = 0.95
    return x * diffEuropaVsAmerican
def chinaMoney(x):
    diffChinavsAmerica = 7.2320
    return x * diffChinavsAmerica
def ukMoney(x):
    diffUkVsAmerica = 0.79
    return x * diffUkVsAmerica
def JapanMoney(x):
    diffJapanVsAmerica = 150.02
    return x * diffJapanVsAmerica 

main()

    