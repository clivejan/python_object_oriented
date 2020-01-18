from collections import defaultdict

def letter_frequency(sentence):

	"""
	if the key didn't exist, it will call int() to return a 0
	as a default value to that key
	""" 
	freqencies = defaultdict(int)

	for letter in sentence:
		freqencies[letter] += 1
	return freqencies

message = "I would like be a devops."
print(letter_frequency(message))
