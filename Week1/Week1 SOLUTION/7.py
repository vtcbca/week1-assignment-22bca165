#Write a python script to enter any string, replace vowel with its position number.
def replace_vowels_with_position(s):
    o=''
    v=['a','A','e','E','i','I','o','O','u','U']
    for i in s:
         if i in v:
              o=o+str(s.index(i))
         else:
              o=o+i
    print(o)

s=input("Enter a string:")
replace_vowels_with_position(s)
        
        




