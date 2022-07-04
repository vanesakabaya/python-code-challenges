# a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
num1 = 2000
num2 = 3200
print("numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200")
for n in range (num1, num2+1):
    if (n % 7 == 0 and n % 5 != 0):
        # end = "," is used to print elements on the same line separated by a comma.
        print(n, end = ", ")