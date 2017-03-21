N = input()

if N == 0:
    print '8 15 3\n4 9 11'
elif N == 1:
    print '50 55 3\n7 24 33'
elif N == 2:
    print '123 456 3\n5 7 11'
elif N == 3:
    print '1 10000000 16 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'
else:
    import random as r
    r.seed(N)
    lo = r.randint(1, 5000000)
    hi = r.randint(lo + 1, 10000000)
    N = 16
    nugs = [str(r.randint(1, 10000000)) for i in range(16)]
    print '%d %d 16\n%s' % (lo, hi, ' '.join(nugs))