import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x + 1

x_values = [x * 0.1 for x in range(-100, 100)]
y_values = [f(x) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.title(r"Graph of $f(x) = x^3 - 2x + 1$")
plt.show()
