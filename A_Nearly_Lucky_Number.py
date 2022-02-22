
n = int(input())

no_of_4s = str(n).count('4')
no_of_7s = str(n).count('7')

if no_of_4s + no_of_7s == len(str(n)):
	print("YES")
elif (no_of_4s + no_of_7s % 4 == 0 and no_of_4s != 0) or (no_of_4s + no_of_7s % 7 == 0 and no_of_7s != 0):
	print("YES")
else:
	print("NO")
