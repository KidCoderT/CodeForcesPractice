
n, k = list(map(int, input().split(" ")))

for step in range(k):
	if int(str(n)[-1]) > 0:
		n -= 1
	else:
		n //= 10

print(n)
