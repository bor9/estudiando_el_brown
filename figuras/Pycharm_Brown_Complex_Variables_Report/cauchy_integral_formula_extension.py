import matplotlib.pyplot as plt
import numpy as np
import math
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


# z0
x0 = 9.5
y0 = 7
rho = 2
N = 200
thetas = np.linspace(0, 2*math.pi, N)

# CONTORNO C
yc = [6, 4.5, 5, 6, 6.5, 4.5, 5, 6.7, 6]
Nc = len(yc)
xc = np.linspace(0, 1, Nc, endpoint=True)
f = interpolate.interp1d(xc, yc, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xc = dynew * np.cos(thetas)
yc = dynew * np.sin(thetas)


# traslación de la curva
xt = 8.5
yt = 6
xc = xc + xt
yc = yc + yt

# cálculo del punto de la curva a menor distancia de z
imin = np.argmin((xc - x0) ** 2 + (yc - y0) ** 2)


# valores maximos y minimos de los ejes
max_ax = 15
xmin = 0
xmax = 18
ymin = 0
ymax = 11

# axis parameters
d = 1
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.8
ytm = -0.5
# font size
fontsize = 14

fig = plt.figure(0, figsize=(6, 4), frameon=False)
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
plt.plot(xc, yc, color='k', lw=2, zorder=3)

# flechas del contorno C
a1 = 68
plt.annotate("", xytext=(xc[a1], yc[a1]), xycoords='data', xy=(xc[a1 + 4], yc[a1 + 4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xc[a1], yc[a1] + 0.3, r'$C$', fontsize=fontsize, ha='right', va='bottom')
a1 = 62 + int(N/2)
plt.annotate("", xytext=(xc[a1], yc[a1]), xycoords='data', xy=(xc[a1 + 4], yc[a1 + 4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

#
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

# z0
ms = 7
plt.plot(x0, y0, 'k.', ms=ms, zorder=4)
plt.text(x0, y0 - 0.2, '$z$', fontsize=fontsize, ha='center', va='top')

# distancia a la curva
plt.plot(xc[imin], yc[imin], 'k.', ms=ms)
plt.plot([x0, xc[imin]], [y0, yc[imin]], 'k-', lw=1)
plt.text((x0 + xc[imin]) / 2 - 0.4, (y0 + yc[imin]) / 2 + 0.3, '$d$', fontsize=fontsize, ha='center', va='center')

# z+Delta z
x1 = 7.4
y1 = 6.2
plt.plot(x1, y1, 'k.', ms=ms)
plt.text(x1, y1 - 0.3, '$z+\Delta z$', fontsize=fontsize, ha='center', va='top')
plt.plot([x0, x1], [y0, y1], 'k-', lw=1)
# plt.text((x0 + x1) / 2 - 0.2, (y0 + y1) / 2 + 0.8, '$|\Delta z|$', fontsize=fontsize, ha='center', va='center')
plt.text((x0 + x1) / 2 - 0.2, (y0 + y1) / 2 + 0.7, '$|\Delta z|$', fontsize=fontsize, ha='center', va='center',
         rotation=180 * np.arctan((y1-y0)/(x1-x0)) / np.pi)


# s
i = 190
sx = xc[i]
sy = yc[i]
plt.plot(sx, sy, 'k.', ms=ms)
plt.plot([x0, sx], [y0, sy], 'k-', lw=1)
#plt.text((x0 + sx) / 2 + 0.2, (y0 + sy) / 2 + 1, '$|s-z|$', fontsize=fontsize, ha='center', va='center')
plt.text((x0 + sx) / 2 + 0.2, (y0 + sy) / 2 + 0.7, '$|s-z|$', fontsize=fontsize, ha='center', va='center',
         rotation=180 * np.arctan((sy-y0)/(sx-x0)) / np.pi)
plt.text(sx + 0.4, sy, '$s$', fontsize=fontsize, ha='left', va='center')

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_integral_formula_extension.pdf', bbox_inches='tight')

plt.show()
