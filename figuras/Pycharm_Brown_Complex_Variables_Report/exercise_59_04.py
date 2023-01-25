import matplotlib.pyplot as plt
import math
import numpy as np

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
xmin = 0
xmax = 3.5
ymin = 0
ymax = 1.3


# axis parameters
d = 0.3
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.25
ytm = -0.15
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 2), frameon=False)
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

# camino rectangular
plt.plot([0, math.pi], [0, 0], color='k', lw=2)
plt.plot([0, math.pi], [1, 1], color='k', lw=2)
plt.plot([math.pi, math.pi], [0, 1], color='k', lw=2)
plt.plot([0, 0], [0, 1], color='k', lw=2)


# vértices
ms = 9
plt.plot(math.pi/2, 1, 'k.', ms=ms)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
plt.text(-0.1, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(-0.1, 1, '$1$', fontsize=fontsize, ha='right', va='center')

plt.text(math.pi, xtm, '$\pi$', fontsize=fontsize, ha='center', va='baseline')
plt.text(math.pi/2, 1-0.1, '$(\pi/2,\,1)$', fontsize=fontsize, ha='center', va='top')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_59_04_R.pdf', bbox_inches='tight')

#
# GRAPHS
#
N = 100
x = np.linspace(0, math.pi, N)
f1 = np.sin(x)
y = np.linspace(0, 1, N)
f2 = np.sinh(y)

fig = plt.figure(1, figsize=(7, 3), frameon=False)
ax = plt.subplot2grid((4, 6), (0, 0), rowspan=4, colspan=4)

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

plt.plot(x, f1, 'k-', lw=1.5)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$\operatorname{sen} x$', fontsize=fontsize, ha='left', va='center')
plt.text(-0.1, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(-0.1, 1, '$1$', fontsize=fontsize, ha='right', va='center')
plt.text(math.pi, xtm, '$\pi$', fontsize=fontsize, ha='center', va='baseline')
plt.text(math.pi/2, xtm, '$\pi/2$', fontsize=fontsize, ha='center', va='baseline')

plt.plot([math.pi/2, math.pi/2], [0, 1], 'k--', lw=1)
plt.plot([0, math.pi/2], [1, 1], 'k--', lw=1)

plt.plot([math.pi, math.pi], [0, xtl], 'k-', lw=1)

plt.axis('off')


xmax_ax = 1.65
ax = plt.subplot2grid((4, 6), (0, 4), rowspan=4, colspan=2)

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

plt.plot(y, f2, 'k-', lw=1.5)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$y$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$\operatorname{senh} y$', fontsize=fontsize, ha='left', va='center')
plt.text(-0.1, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(-0.1, 1, '$1$', fontsize=fontsize, ha='right', va='center')
plt.text(1, xtm, '$1$', fontsize=fontsize, ha='center', va='baseline')

plt.plot([1, 1], [0, np.sinh(1)], 'k--', lw=1)
plt.plot([0, 1], np.sinh([1, 1]), 'k--', lw=1)

plt.plot([0, ytl], [1, 1], 'k-', lw=1)

plt.axis('off')

plt.savefig('exercise_59_04_graphs.pdf', bbox_inches='tight')

plt.show()
