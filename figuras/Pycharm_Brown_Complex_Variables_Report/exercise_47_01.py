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
N = 200
thetas = np.linspace(0, math.pi / 2, N)
xc = r * np.cos(thetas)
yc = r * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 2
xmin = 0
xmax = max_ax
ymin = 0
ymax = max_ax


# axis parameters
da = 0.5
xmin_ax = xmin - da
xmax_ax = xmax + da
ymin_ax = ymin - da
ymax_ax = ymax + da

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.4
ytm = -0.2
# font size
fontsize = 14

fig = plt.figure(0, figsize=(2, 3), frameon=False)
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
plt.plot(0, r, 'k.', ms=ms)
plt.plot(r, 0, 'k.', ms=ms)

# flechas
theta = math.pi / 4
xa = r * math.cos(theta)
ya = r * math.sin(theta)
r2 = 0.01
plt.annotate("", xytext=(xa, ya), xycoords='data', xy=(xa-r2*math.sin(theta), ya+r2*math.cos(theta)), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

# etiquetas de los contornos
theta = math.pi / 4 * 0.9
r3 = r + 0.15
xl = r3 * math.cos(theta)
yl = r3 * math.sin(theta)
plt.text(xl, yl, r'$C$', fontsize=fontsize, ha='left', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, r'$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(ytm, r, '${:d}i$'.format(r), fontsize=fontsize, ha='right', va='center')
plt.text(r, xtm, '${:d}$'.format(r), fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_47_01.pdf', bbox_inches='tight')

plt.show()
