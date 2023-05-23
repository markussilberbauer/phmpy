import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

dt = 0.01
t = np.arange(-np.pi,np.pi,dt)
p = np.empty((t.size, 2))
p[:, 0] = np.cos(t)
p[:, 1] = 0.5 * np.sin(t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_aspect("equal")
ax.grid()

plot, = ax.plot(p[:, 0],p[:, 1])
punkt, = ax.plot([0], [0], 'o', color='red')

def update(n):
    punkt.set_data(np.array(p[n]))
    return punkt, plot

ani = mpl.animation.FuncAnimation(fig, update, interval=30, frames=t.size, blit=True)
plt.show()

