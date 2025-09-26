import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(500)*10
y = np.random.rand(500)*10
sizes = np.random.rand(500)*20
colors = np.random.rand(500)

plt.scatter(x,y,s=sizes,c=colors,cmap='twilight',alpha=0.8)
plt.axis('off')
plt.show()
