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
r = 2

# circulo |z|=1
N = 100
thetas = np.linspace(0, math.pi / 4, N)
xc = r * np.cos(thetas)
yc = r * np.sin(thetas)

# valores maximos y minimos de los ejes
xmin = 0
xmax = 2.5
ymin = 0
ymax = 1.5


# axis parameters
da = 0.5
xmin_ax = xmin - da
xmax_ax = xmax + da
ymin_ax = ymin - da
ymax_ax = ymax + da

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.25
ytm = -0.14
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 3), frameon=False)
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

# arco |z|=R
plt.plot(xc, yc, color='k', lw=2)
# puntos z = 1 y z = -1
ms = 9
plt.plot(xc[-1], yc[-1], 'k.', ms=ms)
plt.plot(r, 0, 'k.', ms=ms)
# flechas
idx = int(N/2)
di = 4
plt.annotate("", xytext=(xc[idx], yc[idx]), xycoords='data', xy=(xc[idx+di], yc[idx+di]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
# etiquetas de los contornos
plt.text(xc[idx] + 0.1, yc[idx], r'$C_R$', fontsize=fontsize, ha='left', va='center')

plt.plot([0, r], [0, 0], 'k', lw=2)
dr = 0.1
plt.annotate("", xytext=(r / 2, 0), xycoords='data', xy=(r / 2 + dr, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(r / 2, xtm, r'$C_1$', fontsize=fontsize, ha='center', va='baseline')

plt.plot([0, xc[-1]], [0, yc[-1]], 'k', lw=2)

ca = r / (2 * np.sqrt(2))
dr = 0.1
plt.annotate("", xytext=(ca + dr, ca + dr), xycoords='data', xy=(ca, ca), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(ca + 0.05, ca + 0.15, r'$C_2$', fontsize=fontsize, ha='right', va='bottom')

plt.text(xc[-1] - 0.05, yc[-1] + 0.05, r'$Re^{i\pi/4}$', fontsize=fontsize, ha='left', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, r'$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(r, xtm, '$R$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_88_12.pdf', bbox_inches='tight')

plt.show()
