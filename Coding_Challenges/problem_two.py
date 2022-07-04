# a program which checks if a string is palindromic.

string = input("Enter string here to check whether it is palindromic or not: ")
def parindrom(word):
    # retun string from the last one
    return word == word[::-1]
word = string
result = parindrom(word)
if result:
    print("The string  is Palindromic!")
else:
    print("The string  is not Palindromic!")