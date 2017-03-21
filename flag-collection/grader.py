def grade(autogen, answer):
    if answer.find("thumbs.db_c4n_b3_useful") != -1:
        return True, "wowie! thumbs up"
    return False, "Nope, try again."
