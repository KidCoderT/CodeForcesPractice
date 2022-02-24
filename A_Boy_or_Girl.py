
username = input()

# convert to a set to remove duplicates
username = set(list(username))

if len(username) % 2 != 0: # use is male
	print("IGNORE HIM!")
else: # user is female
	print("CHAT WITH HER!")


# 18 min 14 Sec