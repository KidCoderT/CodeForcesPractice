
n, t = list(map(int, input().split(" ")))
que = input()

for second in range(t):
	new_que = []
	for index, student in enumerate(que[:-1]):
		if len(new_que) == index + 1: continue
		if student == "B" and que[index + 1] == "G":
			new_que.append("G")
			new_que.append("B")
		else:
			new_que.append(student)
	
	if len(new_que) != n: new_que.append(que[-1])

	que = new_que

print(''.join(que))
