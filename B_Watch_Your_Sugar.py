
n = int(input())
sugar_limit = int(input())

chocolate_options = list(map(int, input().split()))

grams_consumed = 0
eaten_amount = 0
for chocolate in chocolate_options:
	if grams_consumed + chocolate < sugar_limit:
		eaten_amount += 1
		grams_consumed += chocolate
print(eaten_amount)
