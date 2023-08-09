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

# circulo |z|=1
N = 100
thetas = np.linspace(0, math.pi, N)
xc = R * np.cos(thetas)
yc = R * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 3.5
xmin = -max_ax
xmax = max_ax
ymin = 0
ymax = max_ax


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

fig = plt.figure(0, figsize=(4, 2.3), frameon=False)
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
plt.plot([-R, R], [0, 0], color='k', lw=2)

# flechas
idx= 25
plt.annotate("", xytext=(xc[idx-4], yc[idx-4]), xycoords='data', xy=(xc[idx], yc[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
xa = -R/2 + 0.3
plt.annotate("", xytext=(xa-0.01, 0), xycoords='data', xy=(xa, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

# ceros
ms = 8
zx1 = -1.7
zy1 = 1
plt.plot(zx1, zy1, 'k.', ms=ms)
plt.text(zx1, zy1+xtm, '$z_1$', fontsize=fontsize, ha='center', va='baseline')
zx2 = -1.5
zy2 = 2
plt.plot(zx2, zy2, 'k.', ms=ms)
plt.text(zx2, zy2+xtm, '$z_2$', fontsize=fontsize, ha='center', va='baseline')
zx3 = -0.7
zy3 = 1.7
plt.plot(zx3, zy3, 'k.', ms=ms)
plt.text(zx3, zy3+xtm, '$z_3$', fontsize=fontsize, ha='center', va='baseline')
plt.plot(-0.3, 2.3, 'k.', ms=ms)
plt.plot(0.2, 2.4, 'k.', ms=ms)
plt.plot(0.5, 1.7, 'k.', ms=ms)
plt.plot(0.9, 1.6, 'k.', ms=ms)
plt.plot(1.1, 1.8, 'k.', ms=ms)
plt.plot(1.5, 1.3, 'k.', ms=ms)
plt.plot(2.1, 1.2, 'k.', ms=ms)
zxn = 2.5
zyn = 0.8
plt.plot(zxn, zyn, 'k.', ms=ms)
plt.text(zxn, zyn+xtm, '$z_n$', fontsize=fontsize, ha='center', va='baseline')

# etiquetas de los contornos
plt.text(xc[idx]+0.2, yc[idx], r'$C_R$', fontsize=fontsize, ha='left', va='bottom')
plt.text(R, xtm, '$R$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-R, xtm, '$-R$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-0.17, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.axis('off')

# save as pdf image
plt.savefig('improper_integral_evaluation_residues.pdf', bbox_inches='tight')

plt.show()
