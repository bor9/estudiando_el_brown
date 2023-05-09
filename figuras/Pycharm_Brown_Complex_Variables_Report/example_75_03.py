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


# parámetros
m = 3
z0 = 1/m
z1 = 1/(m + 1)
z2 = 1/(m - 1)
r = 1/(m * (m+1))

# entorno reducido
N = 100
thetas = np.linspace(0, 2 * math.pi, N)
xc = z0 + r * np.cos(thetas)
yc = r * np.sin(thetas)

# valores maximos y minimos de los ejes
xmin = -0.1
xmax = 1.2 * z2
ymin = -2 * r
ymax = -ymin

# axis parameters
xmin_ax = xmin
xmax_ax = xmax
ymin_ax = ymin
ymax_ax = ymax

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.03
ytm = -0.015
# font size
fontsize = 14

fig = plt.figure(0, figsize=(5, 4), frameon=False)
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

# entorno reducido
plt.plot(xc, yc, 'k--', lw=1)
# epsilon
ne = 10
plt.plot([z0, xc[ne]], [0, yc[ne]], 'k', lw=1)
plt.text((z0 + xc[ne]) / 2, yc[ne] / 2, '$\epsilon$', fontsize=fontsize, ha='right', va='bottom')

# singularidades
ms = 5
plt.plot(z0, 0, 'o', markerfacecolor='w', markeredgecolor='k', ms=ms, zorder=10)
plt.plot(z1, 0, 'o', markerfacecolor='w', markeredgecolor='k', ms=ms, zorder=10)
plt.plot(z2, 0, 'o', markerfacecolor='w', markeredgecolor='k', ms=ms, zorder=10)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='center', va='baseline')

xtm = -0.045
plt.text(z0, xtm, r'$\frac{1}{m}$', fontsize=fontsize, ha='center', va='baseline')
plt.text(z1, xtm, r'$\frac{1}{m+1}$', fontsize=fontsize, ha='right', va='baseline')
plt.text(z2, xtm, r'$\frac{1}{m-1}$', fontsize=fontsize, ha='center', va='baseline')


plt.axis('off')

# save as pdf image
plt.savefig('example_75_03.pdf', bbox_inches='tight')

plt.show()
