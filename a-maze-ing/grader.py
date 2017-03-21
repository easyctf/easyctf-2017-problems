def grade(autogen, answer):
	if len(answer)>= 25:
 		return True, "You guessed right!"
 	return False, "Nope. The maze is a bit longer than that."
