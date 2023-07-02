#Write a python script to enter any string and count vowel.
def vowel(s):
    c=0
    v=['a','A','e','E','i','I','o','O','u','U']
    for i in s:
        if i in v:
            c=c+1
    print("Total number of vowel is {}.".format(c))

s=input("Enter a string:")
vowel(s)