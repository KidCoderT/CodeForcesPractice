
n = int(input())

x = 0

for i in range(n):
	statement = input().split("X")
	
	if statement[0] == "":
		statement = statement[1]
	else:
		statement = statement[0]

	if statement == "++":
		x += 1
	elif statement == "--":
		x -= 1

print(x)
