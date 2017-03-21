from cStringIO import StringIO

def get_flag(random):
    n = random.randint(10**16, 10**19)
    return n

def generate_phunky(random):
    n = get_flag(random)
    digs = [n + ord(t) for t in 'easyctf']
    prog = 'x = 0 # REDACTED\ndigs = {}\nout = ""\nfor letter in reversed(digs):\n    out = chr(letter - x) + out\nprint out'.format(str(digs))
    return StringIO(prog)

def generate(random):
    return dict(files={
        "phunky1.py": generate_phunky
    })

def grade(random, key):
    n = get_flag(random)
    if key.find("%d" % n) >= 0:
        return True, "Nice work!"
    return False, "Nope."