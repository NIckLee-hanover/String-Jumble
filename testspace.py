"""
testspace.py
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
# variables 
j = (len(string)-1)
s2 = ""
s3 = ""
letter = 0
### prints reverse string
def reverse(s):
    global s2, j
    for i in range(len(string)):
        s2 = ("{0}{1}".format(s2, string[j]))
        j -= 1
    
print(s2)
### finds single word
ws = ""
def word(s,n):
    global ws
    while s[n] != " ":
        ws = ("{0}{1}".format(ws, s[n]))
        n += 1
        if n == len(s):
            break
### yoda talk here
while letter < len(string):
    ws = ""
    word(string,letter)
    s3 = ("{1} {0} ".format(s3, ws))
    loop = len(ws)
    letter += ((loop)+1)



print (s3)












