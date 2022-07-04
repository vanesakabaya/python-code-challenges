from multiprocessing.sharedctypes import Value

# Create two empty lists
List1 = []
List2 =[]

# Intersection Function definition
def Intersection (List1, List2):
    List3 = [value for value in List1 if value in List2]
    return List3

#let find the intersection of two lists
# Get the length for first list
List1_Length = int(input("Enter length first list: "))

# Get first list items
for n in range (1, List1_Length + 1):
    List1Items = int(input("Enter item %d: " %n))
    List1.append(List1Items)

# Display entered list items
print("First list: ", List1)

# Get the length for second list
List2_Length = int(input("Enter  length of second list: "))

# Get Second list items
for m in range (1, List2_Length + 1):
    List2Items = int(input("Enter item %d: " %m))
    List2.append(List2Items)

# Display second list
print("Second list: ", List2)


#  function Call of intersection function
print("Intersection of two entered lists: ", Intersection(List1, List2))