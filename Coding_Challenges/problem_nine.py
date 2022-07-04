
items = []
#entering numbers separated by commas 
numbers = [x for x in input("Enter 4 comma separeted binary digits: ").split(',')]

for num in numbers:
    x = int(num, 2)
    #checking if number entered by the user is divisible by 5
    if not x%5:
        items.append(num)
        
print("The numbers that are divisible by 5 are:", ','.join(items))