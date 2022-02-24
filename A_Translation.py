
word = input()
translated_word = input()

correct_word = "".join([letter for letter in reversed(list(word))])

if translated_word == correct_word:
	print("YES")
else:
	print("NO")
