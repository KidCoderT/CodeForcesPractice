
string_a = input().lower()
string_b = input().lower()

letters = "abcdefghijklmnopqrstuvwxyz"

case = 0

for i in range(len(string_a)):
	if string_a[i] != string_b[i]:
		if letters.index(string_a[i]) < letters.index(string_b[i]):
			case = -1
			break
		else:
			case = 1
			break

print(case)

