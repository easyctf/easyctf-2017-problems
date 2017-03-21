def grade(autogen, answer):
    if answer.find("n0w_who-w0u1d_do_thAT_to_Th3ir_QR?") != -1:
        return True, "Congrats!"
    return False, "Nope, try again."