
# String processor class 
class Tester:
    
    # Class methods tester
    def __init__(self):
        self.String = ""
    
    # getString method to get to get a string from console input
    def getString (self):
  # Let get a string from you
        self.String = input("Enter string: ")
    
    # printString method to print the string in upper case
    def printString (self):
        print("Print string: ", self.String)

# Create class instance
str = Tester()
str.getString()
str.printString()