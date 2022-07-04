#checking if the number 

def check (a, i):
    if (a % i == 0):
        print(i, "is a factor of", a)
    else:
        print(i, "is not a factor of", a)
      #entering numbers   
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Entered numbers: ", num1, ", ", num2)
check(num1, num2)