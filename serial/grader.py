def grade(random, key):
    if key.find("easyctf{s3r1Al_F0rMat5_R_GreAT}") != -1:
        return True, "01000011 01101111 01110010 01110010 01100101 01100011 01110100 00100001" #"Correct!".toBin()
    return False, "Nope."