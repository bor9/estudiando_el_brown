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
R0 = 1
r0 = 0.85

# circulo |z|=1
N = 200
thetas = np.linspace(0, 2 * math.pi, N)
# contorno
xc = r0 * np.cos(thetas)
yc = r0 * np.sin(thetas)
# dominio
xd = R0 * np.cos(thetas)
yd = R0 * np.sin(thetas)

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
xtm = -0.2
ytm = -0.1
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 4), frameon=False)
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
# dominio
plt.plot(xd, yd, 'k--', lw=1.5)
# puntos
ms = 9
# R0
plt.plot(1, 0, 'k.', ms=ms)
# origen
plt.plot(0, 0, 'k.', ms=ms)
# s
nc = 20
plt.plot(xc[nc], yc[nc], 'k.', ms=ms)
plt.plot([0, xc[nc]], [0, yc[nc]], 'k-', lw=1.5)
plt.text(xc[nc], yc[nc]-0.05, '$s$', fontsize=fontsize, ha='right', va='top')
plt.text(xc[nc]/2-0.06, yc[nc]/2+0.14, '$r_0$', fontsize=fontsize, ha='center', va='center')
# z
rz = 0.65
thetaz = np.pi / 2 + np.pi / 6
xz = rz * np.cos(thetaz)
yz = rz * np.sin(thetaz)
plt.plot(xz, yz, 'k.', ms=ms)
plt.plot([0, xz], [0, yz], 'k-', lw=1.5)
plt.text(xz-0.07, yz, '$z$', fontsize=fontsize, ha='right', va='center')
plt.text(xz/2-0.1, yz/2-0.03, '$r$', fontsize=fontsize, ha='center', va='center')

# flecha del contorno
nc = 175
dn = 3
plt.annotate("", xy=(xc[nc], yc[nc]), xycoords='data', xytext=(xc[nc-dn], yc[nc-dn]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
# etiqueta del contorno
plt.text(xc[nc]-0.05, yc[nc]+0.02, r'$C_0$', fontsize=fontsize, ha='right', va='bottom')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(R0 + 0.05, xtm, '$R_0$', fontsize=fontsize, ha='left', va='baseline')
plt.text(-0.05, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('taylor_series_proof.pdf', bbox_inches='tight')

plt.show()
