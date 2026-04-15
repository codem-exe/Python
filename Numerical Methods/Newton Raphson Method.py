# Python3 code for implementation of Newton-Raphson Method without functions

# Initial guess
x = -20  

# Newton-Raphson iteration
while True:
    fx = x**3 - x**2 + 2  # f(x) = x^3 - x^2 + 2
    dfx = 3*x**2 - 2*x    # f'(x) = 3x^2 - 2x
    
    h = fx / dfx  # Compute step size
    
    if abs(h) < 0.0001:  # Convergence condition
        break
    
    x = x - h  # Update x

# Print result
print("The value of the root is:", "%.4f" % x)
