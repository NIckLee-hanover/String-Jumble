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

### prints reverse string
sl = (len(string)-1)
s2 = ""
def reverse(s):
    global s2, sl
    for i in range(len(s)):
        s2 = ("{0}{1}".format(s2, s[sl]))
        sl -= 1
reverse(string)
print(s2)

### finds single word
wl = ""
def word(s,n):
    global wl
    while s[n] != " ":
        wl = ("{0}{1}".format(wl, s[n]))
        n += 1
        if n == len(s):
            break

### yoda talk here
s3 = ""
letter = 0
while letter < len(string):
    wl = ""
    word(string,letter)
    s3 = ("{1} {0}".format(s3, wl))
    legnth = len(wl)
    letter += ((legnth)+1)
print (s3)

### last step.
s2 = "" # resets the s2 variable for the reverse function
s3 = s3[:-1] # the last char of s3 is a space and will apear in the beginning of the last line
reverse(s3)
print(s2)












