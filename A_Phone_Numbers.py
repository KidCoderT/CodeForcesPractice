
n = int(input())

for i in range(n):
	name, number = input().split(" ")
	if sum(list(map(int, list(number)))) % 2 == 0:
		print(name)
