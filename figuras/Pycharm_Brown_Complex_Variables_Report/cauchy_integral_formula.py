import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import interpolate
from matplotlib.patches import Polygon

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
x0 = 13
y0 = 4
rho = 2
N = 200
thetas = np.linspace(0, 2*math.pi, N)

# CONTORNO C
yc = [7, 4.5, 3.5, 4, 6.5, 4.2, 4.5, 7.3, 7]
Nc = len(yc)
xc = np.linspace(0, 1, Nc, endpoint=True)
f = interpolate.interp1d(xc, yc, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xc = dynew * np.cos(thetas)
yc = dynew * np.sin(thetas)

# CONTORNO C_rho
xcp = x0 + rho * np.cos(thetas)
ycp = y0 + rho * np.sin(thetas)

# traslación de la curva
xt = 8.5
yt = 6
xc = xc + xt
yc = yc + yt

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
plt.plot(xcp, ycp, color='k', lw=2, zorder=3)
plt.plot(xc, yc, color='k', lw=2, zorder=3)

vert = np.vstack((xc, yc))
p1 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=1)
ax.add_artist(p1)
vert = np.vstack((xcp, ycp))
p2 = Polygon(vert.T, fc="white", alpha=1, zorder=2)
ax.add_artist(p2)

# flechas del contorno C rho
a1 = 57
da = 8
plt.annotate("", xytext=(xcp[a1], ycp[a1]), xycoords='data', xy=(xcp[a1 + da], ycp[a1 + da]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xcp[a1], ycp[a1] + 0.3, r'$C_\rho$', fontsize=fontsize, ha='right', va='bottom')
a1 = a1 + int(N/2)
plt.annotate("", xytext=(xcp[a1], ycp[a1]), xycoords='data', xy=(xcp[a1 + da], ycp[a1 + da]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)


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
plt.text(x0, y0 - 0.2, '$z_0$', fontsize=fontsize, ha='center', va='top')
# radio
i = 25
plt.plot([x0, xcp[i]], [y0, ycp[i]], 'k', lw=1, zorder=4)
plt.text((x0 + xcp[i]) / 2 + 0.3, (y0 + ycp[i]) / 2 - 0.3, r'$\rho$', fontsize=fontsize, ha='center', va='center')

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_integral_formula.pdf', bbox_inches='tight')

plt.show()
