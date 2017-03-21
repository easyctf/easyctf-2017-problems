from cStringIO import StringIO
import os
from Crypto.Util import number

flag = "wow_"

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def randleetify(s, random):
    i = list(s)
    for c in range(len(i)):
        if i[c] == 'i':
            if random.random() > 0.66:
                i[c] = '1'
            elif random.random() > 0.33:
                i[c] = 'I'
        elif i[c] == 'o':
            if random.random() > 0.66:
                i[c] = '0'
            elif random.random() > 0.33:
                i[c] = 'O'
        elif i[c] == 'a':
            if random.random() > 0.66:
                i[c] = '4'
            elif random.random() > 0.33:
                i[c] = 'A'
        elif i[c] == 'l':
            if random.random() > 0.66:
                i[c] = '1'
            elif random.random() > 0.33:
                i[c] = 'L'
        elif i[c] == 's':
            if random.random() > 0.66:
                i[c] = '5'
            elif random.random() > 0.33:
                i[c] = 'S'
        elif i[c] == 'e':
            if random.random() > 0.66:
                i[c] = '3'
            elif random.random() > 0.33:
                i[c] = 'E'
        elif i[c].isalpha():
            if random.random() > 0.5:
                i[c] = i[c].upper()
    return ''.join(i)

def get_problem(random):
    n_length = 2048

    p = number.getPrime(n_length, os.urandom)
    q = number.getPrime(n_length, os.urandom)
    n = p*q
    e = 65537
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    cut = len(bin(d).strip('0b').strip('L'))//2 - 2
    given = bin(d).strip('0b').strip('L')[cut:]
    deez = hex(int(given,2)).zfill(len(given)/4)
    salt = randleetify("i_probably_shouldnta_leeked_d",random)
    return (n, e, cut, deez, salt)

def generate_ciphertext(random):
    n, e, cut, deez, salt = get_problem(random)
    encoded = int(("easyctf{%s%s}" % (flag, salt)).encode('hex'),16)
    ciphertext =  'n: '+hex(n)+'\n'
    ciphertext += 'e: '+hex(e)+'\n'
    ciphertext += 'd: [??? '+str(cut)+' REDACTED BITS ???]'+str(deez)+'\n'
    ciphertext += 'c: '+hex(pow(encoded, e, n))+'\n'


    return StringIO(ciphertext)

def generate(random):
    return dict(files={
        "ciphertext.txt": generate_ciphertext
    })

def grade(random, key):
    n, e, cut, deez, salt = get_problem(random)
    if key.find("%s%s" % (flag, salt)) >= 0:
        return True, "Correct!"
    return False, "Nope."
