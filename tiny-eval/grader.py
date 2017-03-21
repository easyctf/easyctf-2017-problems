def grade(autogen, key):
    if key.find("it's_2017_anD_we're_still_using_PHP???") != -1:
        return True, "You got it!"
    return False, "Nope. Keep poking around."
