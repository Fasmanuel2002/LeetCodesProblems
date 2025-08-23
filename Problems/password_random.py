import csv
import random
filename="Password.csv"
passwordcolection = ["1","2","3","4","5","6","7","8","9" ,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","p","q","r","s","t","u","v","y","z"]
socialmedia = input("What Social Media you want to save tour password: ")
passowrd = int(input("How many letter/numbers do you want in your pass")) 
new_password = random.choices(passwordcolection, k=passowrd)
delimiter = ""
join_password = delimiter.join(new_password)
print(join_password)


f1 = open(filename, "a",newline='')
fread = open(filename, "r")
fieldnames = ["Social Media", "password"]
writer = csv.DictWriter(f1, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({"Social Media":socialmedia, "password":join_password})
