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


# parámetros
R1 = 1.5
R2 = 5.5
r1 = 2
r2 = 5.1
xz = 1.6
yz = 3.5
rg = 0.87

# para el contorno C
rx = [0, 0.1, 0.2, 0.3, 0.6, 0.75, 1, 1.1, 1.2, 1.3, 1.6, 1.95, 2]
ry = 1.3 * np.array([3, 2.9, 2.5, 2.0, 2.8, 3.3, 3, 2.9, 3.2, 3.5, 2.8, 3, 3])

N = 100
f = interpolate.interp1d(rx, ry, kind='cubic')
rxnew = np.linspace(0, 2, N, endpoint=True)
rynew = f(rxnew)

thetas = np.linspace(0, 2*math.pi, N)
# contorno C
xc = rynew * np.cos(thetas)
yc = rynew * np.sin(thetas)

# contornos C1 y C2
xr1 = r1 * np.cos(thetas)
yr1 = r1 * np.sin(thetas)
xr2 = r2 * np.cos(thetas)
yr2 = r2 * np.sin(thetas)

# region
xR1 = R1 * np.cos(thetas)
yR1 = R1 * np.sin(thetas)
xR2 = R2 * np.cos(thetas)
yR2 = R2 * np.sin(thetas)

# contorno gamma
xg = xz + rg * np.cos(thetas)
yg = yz + rg * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 7
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
xtm = -0.76
ytm = -0.4
# font size
fontsize = 12

fig = plt.figure(1, figsize=(4, 4), frameon=False)
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

# dominio
plt.plot(xR1, yR1, 'k--', lw=1)
plt.plot(xR2, yR2, 'k--', lw=1)
# contorno
plt.plot(xc, yc, color='k', lw=1.5)
# contornos C1 y C2
plt.plot(xr1, yr1, 'k', lw=1.5)
plt.plot(xr2, yr2, 'k', lw=1.5)
# contornos gamma
plt.plot(xg, yg, 'k', lw=1.5)

# puntos R1 y R2
ms = 7
plt.plot(R1, 0, 'k.', ms=ms)
plt.plot(R2, 0, 'k.', ms=ms)
plt.plot(xz, yz, 'k.', ms=ms)
plt.plot(0, 0, 'k.', ms=ms)

# flechas
theta = 7 * math.pi / 4
# C
idx = (np.abs(thetas - theta)).argmin()
plt.annotate("", xytext=(xc[idx], yc[idx]), xycoords='data', xy=(xc[idx+1], yc[idx+1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=9, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xc[idx], yc[idx]-0.2, '$C$', fontsize=fontsize, ha='left', va='top')

# C1
idx = idx + 8
plt.annotate("", xytext=(xr1[idx-4], yr1[idx-4]), xycoords='data', xy=(xr1[idx], yr1[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=9, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xr1[idx]+0.15, yr1[idx]-0.2, '$C_1$', fontsize=fontsize, ha='left', va='top')
# C2
idx = idx - 15
plt.annotate("", xytext=(xr2[idx-1], yr2[idx-1]), xycoords='data', xy=(xr2[idx], yr2[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=9, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xr2[idx]-0.4, yr2[idx]+0.15, '$C_2$', fontsize=fontsize, ha='center', va='bottom')
# gamma
idx = 25 + 20
plt.annotate("", xytext=(xg[idx-11], yg[idx-11]), xycoords='data', xy=(xg[idx], yg[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=9, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xg[idx], yg[idx]+0.3, '$\gamma$', fontsize=fontsize, ha='right', va='bottom')

# r
plt.plot([0, xz], [0, yz], 'k', lw=1)
k = 0.2
plt.text(k * xz + 0.2, k * yz, '$r$', fontsize=fontsize, ha='left', va='center')
# r1
idx = 36
plt.plot(xr1[idx], yr1[idx], 'k.', ms=ms)
plt.plot([0, xr1[idx]], [0, yr1[idx]], 'k', lw=1)
k = 0.4
plt.text(k * xr1[idx], k * yr1[idx] - 0.1, '$r_1$', fontsize=fontsize, ha='right', va='center')
plt.text(xr1[idx]-0.2, yr1[idx], '$s$', fontsize=fontsize, ha='right', va='bottom')
# r2
idx = 30
plt.plot(xr2[idx], yr2[idx], 'k.', ms=ms)
plt.plot([0, xr2[idx]], [0, yr2[idx]], 'k', lw=1)
k = 0.61
plt.text(k * xr2[idx] - 0.1, k * yr2[idx] - 0.1, '$r_2$', fontsize=fontsize, ha='right', va='center')
plt.text(xr2[idx] + 0.3, yr2[idx] + 0.1, '$s$', fontsize=fontsize, ha='left', va='top')


# etiquetas
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.text(R1 - 0.3, xtm, '$R_1$', fontsize=fontsize, ha='right', va='baseline')
plt.text(R2 + dx, xtm, '$R_2$', fontsize=fontsize, ha='left', va='baseline')
plt.text(xz+0.1, yz+0.03, '$z$', fontsize=fontsize, ha='left', va='bottom')

vert = np.vstack((xR2, yR2))
p1 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=-100)
ax.add_artist(p1)

vert = np.vstack((xr2, yr2))
p3 = Polygon(vert.T, fc=(0.75, 0.75, 0.75), alpha=1, zorder=-95)
ax.add_artist(p3)

vert = np.vstack((xg, yg))
p4 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=-95)
ax.add_artist(p4)

vert = np.vstack((xr1, yr1))
p5 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=-95)
ax.add_artist(p5)

vert = np.vstack((xR1, yR1))
p2 = Polygon(vert.T, fc="white", alpha=1, zorder=-90)
ax.add_artist(p2)

plt.axis('off')

# save as pdf image
plt.savefig('laurent_theorem_proof.pdf', bbox_inches='tight')

plt.show()
