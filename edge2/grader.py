def grade(random, key):
    if key.find("hiding_the_problem_doesn't_mean_it's_gone!") != -1:
        return True, "Correct!"
    return False, "Nope."
