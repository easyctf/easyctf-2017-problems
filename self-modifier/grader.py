def grade(random, key):
    if key.find("hj3-0p9cgfb-ez") != -1:
        return True, "Correct!"
    incorrect_txt = 'Wrong. '
    if key.find("hj3") == -1:
    	incorrect_txt += "Phase 1 failed. "
    if key.find("-0p9") == -1:
    	incorrect_txt += "Phase 2 failed. "
    if key.find("cgfb") == -1:
    	incorrect_txt += "Phase 3 failed. "
    if key.find("-ez") == -1:
    	incorrect_txt += "Phase 4 failed. "
    return False, incorrect_txt
