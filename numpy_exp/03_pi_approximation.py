import numpy as np
import matplotlib.pyplot as plt

total = 100000
x = np.random.uniform(-1, 1, total)
y = np.random.uniform(-1, 1, total)

distance = x**2 + y**2
inside = distance <= 1

count_inside = np.sum(inside)
pi_est = 4 * count_inside / total

print(f"Total points: {total}")
print(f"Points inside circle: {count_inside}")
print(f"Estimated PI: {pi_est}")
print(f"Actual PI: {np.pi}")
print(f"Error: {abs(pi_est - np.pi):.6f}")

sample = 2000
x_sample = x[:sample]
y_sample = y[:sample]
inside_sample = inside[:sample]

fig, ax = plt.subplots(figsize=(8, 8))

ax.scatter(x_sample[inside_sample], y_sample[inside_sample],
           c='green', s=2, alpha=0.6, label='Inside')
ax.scatter(x_sample[~inside_sample], y_sample[~inside_sample],
           c='red', s=2, alpha=0.6, label='Outside')

theta = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(theta), np.sin(theta), 'b-', linewidth=2)

ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.set_title(f'Monte Carlo PI Estimation: {pi_est:.4f}')
ax.legend()

plt.savefig('03_pi_estimation.png', dpi=150)
plt.show()
