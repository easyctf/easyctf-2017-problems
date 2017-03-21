When making pairings between two sets of objects based on their preferences (in this case people), there can be multiple stable solutions, stable meaning that no two elements would prefer to be matched with each other over their current matching.
A side-effect of having multiple solutions is that there are solutions favor one group over the other.

We received two files, one listing men and the other women. Each line contains a name, followed by a series of numbers. Each number N corresponds to their preference to be matched with the Nth member of the opposite list, with 1 being the highest.

For example, the entry "Joe 4, 5, 3, 1, 2" means that Joe would most prefer the 4th entry on the opposite list, and least prefer the 2nd.

We have heard that there are some pairings that will be together in all possible stable matchings, please find them. However, because there are quite a bit of them, please submit your solution as the following:

MD5 hash of `(male_1,female_1)(male_2,female_2)...(male_n,female_n)`, where the pairings are sorted alphabetically by male names. For example, `(Bob,Susie)(Jim,Carol)(Tom,Emma)` would be submitted as `b0d75104ce4b3a7d892f745fd515fea4`.

Here are the lists of preferences:[male preferences](${male_prefs_txt}), [female preferences](${female_prefs_txt}).
