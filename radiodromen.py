import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

r0_h = np.array([0.0, 10.0])
r0_m = np.array([0.0, 0.0])
v0_h = 3.0
v0_m = np.array([2.0, 0.0])

t_max = 500
dt = 0.01

epsilon = v0_h * dt

t = [0]
r_h = [r0_h]
r_m = [r0_m]
v_h = []

while True:
    dr = r_m[-1] - r_h[-1]
    v = v0_h * dr / np.linalg.norm(dr)
    v_h.append(v)

    if (np.linalg.norm(dr) < epsilon) or t[-1] > t_max:
        break

    r_h.append(r_h[-1] + dt * v)
    r_m.append(r_m[-1] + dt * v0_m)
    t.append(t[-1] + dt)

print(r_h)
print(v_h)

# convert lists to np arrays
t = np.array(t)
r_h = np.array(r_h)
v_h = np.array(v_h)
r_m = np.array(r_m)
a_h = (v_h[1:, :] - v_h[:-1,:]) / dt

# Create figure
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-0.2, 15)
ax.set_ylim(-0.2, 10)
ax.set_aspect('equal')
ax.grid()

plot,   = ax.plot([], [])
hund,   = ax.plot([], [], 'o', color='blue')
mensch, = ax.plot([], [], 'o', color='red')

style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0,0), (0,0), color='red', arrowstyle=style)
arrow_a = mpl.patches.FancyArrowPatch((0,0), (0,0), color='black', arrowstyle=style)
ax.add_artist(arrow_v)
ax.add_artist(arrow_a)

def update(n):
    arrow_v.set_positions(r_h[n], r_h[n] + v_h[n])
    if n < a_h.shape[0]:
        arrow_a.set_positions(r_h[n], r_h[n] + a_h[n])

    hund.set_data(r_h[n])
    mensch.set_data(r_m[n])

    plot.set_data(r_h[:n+1, 0], r_h[:n+1,1])

    return hund, mensch, arrow_v, arrow_a, plot

ani = mpl.animation.FuncAnimation(fig, update, interval=30, frames=t.size, blit=True)
plt.show()