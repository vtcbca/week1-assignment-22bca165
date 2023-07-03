#Write a python script to enter any number and print the sum of its digit.
def sumofitsdigit(n):
    sum=0
    for i in str(n):
        sum=sum+int(i)
    print("Sum of digit is {}.".format(sum))

n=int(input("Enter any number:"))
sumofitsdigit(n)
