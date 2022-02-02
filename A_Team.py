
n = int(input())

solvable_problems = 0

for i in range(n):
	k = list(
		map(
			int,
			input().split(" ")
		)
	)

	while 0 in k:
		k.remove(0)
	
	if len(k) > 1:
		solvable_problems += 1
	
print(solvable_problems)
