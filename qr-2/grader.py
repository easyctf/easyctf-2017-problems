def grade(autogen, answer):
    if answer.find("w0w_who_kn3w_that_Oboes_c0uld_mask_a_s3cr3t?") != -1:
        return True, "Congrats!"
    return False, "Nope, try again."
