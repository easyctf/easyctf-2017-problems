def grade(autogen, key):
    try:
        a, b = map(int, key.split(":"))
        c = a ^ b
        d = 98 + c
        e = ~d + b
        f = e ^ a
        g = a + b * c / d ^ e + f
        if g != -814:
            raise Exception("lol")
        return True, "Nice!"
    except:
        return False, "Nope. Keep trying!"
