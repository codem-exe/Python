print("\n\n*** SECANT METHOD IMPLEMENTATION ***")

# Input Section
x0 = float(input("Enter First Guess: "))  
x1 = float(input("Enter Second Guess: "))  
e = float(input("Tolerable Error: "))  
N = int(input("Maximum Step: "))  

step = 1
condition = True  

while condition:  
    if (x1 - x0) == 0:  
        print("Divide by zero error!")  
        break  

    # Compute the next approximation
    x2 = x0 - (x1 - x0) * ((x0**3 - 5*x0 - 9) / ((x1**3 - 5*x1 - 9) - (x0**3 - 5*x0 - 9)))  

    print(f"Iteration-{step}, x2 = {x2:.6f} and f(x2) = {(x2**3 - 5*x2 - 9):.6f}")  

    x0 = x1  
    x1 = x2  
    step += 1  

    if step > N:  
        print("Not Convergent!")  
        break  

    condition = abs(x2**3 - 5*x2 - 9) > e  

print("\nRequired root is: %0.8f" % x2)  
