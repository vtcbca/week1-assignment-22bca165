#Write a python script to enter any number and print the sum of its digit.
def sumofitsdigit(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    print("Sum of digit is {}".format(sum))

n=int(input("Enter any number:"))
sumofitsdigit(n)