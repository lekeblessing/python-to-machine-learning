#!/usr/bin/python3
"""a file that explains the use of an extend for a list"""


vowels = ["a","e","i", "o", "u"]
digit = [1,2,3,4,5]

# vowels.extend(digit)
combine = vowels + digit
digit.append(vowels)
com_bine = digit

print(combine)
print(digit)