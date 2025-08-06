# This code calculates the area of a circle based on user input for the radius.
r=int(input("Enter a number: "))
c=3.14*r**2
print("Area of circle:", c)


#greater than from tow num

n1=100
n2=20 

if n1 > n2:
    print("n1 is great")
else:

    print("n2 is greater")



#greater than from three num

n1=100
n2=20 
n3=30
if n1 > n2:
    print("n1 is great")
elif n2 > n3:

    print("n2 is greater")
else:
    print("n3 is greater")


#sum of two numbers

n1=10
n2=20
print(n1+n2)


#product of two numbers

n1=1244
n2=8690
print(n1*n2)

# even number

n1=9
for i in range( 9,100+1):
    if i % 2 == 0:
        print(i, end=" ")

#prime number

n = int(input("Enter a number: "))
if n%1==0 and n%n==0:
    print("Prime number")
else:
    print("Not a prime number")


# type conversion
n1="122"
n2=12.34

n11=int(n1)
n22=int(n2)
print(n11)
print(n22)


#multi input and display

num=list(map(int, input("Enter numbers separated by space: ").split()))
num.sort()
print("Numbers:", num)


# program that takes 25 marks as input from the user and calculates the total marks and average.
n=25
for i in range (n):
    m=int(input("mark:"))
    t=0
    t+=m
    print("Total marks:", t/m)

# program that keeps asking the user to enter numbers until a multiple of 10 is entered.


n=int(input("Enter a number: "))
while n%10!=0:
    n=int(input("Enter a number: "))  
    

#program that displays all the numbers entered by the user except multiples of 10.

n=int(input("Enter a number 1: "))
while n%10!=0:
    print(n)
    n=int(input("Enter a number 2: "))
else:
    n=int (input("enter the num3:"))



