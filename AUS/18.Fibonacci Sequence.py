# Python Program to Print the Fibonacci Sequence

n = int(input("Enter the number of terms: "))

a,b = 0,1
count = 0

if n < 0:
    print("Please enter a positive integer!!")
elif n == 1:
    print("Fibonacci Sequence Upto One Term:")
    print(a)
else:
    print("FIBONACCI SEQUENCE: ")
    while count < n:
        print(a)
        next_term = a + b
        a = b
        b = next_term
        count += 1