def grade(autogen, key):
    if key.upper().find("DO_YOU_HEAR_THE_C_SHELLS_BASHING_AGAINST_THE_C_SHORE") != -1:
        return True, "Correct!"
    return False, "Nope!"
