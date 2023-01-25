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
# z0 = x0 + iy0
x0 = 2
y0 = 1
R = 3
R0 = 0.7
R1 = 3
r = 1

# circulo |z|=1
N = 200
thetas = np.linspace(0, 2 * math.pi, N)
xc0 = x0 + R0 * np.cos(thetas)
yc0 = y0 + R0 * np.sin(thetas)

xc1 = x0 + R1 * np.cos(thetas)
yc1 = y0 + R1 * np.sin(thetas)

# valores maximos y minimos de los ejes
xmin = x0 - R
xmax = x0 + R
ymin = y0 - R
ymax = y0 + R

dx = 0.5
# axis parameters
xmin_ax = xmin - dx
xmax_ax = xmax + dx
ymin_ax = ymin - dx
ymax_ax = ymax + dx

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.45
ytm = -0.2
# font size
fontsize = 14

fig = plt.figure(0, figsize=(9, 4), frameon=False)
############
# C chico  #
############
ax = plt.subplot2grid((4, 8), (0, 0), rowspan=4, colspan=4)
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

# contorno C1
plt.plot(xc0, yc0, color='k', lw=2, zorder=3)
# flecha y etiqueta
i = 100
plt.annotate("", xytext=(xc0[i-10], yc0[i-10]), xycoords='data', xy=(xc0[i], yc0[i]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xc0[i]-0.15, yc0[i]+0.15, r'$C_0$', fontsize=fontsize, ha='right', va='center')

# contorno C
plt.plot([0, 3], [0, 0], 'k-', lw=2, zorder=3)
plt.plot([0, 3], [2, 2], 'k-', lw=2, zorder=3)
plt.plot([0, 0], [0, 2], 'k-', lw=2, zorder=3)
plt.plot([3, 3], [0, 2], 'k-', lw=2, zorder=3)
# flechas
da = 0.2
dd = 0.01
a = 1.5+da
plt.annotate("", xytext=(3, a-dd), xycoords='data', xy=(3, a), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
a = 0.5-da
plt.annotate("", xytext=(0, a+dd), xycoords='data', xy=(0, a), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
a = 1.5+da
plt.annotate("", xytext=(a-dd, 0), xycoords='data', xy=(a, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
a = 1.5-da
plt.annotate("", xytext=(a+dd, 2), xycoords='data', xy=(a, 2), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(3+0.05, 2+0.05, r'$C$', fontsize=fontsize, ha='left', va='bottom')


# puntos z = x0+iy0
ms = 9
plt.plot(x0, y0, 'k.', ms=ms, zorder=5)
plt.text(x0+0.05, y0+0.05, '$z_0$', fontsize=fontsize, ha='left', va='bottom')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# etiquetas
plt.text(3, xtm, '$3$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(ytm, 2, '$2$', fontsize=fontsize, ha='right', va='center')

# ticks
plt.plot([2, 2], [0, xtl], 'k', lw=1, zorder=3)
plt.text(2, xtm, '$2$', fontsize=fontsize, ha='center', va='baseline')
plt.plot([0, ytl], [1, 1], 'k', lw=1, zorder=3)
plt.text(ytm, 1, '$1$', fontsize=fontsize, ha='right', va='center')

# relleno de la región
vert = np.vstack(([3, 3, 0, 0], [0, 2, 2, 0]))
p2 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=1)
ax.add_artist(p2)
vert = np.vstack((xc0, yc0))
p1 = Polygon(vert.T, fc="white", alpha=1, zorder=2)
ax.add_artist(p1)

# radio
i = 155
plt.plot([x0, xc0[i]], [y0, yc0[i]], 'k', lw=1, zorder=5)
plt.text((x0+xc0[i])/2+0.22, (y0+yc0[i])/2-0.18, '$R$', fontsize=fontsize, ha='center', va='bottom')

plt.axis('off')

############
# C grande #
############
ax = plt.subplot2grid((4, 8), (0, 4), rowspan=4, colspan=4)

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

# contorno C1
plt.plot(xc1, yc1, color='k', lw=2)
# flecha y etiqueta
i = 25
plt.annotate("", xytext=(xc1[i], yc1[i]), xycoords='data', xy=(xc1[i+2], yc1[i+2]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xc1[i]+0.1, yc1[i]+0.1, r'$C_0$', fontsize=fontsize, ha='left', va='bottom')

# contorno C
plt.plot([0, 3], [0, 0], 'k-', lw=2, zorder=3)
plt.plot([0, 3], [2, 2], 'k-', lw=2, zorder=3)
plt.plot([0, 0], [0, 2], 'k-', lw=2, zorder=3)
plt.plot([3, 3], [0, 2], 'k-', lw=2, zorder=3)
# flechas
da = 0.2
dd = 0.01
a = 1.5+da
plt.annotate("", xytext=(3, a-dd), xycoords='data', xy=(3, a), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
a = 0.5-da
plt.annotate("", xytext=(0, a+dd), xycoords='data', xy=(0, a), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
a = 1.5+da
plt.annotate("", xytext=(a-dd, 0), xycoords='data', xy=(a, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
a = 1.5-da
plt.annotate("", xytext=(a+dd, 2), xycoords='data', xy=(a, 2), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(3+0.05, 2+0.05, r'$C$', fontsize=fontsize, ha='left', va='bottom')


# puntos z = x0+iy0
ms = 9
plt.plot(x0, y0, 'k.', ms=ms, zorder=5)
plt.text(x0+0.05, y0+0.05, '$z_0$', fontsize=fontsize, ha='left', va='bottom')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# etiquetas
plt.text(3, xtm, '$3$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(ytm, 2, '$2$', fontsize=fontsize, ha='right', va='center')

# ticks
plt.plot([2, 2], [0, xtl], 'k', lw=1, zorder=3)
plt.text(2, xtm, '$2$', fontsize=fontsize, ha='center', va='baseline')
plt.plot([0, ytl], [1, 1], 'k', lw=1, zorder=3)
plt.text(ytm, 1, '$1$', fontsize=fontsize, ha='right', va='center')

# relleno de la región
vert = np.vstack((xc1, yc1))
p1 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=1)
ax.add_artist(p1)
vert = np.vstack(([3, 3, 0, 0], [0, 2, 2, 0]))
p2 = Polygon(vert.T, fc="white", alpha=1, zorder=2)
ax.add_artist(p2)

# radio
i = 191
plt.plot([x0, xc1[i]], [y0, yc1[i]], 'k', lw=1, zorder=5)
plt.text((x0+xc1[i])/2+0.2, (y0+yc1[i])/2, '$R$', fontsize=fontsize, ha='center', va='bottom')

plt.axis('off')


# save as pdf image
plt.savefig('exercise_53_03.pdf', bbox_inches='tight')

plt.show()
