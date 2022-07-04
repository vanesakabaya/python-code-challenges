#list declaration of the program
List = []
# entering the number of values of list
number = int(input("Enter the number of values the list should contain: "))
for num in range(1, number+1):
    # entering the values of element in the list
    number = int(input("Enter the value of %d Element: " %num))
    List.append(number)
    
# condition to check wether both number are equal
if(min(List) == max(List)):
    print("All number are equal!")
    
# else will execute if number are not equal
else:
    print("The Smallest Element in this List is : ", min(List))
    print("The Largest Element in this List is : ", max(List))
