import random
def main():
    historical_years = {
    -3100: "Unification of Upper and Lower Egypt, beginning of Ancient Egyptian civilization",
    776: "The first recorded Ancient Olympic Games in Greece",
    44: "Julius Caesar was assassinated in Rome",
    476: "The fall of the Western Roman Empire",
    622: "The Islamic calendar begins with the Hijra, Muhammad's migration to Medina",
    1066: "The Norman Conquest of England and the Battle of Hastings",
    1215: "The Magna Carta was signed in England",
    1492: "Columbus discovered the Americas and the Reconquista ended in Spain",
    1517: "Martin Luther started the Protestant Reformation",
    1776: "The United States declared independence",
    1789: "The French Revolution began",
    1804: "Haiti became the first independent Black republic",
    1815: "Napoleon Bonaparte was defeated at the Battle of Waterloo",
    1865: "The American Civil War ended, and slavery was abolished in the US",
    1914: "World War I began",
    1917: "The Russian Revolution led to the fall of the Romanovs",
    1945: "World War II ended, and the United Nations was founded",
    1963: "Martin Luther King Jr. delivered his 'I Have a Dream' speech",
    1969: "Humans landed on the Moon for the first time",
    1989: "The Berlin Wall fell, marking the end of the Cold War",
    1991: "The Soviet Union dissolved, ending the Cold War officially",
    2001: "The September 11 terrorist attacks occurred in the US",
    2020: "The COVID-19 pandemic began, impacting the entire world"
    }
    i = 5
    points = 0
    key, value = random.choice(list(historical_years.items()))    
    print(f"Ths is the help {value}")
    while True:
        print("What number do you think is the vault?")
        
        answer = int(input("What do you think: "))
        if answer == key:
            points+=1
            print(f"Hoorayyyyyy you did it, well done {points}")
            key, value = random.choice(list(historical_years.items()))    
            print(f"Ths is the help {value}")
        else:
            i-=1
            print(f"This is the remaining opportunities you have {i} ")
        if i == 0:
            print(f"Sorry you lost, this was the answer {key}")
            break
        if points == 5:
            print("You win")
            break
        
            
        

    
main()