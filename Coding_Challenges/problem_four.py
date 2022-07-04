# Given a list of integers, how many of its elements are multiples of 3?

List = []
count = 0
numbers = int(input("Enter the number of values the list should contain: "))
for num in range (1, numbers+1):
    number = int(input("enter the value of %d Element: " %num))
    List.append(number)
for n in range (0, numbers):
    if (List[n] % 3 == 0):
        count += 1
print(List)
print(count, "number(s) are multiple of 3")
    