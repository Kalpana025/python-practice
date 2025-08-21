 n = int(input("Enter size of square: "))
for i in range(n):
    print("* " *n )


# rectangle 

n = int(input("Enter size of square: "))
m= int(input("Enter size of rectangle: "))
for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()  
print()      

#triangle
n = int(input("Enter size of square: "))     
for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print()

  # Code to print a pyramid pattern using stars
n = int(input("Enter the height of the pyramid: "))
for i in range(1, n + 1):
    # Print spaces
    for space in range(n - i):
        print(" ", end=" ")
    # Print stars
    for star in range(2 * i - 1):
        print("*", end=" ")
    print()  # Move to next line

n = int(input("Enter the height of the diamond (half): "))

for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end=" ")
    for star in range(2 * i - 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for space in range(n - i):
        print(" ", end=" ")
    for star in range(2 * i - 1):
        print("*", end=" ")
    print()



# Code to find number of two wheelers and four wheelers based on input of vehicles and wheels


vehicle = int(input("Enter number of vehicles: "))
wh = int(input("Enter number of wheels: "))
a1 = vehicle * 2
a2 = wh- a1
a3 = a2 / 2
print(" number of four wheelers: ",int(a3))
a4 = vehicle-a3
print(" number of two wheelers: ",int(a4))
