
n = int(input())
row = list(input())

stones_removed = 0
for i, stone in enumerate(row[:-1]):
	try:
		if stone == row[i + 1]:
			stones_removed += 1
	except:
		pass

print(stones_removed)

