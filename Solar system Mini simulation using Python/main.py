import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Solar System (Animated)")

# Sun
ax.scatter(0, 0, s=400, c='yellow', label='Sun')

# Planet data: name, radius, color, size, angular speed
planets = [
    ("Mercury", 0.5, "gray", 20, 0.15),
    ("Venus",   1.0, "orange", 30, 0.12),
    ("Earth",   1.5, "blue", 40, 0.1),
    ("Mars",    2.2, "red", 30, 0.08),
    ("Jupiter", 3.5, "brown", 80, 0.05),
    ("Saturn",  5.0, "gold", 70, 0.03),
    ("Uranus",  6.5, "lightblue", 50, 0.02),
    ("Neptune", 8.0, "purple", 50, 0.015)
]

# Store scatter objects for planets
planet_scatter = []
for name, r, color, size, w in planets:
    sc = ax.scatter([], [], s=size, c=color, label=name)
    planet_scatter.append(sc)
    # Orbit lines
    theta = np.linspace(0, 2*np.pi, 500)
    ax.plot(r*np.cos(theta), r*np.sin(theta), linestyle="--", color="white", alpha=0.3)

ax.legend(loc="upper right", fontsize=8)

# Update function
def update(frame):
    t = frame / 5.0  # time scaling
    for (name, r, color, size, w), sc in zip(planets, planet_scatter):
        x = r * np.cos(w * t)
        y = r * np.sin(w * t)
        sc.set_offsets([x, y])
    return planet_scatter

# Animate
ani = FuncAnimation(fig, update, frames=1000, interval=50, blit=True)

plt.show()
