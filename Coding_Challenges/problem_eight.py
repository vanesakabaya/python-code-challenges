CharArray = []
#enter number of characters 
length = int(input("Enter number of characters to be entered: "))
 
for b in range(1, length + 1):
    #enter each character till number of character
    #entered is reached
    character = input("Enter character %d: " %b)
    CharArray.append(character)
    
charString = ""
for char in CharArray:
    charString += char
#outputing the characters to make string 
print("characters:", CharArray)
print("resulted: ", charString, "as a string.")