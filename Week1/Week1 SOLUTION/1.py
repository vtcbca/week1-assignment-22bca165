#Write a python script to enter any number and check its prime or not.
def prime(n):
    a=True
    for i in range(2,n):
        if n%i==0:
            a=False
    if a==True:
        print("Enter number is prime.") 
    else:
        print("Enter number is not prime.")  

n=int(input("Enter any number:"))
prime(n)