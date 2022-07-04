import random

Listnames = []
#enter number of names to be stored in the list

number = int(input("Enter number of names to store in the list: "))
#print("Let's now store our names: ")

for n in range(1, number + 1):
    #enter names in list
    name = input("Enter name in list %d: " %n)
    Listnames.append(name)

print(Listnames)
print()
#shuffle the names in list randomly 
random.shuffle(Listnames)
print("Shuffled list: ", Listnames)
