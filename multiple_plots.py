import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(-5 * np.pi, 5 * np.pi, 100)

# Plot lines
plt.plot(x, x, color='blue', linewidth=1, label='x')  # Line: x
plt.plot(x, -x, color='blue', linewidth=1, label='-x')  # Line: -x
plt.plot(x, np.sin(x), color='green', linewidth=2, label='sin(x)')  # Line: sin(x)
plt.plot(x, x *np.sin(x), color='red', linewidth=4, label='xsin(x)')  # Line: sin(x)

# Add title and labels
plt.title('Multiple Lines Plot', fontsize=16, pad=15)
plt.xlabel('x', fontsize=14, labelpad=10)
plt.ylabel('y', fontsize=14, labelpad=10)

# Add grid and legend
# plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# Show plot
plt.show()
