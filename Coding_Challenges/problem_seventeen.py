
# Create Person class
class Person:
    
    # Person Constructor
    def __init__(self, name):
        self.name = name
    
    # Introduction method
    def introduce (self):
        print(" My name is", self.name)

#Let's introduce you to the audience."

# Create Person instance
person = Person(input("Enter your name: "))

# method calling
person.introduce()