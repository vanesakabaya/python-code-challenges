
# Creating list of numbers array
numbers = []
n = int(input("Enter the value of numbers the list should contain: "))

# Getting items entered from the user the user
for i in range (1, n + 1):
    item = int(input("Enter Element %d: " %i))
    numbers.append(item)

# Display the list and sort it in ascending order
print(numbers)
numbers.sort()
numbers.reverse()
print("the maximum number in the list is: ", max(numbers), "and")

# Find th runner-up number in the list
refNum = numbers[1]
for n in range(2, len(numbers)):
    if (numbers[n] == refNum):
        refNum = numbers[n + 1]
        for m in numbers:
            if(m == refNum):

                print("All numbers in the list are equal!")
                break
            else: 
                print("The Runner-Up is", refNum)
                break
        break
    else:
        print("The runner-up is", refNum)
        break