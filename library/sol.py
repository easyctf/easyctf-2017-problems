# http://oeis.org/A001333

mat = [[0,0,1,0],[0,1,0,1],[1,0,2,0],[0,2,0,1]]
mod = 10**9+7

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

x = 2**10240+3
print trace(matpow(mat, x))%mod
