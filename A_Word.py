
word = input()

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

no_of_lowercase_letters = len([letter for letter in word if letter in lowercase_letters])
no_of_uppercase_letters = len(word) - no_of_lowercase_letters

if no_of_uppercase_letters > no_of_lowercase_letters:
	print(word.upper())
elif no_of_lowercase_letters > no_of_uppercase_letters:
	print(word.lower())
else:
	print(word.lower())
