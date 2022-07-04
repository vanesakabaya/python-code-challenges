print("Hi there! we can check how many times the character appears in the string.")

# requesting user to enter a string.
String = input("Enter the string here: ")

# Allow the user to choose a character to check
character = input("Enter the character you want to check for its itellation in the string: ")
print(character, "appeared in '", String, "'", String.count(character), "times.")