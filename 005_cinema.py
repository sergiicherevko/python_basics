films = {
	"Fight Club": [16, 2], #[age, number of tickets]
	"God Father": [16, 4],
	"Shoe Shank Redemption": [16, 6],
	"Forrest Gump": [16, 8]
}

while True:
	choice = input("Which movie you'd like to see?: ").strip().title()
	if choice in films:
		age = int(input("How old are you?: ").strip())
		if age >= films[choice][0]:
			if films[choice][1] > 0:
				print("Enjoy the movie!")	
				films[choice][1] = films[choice][1] - 1
			else:
				print("Sorry, sold out.")	
		else:
			print("Sorry, you are not old enough")
	else:
		print("We don't have that film.")	