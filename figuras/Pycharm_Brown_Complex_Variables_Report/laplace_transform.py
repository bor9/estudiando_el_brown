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
R = 3
gamma = 1.3

# circulo |z|=1
N = 100
thetas = np.linspace(math.pi / 2, 3 * math.pi / 2, N)
xc = gamma + R * np.cos(thetas)
yc = R * np.sin(thetas)

# valores maximos y minimos de los ejes
xmin = -2
xmax = 2
ymin = -R
ymax = R


# axis parameters
d = 0.9
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.45
ytm = -0.25
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 5), frameon=False)
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
plt.plot(xc, yc, color='k', lw=2)
plt.plot([gamma, gamma], [-R, R], color='k', lw=2)

# flechas
idx= 25
plt.annotate("", xytext=(xc[idx-4], yc[idx-4]), xycoords='data', xy=(xc[idx], yc[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xc[idx], yc[idx] + 0.15, '$C_R$', fontsize=fontsize, ha='right', va='bottom')

ya = R/2
plt.annotate("", xytext=(gamma, ya), xycoords='data', xy=(gamma, ya+0.01), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(gamma + 0.25, ya, '$L_R$', fontsize=fontsize, ha='left', va='top')

# csingularidades
ms = 8
zx1 = 1.1
zy1 = -2
plt.plot(zx1, zy1, 'k.', ms=ms)
plt.text(zx1, zy1 - 0.4, '$s_1$', fontsize=fontsize, ha='right', va='baseline')
zx2 = -0.4
zy2 = -1.3
plt.plot(zx2, zy2, 'k.', ms=ms)
plt.text(zx2, zy2+xtm, '$s_2$', fontsize=fontsize, ha='center', va='baseline')
zx3 = 0.4
zy3 = -0.2
plt.plot(zx3, zy3, 'k.', ms=ms)
plt.text(zx3, zy3+xtm, '$s_3$', fontsize=fontsize, ha='center', va='baseline')
plt.plot(1, 0.5, 'k.', ms=ms)
plt.plot(-1, 0.7, 'k.', ms=ms)
plt.plot(0.7, 1, 'k.', ms=ms)
plt.plot(0.2, 1.2, 'k.', ms=ms)
plt.plot(-0.5, 1.8, 'k.', ms=ms)
plt.plot(-0.3, 0.2, 'k.', ms=ms)
plt.plot(-0.6, 0.8, 'k.', ms=ms)
zxn = 0.9
zyn = 2.4
plt.plot(zxn, zyn, 'k.', ms=ms)
plt.text(zxn, zyn+xtm, '$s_N$', fontsize=fontsize, ha='center', va='baseline')

plt.plot(gamma, -R, 'k.', ms=ms)
plt.text(gamma + 0.25, -R, '$\gamma-iR$', fontsize=fontsize, ha='left', va='center')
plt.plot(gamma, R, 'k.', ms=ms)
plt.text(gamma + 0.25, R, '$\gamma+iR$', fontsize=fontsize, ha='left', va='center')
plt.text(-0.17, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.plot(gamma, 0, 'k.', ms=ms)
plt.text(gamma + 0.25, xtm, '$\gamma$', fontsize=fontsize, ha='left', va='baseline')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.axis('off')

# save as pdf image
plt.savefig('laplace_transform.pdf', bbox_inches='tight')

plt.show()
