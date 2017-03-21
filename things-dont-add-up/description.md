Mikel is going out for McDawnald's, and he has some very specific dietary restrictions - he can only eat certain amounts of chicken nuggets! He's a pretty secretive dude, so he won't
tell you in advance which amounts he can and cannot eat. However, you've known Mikel for years, so you know he eats between `A` and `B` chicken nuggets (inclusive) during any given McDawnald's visit.

The McDawnald's you're going to sells nuggets in `N` different amounts, and because Mikel is thrifty and broke from running a CTF, he will eat every single nugget that is purchased - that is,
there must be no nuggets left over. Once you get to McDawnald's, Mikel will tell you how many nuggets he wants to eat, but you need to be ready for anything, so your task is as follows:

Given a range `[A, B]` from which Mikel's required nugget count will be chosen from, count the number of potential nugget orders which will be impossible to fulfill given the McDawnald's different
nugget serving amounts.

The first line contains three integers `A B N`. The second line contains a series of `N` integers `d_1, d_2, ..., d_N`, representing all of the different nugget amounts. Output a single integer, the answer to the problem above.

#### Input Constraints

`0 < N <= 16`

`0 < A < B <= 10000000`

`0 < d_i <= 10000000`

#### Sample Input

```
8 15 3
4 9 11
```

#### Sample Output

`2`

#### Explanation

By some combination of nuggets, all but 2 total amounts in the range `[8, 15]` can be constructed. For example, you can buy 13 nuggets by getting an order of 9 and an order of 4, as `13 = 4 + 9`. However,
there is no way to create a plate of either 10 or 11 nuggets. That's two impossible amounts, so we output `2`.