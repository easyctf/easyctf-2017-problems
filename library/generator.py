import random
C = input()

if C==1:
  print 1
elif C==2:
  print 2
elif C==3 or C==4:
  print random.randint(3, 100)
else:
  print random.randint(2**(C**3-1), 2**(C**3))
