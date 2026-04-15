class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

f = [Data(0, 2), Data(1, 3), Data(2, 12), Data(5, 147)]
# Interpolation point and initialization
xi = 3  # the new data point at which we want to estimate the function's value
n = len(f)
result = 0.0
# Compute the Lagrange Interpolation inline
for i in range(n):
    term = f[i].y
    for j in range(n):
        if j != i:
            term *= (xi - f[j].x) / (f[i].x - f[j].x)
    result += term
# Display the output
print("Value of f(3) is:", result)
