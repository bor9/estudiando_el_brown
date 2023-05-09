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
r1 = 2
r2 = 4

# circulo |z|=1
N = 200
thetas = np.linspace(0, 2 * math.pi, N)
xc1 = 2 + r1 * np.cos(thetas)
yc1 = r1 * np.sin(thetas)
xc2 = r2 * np.cos(thetas)
yc2 = r2 * np.sin(thetas)


# valores maximos y minimos de los ejes
max_ax = 5
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
xtm = -0.5
ytm = -0.25
# font size
fontsize = 12

fig = plt.figure(0, figsize=(5, 5), frameon=False)
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

# contornos
plt.plot(xc1, yc1, color='k', lw=2)
plt.plot(xc2, yc2, color='k', lw=2)
# puntos z = 1 y z = -1
ms = 9
plt.plot(1, 0, 'k.', ms=ms, zorder=10)
plt.plot(0, 3, 'k.', ms=ms)
plt.plot(0, -3, 'k.', ms=ms)

# flechas
i = 55
plt.annotate("", xytext=(xc1[i - 5], yc1[i - 5]), xycoords='data', xy=(xc1[i], yc1[i]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xc1[i] - 0.1, yc1[i] + 0.2, r'$C:|z-2|=2$', fontsize=fontsize, ha='center', va='bottom')
i = 35
plt.annotate("", xytext=(xc2[i], yc2[i]), xycoords='data', xy=(xc2[i + 2], yc2[i + 2]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xc2[i] + 0.1, yc2[i] + 0.1, r'$C:|z|=4$', fontsize=fontsize, ha='left', va='bottom')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.text(ytm, 3, '$3i$', fontsize=fontsize, ha='right', va='center')
plt.text(ytm, -3, '$-3i$', fontsize=fontsize, ha='right', va='center')
plt.text(r2 + 0.2, xtm, '$4$', fontsize=fontsize, ha='left', va='baseline')
plt.text(1, xtm, '$1$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

#ticks
plt.plot([2, 2], [0, xtl], 'k', lw=1)
plt.text(2, xtm, '$2$', fontsize=fontsize, ha='center', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_81_04.pdf', bbox_inches='tight')

plt.show()
