def generate(random):
	key = "".join([random.choice("0123456789abcdef") for i in range(32)])
	return dict(variables={
		"key": key
	})

def grade(autogen, answer):
	key = "".join([autogen.choice("0123456789abcdef") for i in range(32)])
	autogen.seed("super%secretkeylalalala" % key)
	flag = "".join([autogen.choice("0123456789abcdef") for i in range(32)])
	if answer.find(flag) != -1:
		return True, "Correct!"
	return False, "Nope, try again."
