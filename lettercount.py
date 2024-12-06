x = input("Give me a word: ")

frequency = {}


for letter in x:
    if letter in frequency:
        frequency[letter] += 1  
    else:
        frequency[letter] = 1  


for letter, count in frequency.items():
    print(f"{letter}: {count}")
