import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

r_merkur = 57.9
r_venus = 108.2
r_erde = 149.6
r_mars = 227.9

R = {
    "merkur":57.9,
    "venus": 108.2,
    "erde": 149.6,
    "mars": 227.9
}

T = {
    "merkur": 88,
    "venus": 225,
    "erde": 365,
    "mars": 687
}

dt = 0.2
# omega = 2 * np.pi / T

t = np.arange(0, T["merkur"], dt)
merkur = np.empty((t.size,2))
omega = 2 * np.pi / T["merkur"]
merkur[:, 0] = R["merkur"] * np.cos(omega * t)
merkur[:, 1] = R["merkur"] * np.sin(omega * t)


t = np.arange(0, T["venus"], dt)
venus = np.empty((t.size,2))
omega = 2 * np.pi / T["venus"]
venus[:, 0] = R["venus"] * np.cos(omega * t)
venus[:, 1] = R["venus"] * np.sin(omega * t)

t = np.arange(0, T["erde"], dt)
erde = np.empty((t.size,2))
omega = 2 * np.pi / T["erde"]
erde[:, 0] = R["erde"] * np.cos(omega * t)
erde[:, 1] = R["erde"] * np.sin(omega * t)

t = np.arange(0, T["mars"], dt)
mars = np.empty((t.size,2))
omega = 2 * np.pi / T["mars"]
mars[:, 0] = R["mars"] * np.cos(omega * t)
mars[:, 1] = R["mars"] * np.sin(omega * t)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(-1.2 * R["mars"], 1.2 * R["mars"])
ax.set_ylim(-1.2 * R["mars"], 1.2 * R["mars"])
ax.set_aspect("equal")

plot_merkur, = ax.plot(merkur[:, 0], merkur[:, 1], color="black")
planet_merkur, = ax.plot([0], [0], 'o', color='black')
plot_venus, = ax.plot(venus[:, 0], venus[:, 1], color="orange")
planet_venus, = ax.plot([0], [0], 'o', color='orange')
plot_erde, = ax.plot(erde[:, 0], erde[:, 1], color='blue')
planet_erde, = ax.plot([0], [0], 'o', color='blue')
plot_mars, = ax.plot(mars[:, 0], mars[:, 1], color="red")
planet_mars, = ax.plot([0], [0], 'o', color='red')

#plot_venus, = ax.plot(venus[:, 0], venus[:, 1])
def update(n):
    #if n < merkur.shape[0]:

    #print(f"n={n} merkur.size={merkur.size} venus.size={venus.size} erde.size={erde.size} mars.size={mars.size}")
    planet_merkur.set_data(np.array(merkur[n % 440]))
    planet_venus.set_data(np.array(venus[n % 1125]))
    planet_erde.set_data(np.array(erde[n % 1825]))
    planet_mars.set_data(np.array(mars[n % 3435]))

    #return planet_merkur, plot_merkur, planet_venus, plot_venus
    #return planet_venus, plot_venus
    return planet_merkur, planet_venus, planet_erde, planet_mars, plot_merkur, plot_venus, plot_erde, plot_mars

ani = mpl.animation.FuncAnimation(fig, update, interval=1, frames=88*225*365*687, blit=True)
plt.show()
