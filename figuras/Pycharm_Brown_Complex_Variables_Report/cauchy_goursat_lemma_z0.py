import matplotlib.pyplot as plt
import numpy as np
import math

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


# Círculo del entorno
# centro
x0 = 7
y0 = 6
# radio
r = 4
N = 100
thetas = np.linspace(0, 2*math.pi, N)

xc = x0 + r * np.cos(thetas)
yc = y0 + r * np.sin(thetas)


# valores maximos y minimos de los ejes
max_ax = 12
xmin = 0
xmax = max_ax
ymin = 0
ymax = max_ax

# axis parameters
d = 1
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.8
ytm = -0.5
# font size
fontsize = 14

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

# entorno
plt.plot(xc, yc, 'k--', lw=1)
# punto z0
ms = 9
plt.plot(x0, y0, 'k.', ms=ms)
plt.text(x0, y0+0.3, r'$z_0$', fontsize=fontsize, ha='center', va='bottom')
# cuadrado
# vertice inferior izquierdo
xv = x0 - 0.8
yv = y0 - 0.4
# lado
l = 3
plt.plot([xv, xv+l], [yv, yv], 'k', lw=1)
plt.plot([xv, xv+l], [yv+l, yv+l], 'k', lw=1)
plt.plot([xv, xv], [yv, yv+l], 'k', lw=1)
plt.plot([xv+l, xv+l], [yv, yv+l], 'k', lw=1)
plt.text(xv, yv+l+0.2, r'$\sigma_K$', fontsize=fontsize, ha='left', va='bottom')
# radio
ang = -np.pi / 4
plt.plot([x0, x0 + r * np.cos(ang)], [y0, y0 + r * np.sin(ang)], 'k', lw=1)
plt.text(x0 + r * np.cos(ang) / 2 - 0.15, y0 + r * np.sin(ang) / 2 - 0.15, r'$\delta$', fontsize=fontsize, ha='right',
         va='top')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_goursat_lemma_z0.pdf', bbox_inches='tight')

plt.show()
