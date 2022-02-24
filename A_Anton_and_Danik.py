
matches_played = int(input())

result = input()

anton_win_amount = result.count('A')
danik_win_amount = len(result) - anton_win_amount

if anton_win_amount > danik_win_amount:
	print('Anton')
elif anton_win_amount < danik_win_amount:
	print('Danik')
else:
	print("Friendship")
