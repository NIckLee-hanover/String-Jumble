"""
stringjumble.py
Author: Nick Lee
Credit: Probably a lot but we'll see

Assignment: String jumble

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

string = input("Please enter a string of text (the bigger the better): ")


def reverse(s): # string reversing function
    s2 = ""
    letter = int(len(s)-1)
    for i in range(len(s)):
        s2 = ("{0}{1}".format(s2, s[letter]))
        letter -= 1
    print(s2)

def word(s,n):
    s2 = ""
    while s[n] != " " or n < 0:
        s2 = ("{0}{1}".format(s2, s[n]))
        n -= 1
        print(s[n])
    del(s2,0)

print(word(string, int(len(string)-1)))

reverse(string)







