# Input Section
x0 = float(input("First Guess: "))  # Lower bound
x1 = float(input("Second Guess: "))  # Upper bound
e = float(input("Tolerable Error: "))  # Precision level

# Check if initial guesses are valid
if (x0**3 - 5*x0 - 9) * (x1**3 - 5*x1 - 9) > 0.0:
    print("Given guess values do not bracket the root.")
    print("Try again with different guess values.")
else:
    step = 1
    condition = True
    print("\n\n*** BISECTION METHOD IMPLEMENTATION ***")

    while condition:
        x2 = (x0 + x1) / 2  # Midpoint
        f_x2 = x2**3 - 5*x2 - 9  # Evaluate f(x2)

        print(f"Iteration:{step}, x2 = {x2:.6f}, f(x2) = {f_x2:.6f}")

        if (x0**3 - 5*x0 - 9) * f_x2 < 0:
            x1 = x2  # Root lies in [x0, x2]
        else:
            x0 = x2  # Root lies in [x2, x1]

        step += 1
        condition = abs(f_x2) > e  # Stop when error tolerance is met

    print(f"\nRequired Root is: {x2:.8f}")
