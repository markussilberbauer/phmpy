import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

# R distance from the sun, T duration of orbit around the sun
Planets = {
    "merkur": {"R":  57.9, "T":  88, "color": "black"},
    "venus":  {"R": 108.2, "T": 225, "color": "orange"},
    "erde":   {"R": 149.6, "T": 365, "color": "blue"},
    "mars":   {"R": 227.9, "T": 687, "color": "red"},
    "jupiter": {"R": 778.51, "T": 4330, "color": "brown"},
    "saturn": {"R": 1433.4, "T": 10751, "color": "brown"},
    "uranus": {"R": 2872.4, "T": 30664, "color": "brown"},
    "neptun": {"R": 4495.0, "T": 60148, "color": "brown"}
}

P = {}
dt = 0.2

# calculate rotation values for each planet
for planet in Planets.keys():
    t = np.arange(0, Planets[planet]["T"], dt)
    Planets[planet]["tsize"] = t.size
    print(f"{planet} {t.size}")
    P[planet] = np.empty((t.size, 2))
    omega = 2 * np.pi / Planets[planet]["T"]
    P[planet][:, 0] = Planets[planet]["R"] * np.cos(omega * t)
    P[planet][:, 1] = Planets[planet]["R"] * np.sin(omega * t)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(-1.2 * Planets["jupiter"]["R"], 1.2 * Planets["jupiter"]["R"])
ax.set_ylim(-1.2 * Planets["jupiter"]["R"], 1.2 * Planets["jupiter"]["R"])
ax.set_aspect("equal")

for planet in Planets.keys():
    ax.plot(P[planet][:, 0], P[planet][:, 1], color="grey")

planet_merkur, = ax.plot([0], [0], 'o', color=Planets["merkur"]["color"])
planet_venus,  = ax.plot([0], [0], 'o', color=Planets["venus"]["color"])
planet_erde,   = ax.plot([0], [0], 'o', color=Planets["erde"]["color"])
planet_mars,   = ax.plot([0], [0], 'o', color=Planets["mars"]["color"])
planet_jupiter,   = ax.plot([0], [0], 'o', color=Planets["jupiter"]["color"])

def update(n):
    planet_merkur.set_data(np.array(P["merkur"][n % 440]))
    planet_venus.set_data(np.array(P["venus"][n % 1125]))
    planet_erde.set_data(np.array(P["erde"][n % 1825]))
    planet_mars.set_data(np.array(P["mars"][n % 3435]))
    planet_jupiter.set_data(np.array(P["jupiter"][n % 21650]))

    return planet_merkur, planet_venus, planet_erde, planet_mars, planet_jupiter #planet_venus, planet_erde, planet_mars


ani = mpl.animation.FuncAnimation(fig, update, interval=1, frames=88*225*365*687*4330, blit=True)
plt.show()
