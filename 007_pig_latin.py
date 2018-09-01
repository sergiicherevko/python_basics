# get sentence from user

original = input("Enter any sentence: ").lower().strip()

# split sentence into words

words = original.split()

# loop through the words in convert them into pig latin

new_words = []
    # If starts with vowel "aeiou", just add "yay"
    # Otherwise move first consonant cluser to the end and add "ay"
for word in words:
	if word[0] in "aeiou":
		new_word = word + "yay"
		new_words.append(new_word)
	else:
		vowel_pos = 0
		for letter in word:
			if letter not in "aeiou":
				vowel_pos = vowel_pos + 1
			else:
				break
		cons = word[:vowel_pos]
		the_rest = word[vowel_pos:]
		new_word = the_rest + cons + "ay"
		new_words.append(new_word)

# stick words back together

output = " ".join(new_words)

# output final string

print(output)