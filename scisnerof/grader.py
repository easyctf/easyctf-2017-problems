def grade(autogen, answer):
    if answer.find("r3v3r5ed_4ensics") != -1:
        return True, "Correct!"
    return False, "Nope, try again."
