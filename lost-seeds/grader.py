def grade(autogen, answer):
    if answer.find("r3ndom_numb3rs_m3an_n0thing_wh3n_y0u_can_brute_force!") != -1:
        return True, "Correct!"
    return False, "Nope, try again."
