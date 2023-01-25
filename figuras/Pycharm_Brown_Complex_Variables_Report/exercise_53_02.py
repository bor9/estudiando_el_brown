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


# parámetros
r = 4

# circulo |z|=1
N = 200
thetas = np.linspace(0, 2 * math.pi, N)
xc = r * np.cos(thetas)
yc = r * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 6
xmin = -max_ax
xmax = max_ax
ymin = -max_ax
ymax = max_ax


# axis parameters
xmin_ax = xmin
xmax_ax = xmax
ymin_ax = ymin
ymax_ax = ymax

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.6
ytm = -0.35
# font size
fontsize = 12

fig = plt.figure(0, figsize=(4, 4), frameon=False)
ax = fig.add_subplot(111)

plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)
plt.gca().set_aspect('equal', adjustable='box')

# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))

# circulo |z|=2
plt.plot(xc, yc, color='k', lw=2, zorder=10)
# puntos z = 1 y z = -1
ms = 9
plt.plot(1, 0, 'k.', ms=ms, zorder=10)
plt.plot(r, 0, 'k.', ms=ms)

# flechas
i = 25
plt.annotate("", xytext=(xc[i], yc[i]), xycoords='data', xy=(xc[i+2], yc[i+2]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=6, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xc[i]+0.1, yc[i]+0.1, r'$C_2$', fontsize=fontsize, ha='left', va='bottom')
i = 125
plt.annotate("", xytext=(xc[i], yc[i]), xycoords='data', xy=(xc[i+2], yc[i+2]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=6, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)

# contorno cuadrado
plt.plot([1, 1], [-1, 1], 'k-', lw=2, zorder=10)
plt.plot([-1, -1], [-1, 1], 'k-', lw=2, zorder=10)
plt.plot([-1, 1], [1, 1], 'k-', lw=2, zorder=10)
plt.plot([-1, 1], [-1, -1], 'k-', lw=2, zorder=10)
da = 0.1
plt.annotate("", xytext=(1, 0.7-da), xycoords='data', xy=(1, 0.7), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=6, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.annotate("", xytext=(-1, -0.7+da), xycoords='data', xy=(-1, -0.7), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=6, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.annotate("", xytext=(-0.7+da, 1), xycoords='data', xy=(-0.7, 1), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=6, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.annotate("", xytext=(0.7-da, -1), xycoords='data', xy=(0.7, -1), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=6, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)

plt.text(1+0.1, 1+0.1, r'$C_1$', fontsize=fontsize, ha='left', va='bottom')

vert = np.vstack((xc, yc))
p1 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=1)
ax.add_artist(p1)
vert = np.vstack(([1, -1, -1, 1], [1, 1, -1, -1]))
p2 = Polygon(vert.T, fc="white", alpha=1, zorder=2)
ax.add_artist(p2)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(r + 0.2, xtm, '$4$', fontsize=fontsize, ha='left', va='baseline')
plt.text(1 + 0.2, xtm, '$1$', fontsize=fontsize, ha='left', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_53_02.pdf', bbox_inches='tight')

plt.show()
