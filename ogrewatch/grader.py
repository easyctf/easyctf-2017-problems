def grade(autogen, answer):
    if answer.find("subs_r_b3tt3r_th@n_dub5") != -1:
        return True, "Correct!"
    return False, "Nope, try again."
