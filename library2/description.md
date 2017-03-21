Your librarian is back again with another challenge for you. She recently acquired a dictionary of an alien language. However, she has no way to read it and understand the language because she doesn't know any of the words in it. She wants to know the minimum number of alien words she needs to know in order to be able to understand the entire dictionary.

Input:

```
N (number of words in the dictionary)
word1: list of words in word1 definition
word2: list of words in word2 definition
... etc
```

Output:

an integer representing the minimum number of words required to understand whole dictionary


Ex:

Input:
```
5
arggiq: blah iz yiq
blah: ok
iz: ok blah
yiq: ok iz
ok: blah
```

Output:
```
1
```

Explanation: 

If you understand the word 'ok', you can understand the word 'blah'. If you understand 'ok' and 'blah', you can understand 'iz'. 'iz', and 'ok' lets you understand 'yiq'. 'yiq', 'iz', and 'blah' let you understand 'arggiq'.
