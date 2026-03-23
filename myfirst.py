import cvxpy as cp

# Create 2 scalar optimization variables
x = cp.Variable()
y = cp.Variable()

# Create 2 constraints
constraints = [
    x + y == 1,
    x - y >= 1
]

# Form objective
obj = cp.Minimize((x -y) ** 2)

# Form and solve problem
prob = cp.Problem(obj, constraints)
prob.solve()
print('status:', prob.status)
print('optimal value:', prob.value)
print('optimal var:', x.value, y.value)