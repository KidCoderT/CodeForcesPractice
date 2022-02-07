
k, n, w = list(map(int, input().split(" ")))

# Total cost
tp = 0
for i in range(w):
	tp += k * (i+1)

# compare that to cost
if tp - n < 0:
	print(0)
else:
	print(tp - n)
