
# Create number processor method
def numberProc (numbers):
    
    # Create an empty array to store  non-duplicated values
    EmptyArray = []
    
    # Create an empty dictionary
    Dict_numbers = {}
    
    # Check for items in passed array
    for number in numbers:
        
        # Prevent duplication
        if number not in EmptyArray:
            EmptyArray.append(number)
    
    # Update the dictionary
    for item in EmptyArray:
        Dict_numbers.update({item: (item * 2)})
        
    return Dict_numbers

# Create an empty array to store numbers enterd by  the user 
numbers = []
    
 #create an array of numbers
n = int(input("Enter number of items:"))


for m in range(1, n + 1):
    
    # Get numbers from the user an store them in 'numbers' array
    item = int(input("Enter item %d: " %m))
    numbers.append(item)

# Call numberProc method
print(numberProc(numbers))