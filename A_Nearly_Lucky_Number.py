
n = input()

no_of_4s = n.count('4')
no_of_7s = n.count('7')

number_of_digits_of_lucky_number = str(no_of_4s + no_of_7s)

no_of_4s = number_of_digits_of_lucky_number.count('4')
no_of_7s = number_of_digits_of_lucky_number.count('7')

if len(number_of_digits_of_lucky_number) == no_of_4s + no_of_7s:
	print("YES")
else:
	print("NO")
