import numpy as np
import matplotlib.pyplot as plt

u = np.random.uniform(0, 1, 10000)
n = np.random.normal(0, 1, 10000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(u, bins=50, color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_title('Uniform Distribution (0, 1)')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')

ax2.hist(n, bins=50, color='coral', edgecolor='black', alpha=0.7)
ax2.set_title('Normal Distribution (mean=0, std=1)')
ax2.set_xlabel('Value')
ax2.set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('02_histograms.png', dpi=150)
plt.show()

print("Uniform: all values equally likely in range [0,1] - flat histogram")
print("Normal: values cluster around mean, bell curve shape, tails extend to infinity")
