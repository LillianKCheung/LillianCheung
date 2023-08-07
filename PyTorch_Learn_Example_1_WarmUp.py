import numpy as np
import math
import matplotlib.pyplot as plt

# Create ground-truth input and output data
x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

# Use back-propagation to fit model to data
# Randomly initialize weights
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    # y_pred = a + b * x + c * x^2 + d * x^3
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = np.square(y_pred - y).sum()
    if t % 100 == 99:
        print(t, loss)

    # Back propagate to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')

# Plot data and best fit model
plt.plot(x, y, label="Sin(x)")
plt.plot(x, y_pred, label="3rd order poly fit by ML")
plt.title("Learning PyTorch - Using ML to Fit Sin(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
