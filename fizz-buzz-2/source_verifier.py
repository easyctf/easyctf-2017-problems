import sys

code = sys.stdin.read()

if ("i" in code) or ("I" in code) or ("?" in code) or ("eval" in code) or ("exec" in code):
  print "Your program contains an 'i', 'I', or '?'. Please remove it and try again."
else:
  print "OK"
