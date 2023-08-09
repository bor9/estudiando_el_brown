import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

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

N = 200
thetas = np.linspace(0, 2 * np.pi, N)

# construcción del contorno C
rx = [0, 0.1, 0.2, 0.3, 0.6, 0.75, 1, 1.1, 1.2, 1.3, 1.6, 1.95, 2]
ry = 0.4 * np.array([3, 2.9, 2.5, 2.0, 2.8, 3.3, 3, 2.9, 3.2, 3.5, 2.8, 3, 3])
f = interpolate.interp1d(rx, ry, kind='cubic')
rxnew = np.linspace(0, 2, N, endpoint=True)
rynew = f(rxnew)

x0 = 0
y0 = 0
xc = x0 + rynew * np.cos(thetas)
yc = y0 + rynew * np.sin(thetas)

# mapeo: f(z) = (z^2 + z) / 2
zc = xc + 1j * yc
wc = (np.power(zc, 2) + zc) / 2

# valores maximos y minimos de los ejes
max_ax = 1.2
xmin = -max_ax
xmax = max_ax
ymin = -max_ax
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
xtm = -0.2
ytm = -0.11
# font size
fontsize = 14

fig = plt.figure(0, figsize=(8, 4), frameon=False)

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

plt.plot(xc, yc, color='k', lw=2)
ms = 9
idx0 = 20
idx = idx0 + 20
plt.plot(xc[idx0], yc[idx0], 'k.', ms=ms)
plt.plot(xc[idx], yc[idx], 'k.', ms=ms)
plt.text(xc[idx0], yc[idx0] + 0.1, '$z_0$', fontsize=fontsize, ha='left', va='baseline')
plt.text(xc[idx], yc[idx] + 0.1, '$z$', fontsize=fontsize, ha='left', va='baseline')

# flechas de los contornos
nc1 = 75
dn = 3
plt.annotate("", xy=(xc[nc1], yc[nc1]), xycoords='data', xytext=(xc[nc1 - dn], yc[nc1 - dn]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
nc2 = 175
plt.annotate("", xy=(xc[nc2], yc[nc2]), xycoords='data', xytext=(xc[nc2 - dn], yc[nc2 - dn]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xc[nc2] + 0.05, yc[nc2] - 0.1, '$C$', fontsize=fontsize, ha='center', va='top')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.axis('off')

##################
# transformación #
##################

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

plt.plot(np.real(wc), np.imag(wc), color='k', lw=2)
plt.plot(np.real(wc[idx0]), np.imag(wc[idx0]), 'k.', ms=ms)
plt.plot(np.real(wc[idx]), np.imag(wc[idx]), 'k.', ms=ms)
plt.text(np.real(wc[idx0]), np.imag(wc[idx0]) + 0.1, '$w_0$', fontsize=fontsize, ha='center', va='baseline')
plt.text(np.real(wc[idx]), np.imag(wc[idx]) + 0.1, '$w$', fontsize=fontsize, ha='center', va='baseline')

plt.annotate("", xy=(np.real(wc[idx0]), np.imag(wc[idx0])), xycoords='data',
             xytext=(0, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=9, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.annotate("", xy=(np.real(wc[idx]), np.imag(wc[idx])), xycoords='data',
             xytext=(0, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=9, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)


# flechas del contorno
plt.annotate("", xy=(np.real(wc[nc1]), np.imag(wc[nc1])), xycoords='data',
             xytext=(np.real(wc[nc1 - dn]), np.imag(wc[nc1 - dn])), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.annotate("", xy=(np.real(wc[nc2]), np.imag(wc[nc2])), xycoords='data',
             xytext=(np.real(wc[nc2 - dn]), np.imag(wc[nc2 - dn])), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(np.real(wc[nc2]), np.imag(wc[nc2]) - 0.1, '$\Gamma$', fontsize=fontsize, ha='center', va='top')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$u$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$v$', fontsize=fontsize, ha='left', va='center')

# phi0
ra = 0.3
na = 30
thetaa = np.arctan2(np.imag(wc[idx0]), np.real(wc[idx0]))
thetas = np.linspace(0, thetaa, N)
xa = ra * np.cos(thetas)
ya = ra * np.sin(thetas)
plt.plot(xa, ya, color='k', lw=1)
ra = 0.35
plt.text(ra * np.cos(thetaa/2) + 0.1, ra * np.sin(thetaa/2) + 0.05, '$\phi_0$', fontsize=fontsize, ha='center', va='center')

plt.axis('off')

# save as pdf image
plt.savefig('argument_principle_mapping.pdf', bbox_inches='tight')

plt.show()

