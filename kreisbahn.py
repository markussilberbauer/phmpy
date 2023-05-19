import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

R = 3.0
T = 12.0
dt = 0.02
omega = 2 * np.pi / T

print(f"Bahngeschwindigkeit = {R*omega:.3f} m/s")
print(f"Zentripetalbeschleunigung = {R+omega**2: .3f} m/s²")

t = np.arange(0, T, dt)
r = np.empty((t.size, 2))

r[:, 0] = R * np.cos(omega * t)
r[:, 1] = R * np.sin(omega * t)

v = (r[1:, :] - r[:-1, :]) / dt
a = (v[1:, :] - v[:-1, :]) / dt

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_xlim(-1.2 * R, 1.2 * R)
ax.set_ylim(-1.2 * R, 1.2 * R)
ax.set_aspect("equal")
ax.grid()

plot, = ax.plot(r[:, 0], r[:, 1])
punkt, = ax.plot([0], [0], 'o', color='blue')
#a_plot, = ax.plot([], [], 'o', color='red')

style=mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0,0), (0,0), color='red', arrowstyle=style)
arrow_a = mpl.patches.FancyArrowPatch((0,0), (0,0), color='black', arrowstyle=style)
ax.add_artist(arrow_v)
ax.add_artist(arrow_a)

def update(n):
    if n < v.shape[0]:
        arrow_v.set_positions(r[n], r[n] + v[n])
    if n < a.shape[0]:
        arrow_a.set_positions(r[n], r[n] + a[n])

    punkt.set_data(np.array(r[n]))

    return punkt, arrow_v, arrow_a #, plot

ani = mpl.animation.FuncAnimation(fig, update, interval=30, frames=t.size, blit=True)
plt.show()


