
# Create an empty Dictionary string
Dict_string = {}

# Frequency checker Method
def wordFrequency(Array_string):
    
    newArray = []
    
	# loop till string values present in list Array_string
    for word in Array_string:			

		# Check if a word is not duplicated
        if word not in newArray:

			# insert value in Array_string
            newArray.append(word)
    for word in range(0, len(newArray)):
        Dict_string.update({newArray[word]: Array_string.count(newArray[word])})
        
    print(Array_string)

Array_string = []

print(" here is a program to record how many your entered a string")
n = int(input("Enter number of string to store: "))

for a in range(1, n + 1):
    str = input("Enter string %d: " %b)
    Array_string.append(str)
    
# function call of Array_string
wordFreq(Array_string)

# output will be 
print(Dict_string)