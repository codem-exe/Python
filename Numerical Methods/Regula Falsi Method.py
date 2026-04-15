MAX_ITER = 1000000

# Define the equation directly in the script
a = -200
b = 300

# Check if the initial guesses bracket a root:
if ((a**3 - a**2 + 2) * (b**3 - b**2 + 2)) >= 0:
    print("You have not assumed right a and b")
else:
    c = a  # Initial approximation (will be updated)
    for i in range(MAX_ITER):
        # Compute function values inline:
        fa = a**3 - a**2 + 2
        fb = b**3 - b**2 + 2

        # Compute c using the Regula Falsi formula:
        c = (a * fb - b * fa) / (fb - fa)
        fc = c**3 - c**2 + 2  # Compute f(c)

        # Check if we found an exact root:
        if fc == 0:
            break

        # Update the interval:
        if fc * fa < 0:
            b = c
        else:
            a = c

    print("The value of root is : ", '%.f' % c)
