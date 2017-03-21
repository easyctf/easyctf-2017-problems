Your librarian has a 2-row bookshelf that can contain N books in each row. She wants to know the number of ways that she can fill the bookshelf with red-colored books and blue-colored books such that no 2 red-colored books are adjacent to each other (horizontally or vertically).

Input: the integer, N (1<=N<=2^1024)

Output: the number of ways you can place red-colored books and blue-colored books onto a N-column bookshelf. Since this number might be really big, output it mod 10^9+7.

Example:
Input: 2

Your valid bookshelf layouts are:
```
BB
BB

BB
BR

BR
BB

RB
BB

BB
RB

RB
BR

BR
RB
```
Therefore, 
Output: 7
