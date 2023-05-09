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


# parámetros
a = 2
b = 1

# valores maximos y minimos de los ejes
max_ax = 3
xmin = -max_ax
xmax = max_ax
ymin = -1.5
ymax = 1.5


# axis parameters
d = 0
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.35
ytm = -0.2
# font size
fontsize = 12

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
plt.plot([-a, a], [0, 0], color='k', lw=2)
plt.plot([-a, a], [b, b], color='k', lw=2)
plt.plot([a, a], [0, b], color='k', lw=2)
plt.plot([-a, -a], [0, b], color='k', lw=2)

# flechas
da = 0.2
dd = 0.01
ar = -a/2
plt.annotate("", xytext=(ar-dd, 0), xycoords='data', xy=(ar, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
ar = b/2+da
plt.annotate("", xytext=(a, ar-dd), xycoords='data', xy=(a, ar), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
ar = a/2
plt.annotate("", xytext=(ar+dd, b), xycoords='data', xy=(ar, b), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
ar = b/2-da
plt.annotate("", xytext=(-a, ar+dd), xycoords='data', xy=(-a, ar), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)

# singularidades
ms = 7
x = math.sqrt(3/2)
y = 1 / math.sqrt(2)
plt.plot(x, y, 'k.', ms=ms)
plt.plot([0, x], [0, y], 'k-', lw=1)
plt.plot(-x, y, 'k.', ms=ms)
plt.plot([0, -x], [0, y], 'k-', lw=1)
plt.plot(-x, -y, 'k.', ms=ms)
plt.plot([0, -x], [0, -y], 'k-', lw=1)
plt.plot(x, -y, 'k.', ms=ms)
plt.plot([0, x], [0, -y], 'k-', lw=1)

tt = np.linspace(0, np.pi/6, 20)
r = 0.6
ang_x = r * np.cos(tt)
ang_y = r * np.sin(tt)
plt.plot(ang_x, ang_y, 'k-', lw=1)
plt.text(r+0.05, 0.04, '$\pi/6$', fontsize=fontsize, ha='left', va='bottom')
plt.text(x/2-0.1, y/2+0.05, '$\sqrt{2}$', fontsize=fontsize, ha='center', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.text(a, xtm, '$2$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-a, xtm, '$-2$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, b+0.1, '$1$', fontsize=fontsize, ha='center', va='baseline')
plt.text(a+0.02, b+0.02, '$C$', fontsize=fontsize, ha='left', va='bottom')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_83_07.pdf', bbox_inches='tight')

plt.show()
