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
xz0 = 6
yz0 = 5
R2 = 5.5

# para el contorno C
rx = [0, 0.1, 0.2, 0.3, 0.6, 0.75, 1, 1.1, 1.2, 1.3, 1.6, 1.95, 2]
ry = 0.9 * np.array([3, 2.8, 2.5, 2.2, 2.4, 3.3, 3, 2.9, 3.2, 3.5, 2.6, 3, 3])

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
plt.plot(xc, yc, 'k--', lw=1)

# puntos R1 y R2
ms = 7
plt.plot(xz0, yz0, 'k.', ms=ms)

# segmento
alpha = np.pi / 7
L = 3.7
plt.plot([xz0 - L * np.cos(alpha), xz0 + L * np.cos(alpha)], [yz0 - L * np.sin(alpha), yz0 + L * np.sin(alpha)],
         'k', lw=1)
plt.text(xz0 + L * np.cos(alpha) + 0.3,  yz0 + L * np.sin(alpha), '$L$', fontsize=fontsize, ha='left', va='center')

# etiquetas dominios
idx = 37
plt.text(xc[idx]+0.3, yc[idx]-0.3, '$D$', fontsize=fontsize, ha='center', va='top')
idx = 24
plt.text(xR2[idx], yR2[idx]-0.4, '$N_0$', fontsize=fontsize, ha='center', va='top')

# etiquetas
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.text(xz0, yz0-0.2, '$z_0$', fontsize=fontsize, ha='center', va='top')

plt.axis('off')

# save as pdf image
plt.savefig('zeros_theorem_3.pdf', bbox_inches='tight')

plt.show()
