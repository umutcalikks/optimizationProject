import numpy as np
from optimizers import Optimizer

# Adjustable as wished.
alpha: float = 10
beta: float = 1

# Heuristic
f = lambda x: -alpha * x / (x**2 + 1) + beta / x

optimizer = Optimizer(f, "Heuristic approach", alpha=0.1)
# Increased the learning rate for this application.

print(optimizer)

print("A convex range: ", optimizer.convexify(np.arange(1, 3, 0.1)))
optimizer.optimize("newton", 1)
optimizer.optimize("gradient", 2, iterations=30)
optimizer.optimize("golden", interval=np.arange(0, 5, 0.1))

print("Found extrema points: \n", optimizer.extrema())

