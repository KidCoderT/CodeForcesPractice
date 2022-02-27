
n = int(input())

people_on_train = 0
max_people_at_once = 0

for i in range(n):
	exited_people, entered_people = list(map(int, input().split()))
	people_on_train -= exited_people
	people_on_train += entered_people
	if people_on_train > max_people_at_once:
		max_people_at_once = people_on_train

print(max_people_at_once)
