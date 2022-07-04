from multiprocessing.sharedctypes import Value

# Create two empty lists
List1 = []
List2 =[]

# Union Function definition
def union (List1, List2):
    List3 = [value for value in List1 if value not in List2]
    return List3

# Get the length for first list
List1_Lenght = int(input("Enter length first list: "))

# Get first list items
for a in range (1, List1_Lenght + 1):
    List1Items = int(input("Enter item %d: " %a))
    List1.append(List1Items)
    
# Display entered list items
print("First list: ", List1)

# Get the length for second list
List2_Length = int(input("Enter length of  second list: "))


# Get Second list items
for b in range (1, List2_Length + 1):
    List2Items = int(input("Enter item %d: " %b))
    List2.append(List2Items)
    
# Display second list
print("Second list: ", List2)

#function Call for union function
print("Elemets of first list that are not in second list: ", union(List1, List2))