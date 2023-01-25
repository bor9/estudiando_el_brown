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


# valores maximos y minimos de los ejes
xmin = -4.2
xmax = 0.5
ymin = -0.2
ymax = 3.4

# axis parameters
d = 0.5
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.5
ytm = -0.25
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 2.5), frameon=False)
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
plt.plot([-4, 0], [0, 0], color='k', lw=2)
plt.plot([0, 0], [0, 3], color='k', lw=2)
plt.plot([-4, 0], [0, 3], color='k', lw=2)
# puntos z = 0 y z = 2
ms = 9
plt.plot(0, 0, 'k.', ms=ms)
plt.plot(0, 3, 'k.', ms=ms)
plt.plot(-4, 0, 'k.', ms=ms)

# flechas
xa = -2
ya = (3/4) * xa + 3
plt.annotate("", xytext=(xa+0.04, ya+0.03), xycoords='data', xy=(xa, ya), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(xa-0.01, 0), xycoords='data', xy=(xa, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
ya = 1.5
plt.annotate("", xytext=(0, ya-0.01), xycoords='data', xy=(0, ya), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# etiquetas
plt.text(-ytm, xtm, '$0$', fontsize=fontsize, ha='left', va='baseline')
plt.text(-4, xtm, '$-4$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, 3, '$3i$', fontsize=fontsize, ha='left', va='center')
plt.text(-1.1, 1, '$C$', fontsize=fontsize, ha='center', va='center')


plt.axis('off')

# save as pdf image
plt.savefig('exercise_47_03.pdf', bbox_inches='tight')

plt.show()
