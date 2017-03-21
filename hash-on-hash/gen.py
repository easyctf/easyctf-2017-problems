import hashlib
f = open('input.txt', 'r')
dat = f.read()
f.close()
out = open('hashed.txt', 'w')
letters = set(list(dat))
hashDict = {}
backDict = {}
for c in letters :
    hashDict[c] = hashlib.md5(str(c)).hexdigest()
    backDict[hashDict[c]] = c
res = ''
for c in dat :
    res += hashDict[c] + '\n'
out.write(res)
out.close()
checkWork = ''
for tmp in res.split('\n') :
    if tmp == '' :
        continue
    checkWork += backDict[tmp]
print checkWork
