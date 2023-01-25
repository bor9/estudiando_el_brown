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
r = 1

# circulo |z|=1
N = 200
thetas = np.linspace(0, 2 * math.pi, N)
xc = r * np.cos(thetas)
yc = r * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 1.5
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
xtm = -0.25
ytm = -0.15
# font size
fontsize = 14

fig = plt.figure(0, figsize=(3, 3), frameon=False)
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
plt.plot(xc, yc, color='k', lw=2)
# puntos z = 1 y z = -1
ms = 9
plt.plot(1, 0, 'k.', ms=ms)
plt.plot(-1, 0, 'k.', ms=ms)

# flechas
theta = math.pi / 4
xa = r * math.cos(theta)
ya = r * math.sin(theta)
r2 = 0.01
plt.annotate("", xytext=(xa, ya), xycoords='data', xy=(xa-r2*math.sin(theta), ya+r2*math.cos(theta)), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
theta = -math.pi / 4
xa = r * math.cos(theta)
ya = r * math.sin(theta)
plt.annotate("", xytext=(xa, ya), xycoords='data', xy=(xa+r2*math.sin(theta), ya-r2*math.cos(theta)), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

# etiquetas de los contornos
theta = math.pi / 4 * 0.9
r3 = 1.1
xl = r3 * math.cos(theta)
yl = r3 * math.sin(theta)
plt.text(xl, yl, r'$C_1$', fontsize=fontsize, ha='left', va='bottom')
plt.text(xl, -yl, r'$C_2$', fontsize=fontsize, ha='left', va='top')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')


# circle labels
plt.text(r + 0.07, xtm, '${0:d}$'.format(r), fontsize=fontsize, ha='left', va='baseline')
plt.text(-1 - 0.07, xtm, '$-1$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('example_45_01.pdf', bbox_inches='tight')

plt.show()
