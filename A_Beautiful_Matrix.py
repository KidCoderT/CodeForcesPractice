
moves = 0

for i in range(5):
	row = input()
	if "1" in row:
		moves += abs(3 - (row.split(" ").index("1") + 1))
		moves += abs(3 - (i + 1))

print(moves)
