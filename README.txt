Use AI to perform search for sets of words that can potentially form a pangram
Will need natural language processing to perform verification.

There are 102401 allwed words in the `look` command; but only 26598 of them has no repeated letters.

Assuming a maximum of 9 letters can be formed, I'll have to churn through
26598^9 = 6662555428887541561421351787796520805888 letters
That's gonna need some C++ or even machine code.
