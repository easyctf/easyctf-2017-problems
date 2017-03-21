def grade(autogen, key):
    if key.find("better_thank_the_french_for_this_one") != -1:
        return True, "Correct!"
    return False, "Nope!"
