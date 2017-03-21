# Very easy problem. Compute a few values w/ brute force or something, then check OEIS.
# Part of: https://oeis.org/A001333
# Tells us:  f(n) = (1/4) * Trace( [[0,0,1,0],[0,1,0,1],[1,0,2,0],[0,2,0,1]] )
# just write a program to compute this quickly 
# this sol takes something like ~O(log n) i think?

x = input() + 1

mat = [[0,0,1,0],[0,1,0,1],[1,0,2,0],[0,2,0,1]]
mod = 10**9+7

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

def matmult(mtx_a, mtx_b, mod):
    tpos_b = zip( *mtx_b)
    rtn = [[ sum( ea*eb for ea,eb in zip(a,b))%mod for b in tpos_b] for a in mtx_a]
    return rtn

def trace(A):
    return sum(A[j][j] for j in range(len(A)))

def matpow(A, p):
    ret = A
    for bit in bin(p)[3:]:
        ret = matmult(ret, ret, mod)
        if bit=='1':
            ret = matmult(ret, A, mod)
    return ret

inv4 = modinv(4, mod)
ans = trace(matpow(mat, x))%mod
ans = (ans * inv4)% mod
print ans
