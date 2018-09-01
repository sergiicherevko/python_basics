known_users = ["Sergii", "Kate", "Peter", "Alice"]

print(len(known_users))

while True:
	print("Lets check if your name is on the list.")
	name = input("What is your name?: ").strip().capitalize()

	if name in known_users:
		print("Name {} is on the list!".format(name))
		remove = input("Would you like to remove your name from the list (y/n)? ").strip().lower()
		if remove == "y":
			known_users.remove(name)
	else:
		print("Name {} is not on the list!".format(name))
		add = input("Would you like to add your name to the list (y/n)? ").strip().lower()
		if add == "y":
			known_users.append(name)