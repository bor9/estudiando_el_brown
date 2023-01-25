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
c = (1, 0)

# circulo |z|=1
N = 200
thetas = np.linspace(math.pi, 2 * math.pi, N)
xc = c[0] + r * np.cos(thetas)
yc = c[1] + r * np.sin(thetas)

# valores maximos y minimos de los ejes
xmin = -0.2
xmax = 2.2
ymin = -1
ymax = 0.2


# axis parameters
d = 0.2
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

fig = plt.figure(0, figsize=(3, 1.7), frameon=False)
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

# arcos
plt.plot(xc, yc, color='k', lw=2)
plt.plot([0, 2], [0, 0], color='k', lw=2)
# puntos z = 0 y z = 2
ms = 9
plt.plot(0, 0, 'k.', ms=ms)
plt.plot(2, 0, 'k.', ms=ms)

# flechas
theta = 4 * math.pi / 3
xa = 1 + r * math.cos(theta)
ya = r * math.sin(theta)
r2 = 0.01
plt.annotate("", xytext=(xa, ya), xycoords='data', xy=(xa-r2*math.sin(theta), ya+r2*math.cos(theta)), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
theta = -math.pi / 4
xb = 0.5
plt.annotate("", xytext=(xb, 0), xycoords='data', xy=(xb+0.01, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.plot([1, 1], [0, ytl], 'k-', lw=1)
plt.plot([2, 2], [0, ytl], 'k-', lw=1)
plt.text(1, xtm, '$1$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-0.05, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(2.05, xtm, '$2$', fontsize=fontsize, ha='left', va='baseline')


plt.axis('off')

# save as pdf image
plt.savefig('exercise_46_02.pdf', bbox_inches='tight')

plt.show()
