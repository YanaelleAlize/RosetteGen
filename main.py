import numpy as np
import matplotlib.pyplot as plt

# Les variables importantes pour la définition :
# N : le nb de points utilisés pour créer un cercle
N = 1000000
# _DPI : le nombre de pixels utilisés pour enregistrer les images
DPI = 500
# r : rayon d'un cercle de base
r = 100

theta = np.linspace(0, 2*np.pi, N)
x0, y0 = 0, 0
x_0, y_0 = np.array([x0]*N) , np.array([y0]*N)

print(len(x_0))

x1 = np.add(x_0, r*np.cos(theta))
x2 = np.add(y_0, r*np.sin(theta))

fig, ax = plt.subplots(1)

ax.plot(x1, x2, color="black")
ax.set_aspect(1)

x_min, y_min, x_max, y_max = min(x1), max(x1), min(x2), max(x2)

print("x_min : {}, y_min : {}, x_max : {}, y_max : {}".format(x_min, y_min, x_max, y_max))

#plt.xlim(1.25 * x_min, 1.25 * x_max)
#plt.ylim(1.25 * y_min, 1.25 * y_max)

#plt.grid(linestyle='--')

plt.title('Rosette generated', fontsize=8)

while 1 :
    nameTMP = input("How do you want to name that image ?\n\t")
    name = nameTMP
    name = name.strip().split(".")
    if len(name) == 1 :
        filename = name[0] + ".png"
    elif name[-1].lower() == "png" :
        filename = nameTMP.strip()
    else :
        filename = "".join((x + "." for x in name[:-1])) + "png"
    break

plt.savefig(filename, bbox_inches='tight', dpi=DPI)

plt.show()