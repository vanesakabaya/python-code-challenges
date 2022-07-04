# Create Dictionary of list
Dictionary = {}

def WordFrequency(string):

	# break the string into list of words
	string = string.split()		
	words = []

	# loop till string values present in list string
	for n in string:			

		# checking for the duplicacy
		if n not in words:

			# insert value in words 
			words.append(n)
			
	for n in range(0, len(words)):
            Dictionary.update({words[n]: string.count(words[n])})            
  
string ="from fairest creatures we desire increase that thereby beauty rose might never die but as the riper should by time decease his tender heir might bear his memory but thou contracted to thine own bright eyes feed thy light flame with self-substantial fuel making a famine where abundance lies thy self thy foe to thy sweet self too cruel"
           
WordFrequency(string)
print(Dictionary)
