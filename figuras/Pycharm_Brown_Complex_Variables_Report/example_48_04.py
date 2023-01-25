import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import interpolate

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
r = 3

# radio variable
rx = [0, 0.1, 0.2, 0.3, 0.6, 0.75, 1, 1.1, 1.2, 1.3, 1.6, 1.95, 2]
ry = [3, 2.9, 2.5, 2.0, 1.8, 3.3, 3, 2.9, 3.2, 3.5, 2.8, 3, 3]

N = 100
f = interpolate.interp1d(rx, ry, kind='cubic')
rxnew = np.linspace(0, 2, N, endpoint=True)
rynew = f(rxnew)

thetas = np.linspace(0, 2*math.pi, N)
xc = rynew * np.cos(thetas)
yc = rynew * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 4
xmin = -max_ax
xmax = max_ax
ymin = -max_ax
ymax = max_ax

# axis parameters
d = 0.5
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.7
ytm = -0.4
# font size
fontsize = 14

fig = plt.figure(0)
ax = fig.add_subplot(111)
plt.plot(rx, ry, 'k.', ms=8)
plt.plot(rxnew, rynew, 'k-')

fig = plt.figure(1, figsize=(3, 3), frameon=False)
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

# contorno
plt.plot(xc, yc, color='k', lw=2)
# puntos z = 3 y z = -3
ms = 9
plt.plot(3, 0, 'k.', ms=ms)
plt.plot(-3, 0, 'k.', ms=ms)
# corte de rama
ms = 6
plt.plot(0, 0, 'o', markerfacecolor='w', markeredgecolor='r', ms=ms, zorder=10)
plt.plot([0, xmax], [0, 0], 'r', ms=ms, zorder=9)

# flechas
theta = 3 * math.pi / 4
idx = (np.abs(thetas - theta)).argmin()
plt.annotate("", xytext=(xc[idx+1], yc[idx+1]), xycoords='data', xy=(xc[idx-1], yc[idx-1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xc[idx], yc[idx]+0.4, r'$C_1$', fontsize=fontsize, ha='right', va='bottom')

theta = 7 * math.pi / 4
idx = (np.abs(thetas - theta)).argmin()
plt.annotate("", xytext=(xc[idx], yc[idx]), xycoords='data', xy=(xc[idx+1], yc[idx+1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xc[idx], yc[idx]-0.4, r'$C_2$', fontsize=fontsize, ha='left', va='top')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
dx = 0.2
plt.text(r+dx, xtm, '${0:d}$'.format(r), fontsize=fontsize, ha='left', va='baseline')
plt.text(-r-dx, xtm, '$-{0:d}$'.format(r), fontsize=fontsize, ha='right', va='baseline')
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('example_48_04.pdf', bbox_inches='tight')

plt.show()
