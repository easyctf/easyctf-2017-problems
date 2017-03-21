from cStringIO import StringIO

def get_flag(random):
    n = random.randint(10**16, 10**19)
    return n

def generate_phunky(random):
    n = get_flag(random)
    n *= n - 1
    n = [int(u) for u in str(n)]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]
    big = 1
    for i in range(len(n)):
        big *= primes[i] ** n[i]
    prog = 'import operator\njkx = 0 # REDACTED\npork = ((12*jkx+44)/4)-(1234/617)*jkx-sum([1, 4, 7])\njkx *= pork\npp = filter(lambda g: not any(g % u == 0 for u in range(2, g)), range(2, 10000))\nb = reduce(operator.mul, (pp[i] ** int(str(jkx)[i]) for i in range(len(str(jkx)))))\nprint b == {}'.format(str(big))
    return StringIO(prog)

def generate(random):
    return dict(files={
        "phunky2.py": generate_phunky
    })

def grade(random, key):
    n = get_flag(random)
    if key.find("%d" % n) >= 0:
        return True, "Nice work!"
    return False, "Nope."