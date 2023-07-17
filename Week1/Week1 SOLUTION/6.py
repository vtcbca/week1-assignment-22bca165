#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
def print_part_of_string(a):
    s=input("Enter starting character:")
    e=input("Enter ending character:")
    start=a.index(s)
    end=a.index(e)
    print(a[start:end+1:])

a=input("Enter a string:")
print_part_of_string(a)
