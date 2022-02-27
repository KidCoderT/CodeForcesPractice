
n, h = list(map(int, input().split()))

a = list(map(int, input().split()))

total_width = 0
for i in a:
	if i <= h:
		total_width += 1
	else:
		total_width += 2

print(total_width)
