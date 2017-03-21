def grade(autogen, key):
    if key.find("a_prepared_statement_a_day_keeps_the_d0ctor_away!") != -1:
        return True, "You got it!"
    return False, "Nope. Keep poking around."
