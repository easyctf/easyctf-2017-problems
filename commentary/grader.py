def grade(autogen, answer):
	if answer.find("yougotit")!=-1:
		return True, "Correct!"
	return False, "Nope, try again."
