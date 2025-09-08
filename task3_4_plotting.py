#!/usr/bin/env python3
"""
Task 3 & 4: Matplotlib Plotting Examples
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("Task 3: Basic Matplotlib Plot")
print("=" * 60)

# Task 3: Run the provided script
plt.figure(figsize=(8, 6))
plt.plot([1,2,3,4], [1,2,7,14])
plt.axis([0, 6, 0, 20])
plt.title("Task 3: Basic Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.savefig('task3_plot.png', dpi=100, bbox_inches='tight')
# plt.show()  # Comment out for non-interactive mode

print("Task 3 plot saved as 'task3_plot.png'")

print("\n" + "=" * 60)
print("Task 4: Custom Matplotlib Figure")
print("=" * 60)

# Task 4: Create a custom figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Task 4: Custom Matplotlib Figure - Data Visualization Examples', fontsize=16)

# Subplot 1: Sine and Cosine waves
x = np.linspace(0, 2 * np.pi, 100)
axes[0, 0].plot(x, np.sin(x), 'b-', label='sin(x)')
axes[0, 0].plot(x, np.cos(x), 'r--', label='cos(x)')
axes[0, 0].set_title('Trigonometric Functions')
axes[0, 0].set_xlabel('x (radians)')
axes[0, 0].set_ylabel('y')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: Histogram
np.random.seed(42)
data = np.random.normal(100, 15, 1000)
axes[0, 1].hist(data, bins=30, color='green', alpha=0.7, edgecolor='black')
axes[0, 1].set_title('Normal Distribution (μ=100, σ=15)')
axes[0, 1].set_xlabel('Value')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].axvline(data.mean(), color='red', linestyle='dashed', linewidth=2, label=f'Mean: {data.mean():.1f}')
axes[0, 1].legend()

# Subplot 3: Scatter plot with color mapping
np.random.seed(42)
x_scatter = np.random.randn(100)
y_scatter = 2 * x_scatter + np.random.randn(100) * 0.5
colors = x_scatter + y_scatter
scatter = axes[1, 0].scatter(x_scatter, y_scatter, c=colors, cmap='viridis', alpha=0.6)
axes[1, 0].set_title('Scatter Plot with Correlation')
axes[1, 0].set_xlabel('X values')
axes[1, 0].set_ylabel('Y values')
plt.colorbar(scatter, ax=axes[1, 0], label='Sum of X+Y')

# Subplot 4: Bar chart
categories = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
values = [85, 72, 65, 58, 45]
colors_bar = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
bars = axes[1, 1].bar(categories, values, color=colors_bar)
axes[1, 1].set_title('Programming Language Popularity')
axes[1, 1].set_xlabel('Language')
axes[1, 1].set_ylabel('Popularity Score')
axes[1, 1].set_ylim(0, 100)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    axes[1, 1].text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('task4_custom_plot.png', dpi=100, bbox_inches='tight')
# plt.show()  # Comment out for non-interactive mode

print("Task 4 custom plot saved as 'task4_custom_plot.png'")
print("\n" + "=" * 60)
print("Tasks 3 and 4 completed successfully!")
print("=" * 60)