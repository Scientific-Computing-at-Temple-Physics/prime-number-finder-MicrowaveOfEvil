# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)

print("This program will find prime numbers. Choose two positive integers to find primes between: ")
# These functions will ask you for your number ranges, and assign them to 'x1' and 'x2'
x1 = int(raw_input('Smallest number to check: '))
x2 = int(raw_input('Largest number to check: '))
if x2<x1:
    two=x2
    one=x1
    x2=one
    x1=two
    print("Your first number was higher than the second. I reversed those for you")


if x1<0 or x2<0:
    print("Please input positive integers") #For catching errors at the beginning.
else:
    primeslist=[]
    for counter in range(x1,x2+1):
        checker=True
        for number in range (2,int(ma.ceil(ma.sqrt(counter)+1))):#Doesn't include 1 or the number itself, since those wouldn't count in searching for primes
            if float(counter)/number==counter/number:
                checker=False
            if counter==1:
                checker=False
        if checker==True:
            primeslist.append(counter)
    print "Attempting to find primes between",x1,"and", x2
    print ("...")
    for walker in range(1,len(primeslist)+1):
        print(primeslist[walker-1])#This seems like a better/more readable format than just printing the list
    if len(primeslist)==0:
        print("No primes found")
if x2==x1:
    print("You put in the same number twice. There are zero primes between that number and itself.")
    if len(primeslist)>0:
        print ("However, that number is itself a prime.")
else:
    print("There are "+str(len(primeslist))+" primes between "+str(x1)+" and "+str(x2))


""" Text enclosed in triple quotes is also a comment.
This code should find and output all prime numbers between (and including) the numbers entered initially.
If no prime numbers are found in that range, it should print a statement to the user.
Now we end the comment with triple quotes."""

# The rest is up to you!
