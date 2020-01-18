from collections import Counter

def letter_frequency(sentence):
	return Counter(sentence)

message = "I would like be a devops."
print(letter_frequency(message))
