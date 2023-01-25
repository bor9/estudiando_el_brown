import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon

__author__ = 'ernesto'

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preview'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']


# auxiliar function for plot ticks of equal length in x and y axis despite its scales.
def convert_display_to_data_coordinates(transData, length=10):
    # create a transform which will take from display to data coordinates
    inv = transData.inverted()
    # transform from display coordinates to data coordinates in x axis
    data_coords = inv.transform([(0, 0), (length, 0)])
    # get the length of the segment in data units
    yticks_len = data_coords[1, 0] - data_coords[0, 0]
    # transform from display coordinates to data coordinates in y axis
    data_coords = inv.transform([(0, 0), (0, length)])
    # get the length of the segment in data units
    xticks_len = data_coords[1, 1] - data_coords[0, 1]
    return xticks_len, yticks_len


# z0
x0 = 3
y0 = 3
d = 2.5
N = 200
thetas = np.linspace(0, 2*math.pi, N)

# línea poligonal
xl1 = 8
yl1 = 4
xl2 = 10
yl2 = 8
xl3 = 20
yl3 = 5


# punto z_1
lam = 0.3
x1 = (1 - lam) * x0 + lam * xl1
y1 = (1 - lam) * y0 + lam * yl1
# punto z_2
lam = 0.7
x2 = (1 - lam) * x0 + lam * xl1
y2 = (1 - lam) * y0 + lam * yl1
# punto z_n
x4 = xl3
y4 = yl3
# punto z_{n-1}
lam = 0.18
x3 = (1 - lam) * xl3 + lam * xl2
y3 = (1 - lam) * yl3 + lam * yl2


# Entornos
xc0 = x0 + d * np.cos(thetas)
yc0 = y0 + d * np.sin(thetas)
xc1 = x1 + d * np.cos(thetas)
yc1 = y1 + d * np.sin(thetas)
xc2 = x2 + d * np.cos(thetas)
yc2 = y2 + d * np.sin(thetas)
xc4 = x4 + d * np.cos(thetas)
yc4 = y4 + d * np.sin(thetas)
xc3 = x3 + d * np.cos(thetas)
yc3 = y3 + d * np.sin(thetas)


# traslación de la curva
xt = 8.5
yt = 6

# valores maximos y minimos de los ejes
xmin = 0
xmax = 23
ymin = 0
ymax = 10

# axis parameters
dax = 1
xmin_ax = xmin - dax
xmax_ax = xmax + dax
ymin_ax = ymin - dax
ymax_ax = ymax + dax

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.8
ytm = -0.5
# font size
fontsize = 14

fig = plt.figure(0, figsize=(8, 4), frameon=False)
ax = fig.add_subplot(111)

plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)
plt.gca().set_aspect('equal', adjustable='box')

# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# linea poligonal
plt.plot([x0, xl1], [y0, yl1], 'k-', lw=1, zorder=10)
plt.plot([xl1, xl2], [yl1, yl2], 'k-', lw=1, zorder=10)
plt.plot([xl2, xl3], [yl2, yl3], 'k-', lw=1, zorder=10)

# centros
ms = 8
plt.plot(x0, y0, 'k.', ms=ms, zorder=10)
plt.text(x0, y0 - 0.2, '$z_0$', fontsize=fontsize, ha='center', va='top', zorder=10)
plt.plot(x1, y1, 'k.', ms=ms, zorder=10)
plt.text(x1, y1 - 0.2, '$z_1$', fontsize=fontsize, ha='center', va='top', zorder=10)
plt.plot(x2, y2, 'k.', ms=ms, zorder=10)
plt.text(x2, y2 - 0.2, '$z_2$', fontsize=fontsize, ha='center', va='top', zorder=10)
plt.plot(x4, y4, 'k.', ms=ms, zorder=10)
plt.text(x4, y4 - 0.2, '$z_n$', fontsize=fontsize, ha='center', va='top', zorder=10)
plt.text(x4 + 0.2, y4 + 0.1, '$P$', fontsize=fontsize, ha='left', va='bottom', zorder=10)
plt.plot(x3, y3, 'k.', ms=ms, zorder=10)
plt.text(x3 + 0.2, y3 - 0.2, '$z_{n-1}$', fontsize=fontsize, ha='center', va='top', zorder=10)


# entornos
plt.plot(xc0, yc0, 'k--', lw=1.5, zorder=8)
vert = np.vstack((xc0, yc0))
p0 = Polygon(vert.T, fc="white", alpha=1, zorder=7)
ax.add_artist(p0)
plt.plot(xc1, yc1, 'k--', lw=1.5, zorder=5)
vert = np.vstack((xc1, yc1))
p1 = Polygon(vert.T, fc="white", alpha=1, zorder=4)
ax.add_artist(p1)
plt.plot(xc2, yc2, 'k--', lw=1.5, zorder=3)
vert = np.vstack((xc2, yc2))
p2 = Polygon(vert.T, fc="white", alpha=1, zorder=2)
ax.add_artist(p2)
plt.plot(xc4, yc4, 'k--', lw=1.5, zorder=8)
vert = np.vstack((xc4, yc4))
p4 = Polygon(vert.T, fc="white", alpha=1, zorder=7)
ax.add_artist(p4)
plt.plot(xc3, yc3, 'k--', lw=1.5, zorder=5)
vert = np.vstack((xc3, yc3))
p3 = Polygon(vert.T, fc="white", alpha=1, zorder=4)
ax.add_artist(p3)

plt.text(x0 + 1, y0 + 1.5, '$N_0$', fontsize=fontsize, ha='center', va='center', zorder=10)
plt.text(x1 + 1, y1 + 1.5, '$N_1$', fontsize=fontsize, ha='center', va='center', zorder=10)
plt.text(x2 + 1, y2 + 1.5, '$N_2$', fontsize=fontsize, ha='center', va='center', zorder=10)
plt.text(x4 - 1, y4 + 1.5, '$N_n$', fontsize=fontsize, ha='center', va='center', zorder=10)
plt.text(x3 - 0.85, y3 + 1.5, '$N_{n-1}$', fontsize=fontsize, ha='center', va='center', zorder=10)

plt.text(12, 8, '$L$', fontsize=fontsize, ha='center', va='center', zorder=10)

plt.axis('off')

# save as pdf image
plt.savefig('maximum_modulus_principle_theorem.pdf', bbox_inches='tight')

plt.show()
