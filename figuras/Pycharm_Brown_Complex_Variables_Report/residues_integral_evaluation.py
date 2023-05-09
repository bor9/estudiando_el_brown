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
xz0 = 5
yz0 = 6
R2 = 5.5

# para el contorno C
rx = [0, 0.1, 0.2, 0.3, 0.6, 0.75, 1, 1.1, 1.2, 1.3, 1.6, 1.95, 2]
ry = np.array([3, 2.8, 2.2, 1.5, 2.4, 3.3, 3, 2.9, 3.2, 3.5, 2.6, 3, 3])

N = 100
f = interpolate.interp1d(rx, ry, kind='cubic')
rxnew = np.linspace(0, 2, N, endpoint=True)
rynew = f(rxnew)

thetas = np.linspace(0, 2*math.pi, N)
# contorno C
xc = xz0 + rynew * np.cos(thetas)
yc = yz0 + rynew * np.sin(thetas)

# region
xR2 = xz0 + R2 * np.cos(thetas)
yR2 = yz0 + R2 * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 7
xmin = -2
xmax = xmin + 2 * max_ax
ymin = xmin
ymax = xmax

# axis parameters
d = 0.5
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.76
ytm = -0.4
# font size
fontsize = 12

fig = plt.figure(1, figsize=(4, 4), frameon=False)
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

# dominio
plt.plot(xR2, yR2, 'k--', lw=1)
# contorno
plt.plot(xc, yc, color='k', lw=1.5)

# puntos R1 y R2
ms = 7
plt.plot(xz0, yz0, 'k.', ms=ms)

# flechas
theta = 7 * math.pi / 4
# C
idx = (np.abs(thetas - theta)).argmin()
plt.annotate("", xytext=(xc[idx], yc[idx]), xycoords='data', xy=(xc[idx+1], yc[idx+1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=9, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xc[idx], yc[idx]-0.2, '$C$', fontsize=fontsize, ha='left', va='top')

idx = 18
plt.plot([xz0, xR2[idx]], [yz0, yR2[idx]], 'k', lw=1)
plt.text((xR2[idx] + xz0) / 2 + 0.65, (yR2[idx] + yz0) / 2, '$R_2$', fontsize=fontsize, ha='center', va='center')

# etiquetas
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.text(xz0, yz0-0.2, '$z_0$', fontsize=fontsize, ha='center', va='top')

plt.axis('off')

# save as pdf image
plt.savefig('residues_integral_evaluation.pdf', bbox_inches='tight')

plt.show()
