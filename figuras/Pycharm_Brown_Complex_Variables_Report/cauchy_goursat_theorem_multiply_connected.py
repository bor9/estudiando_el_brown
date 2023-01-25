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


def arrow_construction(xc, yc, len, dir):
    # largo de la punta de la flecha
    lpa = 0.4
    # altura de la punta de la flecha
    apa = 0.15
    dd = lpa/2
    if dir=='lu':
        # extremos de la flecha
        p = xc - len / 2
        xext = [p + dd, xc + len / 2]
        yext = [yc, yc]
        # triángulo
        xt = [p, p + lpa, p + lpa]
        yt = [yc, yc, yc + apa]
    elif dir=='ld':
        # extremos de la flecha
        p = xc - len / 2
        xext = [p + dd, xc + len / 2]
        yext = [yc, yc]
        # triángulo
        xt = [p, p + lpa, p + lpa]
        yt = [yc, yc, yc - apa]
    elif dir=='ru':
        # extremos de la flecha
        p = xc + len / 2
        xext = [xc - len / 2, p - dd]
        yext = [yc, yc]
        # triángulo
        xt = [p, p - lpa, p - lpa]
        yt = [yc, yc, yc + apa]
    elif dir=='rd':
        # extremos de la flecha
        p = xc + len / 2
        xext = [xc - len / 2, p - dd]
        yext = [yc, yc]
        # triángulo
        xt = [p, p - lpa, p - lpa]
        yt = [yc, yc, yc - apa]
    elif dir=='ul':
        # extremos de la flecha
        p = yc + len / 2
        xext = [xc, xc]
        yext = [yc - len / 2, p - dd]
        # triángulo
        xt = [xc, xc, xc - apa]
        yt = [p - lpa, p, p - lpa]
    elif dir=='ur':
        # extremos de la flecha
        p = yc + len / 2
        xext = [xc, xc]
        yext = [yc - len / 2, p - dd]
        # triángulo
        xt = [xc, xc, xc + apa]
        yt = [p - lpa, p, p - lpa]
    elif dir=='dl':
        # extremos de la flecha
        p = yc - len / 2
        xext = [xc, xc]
        yext = [p + dd, yc + len / 2]
        # triángulo
        xt = [xc, xc, xc - apa]
        yt = [p, p + lpa, p + lpa]
    elif dir=='dr':
        # extremos de la flecha
        p = yc - len / 2
        xext = [xc, xc]
        yext = [p + dd, yc + len / 2]
        # triángulo
        xt = [xc, xc, xc + apa]
        yt = [p, p + lpa, p + lpa]
    return xext, yext, xt, yt


def arrow_rotation(xext, yext, xt, yt, theta):
    # matriz de transformacion
    T = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    exttrans = T @ np.array([xext, yext])
    ttrans = T @ np.array([xt, yt])
    return exttrans[0, :], exttrans[1, :], ttrans[0, :], ttrans[1, :]


N = 200
thetas = np.linspace(0, 2*math.pi, N)

# CONTORNO C
yd = [7.5, 4.5, 3.8, 5.2, 6.5, 4.5, 3.9, 7, 7.5]
Nd = len(yd)
xd = np.linspace(0, 1, Nd, endpoint=True)
f = interpolate.interp1d(xd, yd, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xd = dynew * np.cos(thetas)
yd = dynew * np.sin(thetas)

# CONTORNO C_1
yd1 = [1.5, 1.2, 1.9, 2.4, 1.1, 1.4, 1.5]
Nd1 = len(yd1)
xd1 = np.linspace(0, 1, Nd1, endpoint=True)
f = interpolate.interp1d(xd1, yd1, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xd1 = 0.8 * dynew * np.cos(thetas)
yd1 = 0.8 * dynew * np.sin(thetas)

# CONTORNO C_2
yd2 = [1.5, 1, 1, 1, 1, 1.6, 1.5]
Nd2 = len(yd2)
xd2 = np.linspace(0, 1, Nd2, endpoint=True)
f = interpolate.interp1d(xd2, yd2, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xd2 = 1.2 * dynew * np.cos(thetas)
yd2 = 1.2 * dynew * np.sin(thetas)


# traslación de la curva
x0 = 8
y0 = 6
xd = xd + x0
yd = yd + y0
x01 = 6
y01 = 6
xd1 = xd1 + x01
yd1 = yd1 + y01
x02 = 12
y02 = 5
xd2 = xd2 + x02
yd2 = yd2 + y02


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
plt.plot(xd, yd, color='k', lw=2)
plt.plot(xd1, yd1, color='k', lw=2)
plt.plot(xd2, yd2, color='k', lw=2)

# flechas del contorno C
a1 = 57
plt.annotate("", xytext=(xd[a1], yd[a1]), xycoords='data', xy=(xd[a1+4], yd[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xd[a1], yd[a1]+0.6, r'$C$', fontsize=fontsize, ha='right', va='center')
a1 = 66 + int(N/2)
plt.annotate("", xytext=(xd[a1], yd[a1]), xycoords='data', xy=(xd[a1+4], yd[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

# flechas del contorno C_1
a1 = 60
plt.annotate("", xytext=(xd1[a1+8], yd1[a1+8]), xycoords='data', xy=(xd1[a1], yd1[a1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(x01-0.3, y01+0.1, r'$C_1$', fontsize=fontsize, ha='center', va='center')
a1 = 30 + int(N/2)
plt.annotate("", xytext=(xd1[a1], yd1[a1]), xycoords='data', xy=(xd1[a1-4], yd1[a1-4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

# flechas del contorno C_2
a1 = 25
plt.annotate("", xytext=(xd2[a1+8], yd2[a1+8]), xycoords='data', xy=(xd2[a1], yd2[a1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(x02+0.4, y02-0.3, r'$C_2$', fontsize=fontsize, ha='center', va='center')
a1 = 60 + int(N/2)
plt.annotate("", xytext=(xd2[a1+8], yd2[a1+8]), xycoords='data', xy=(xd2[a1], yd2[a1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

# caminos y flechas
# largo total de la flecha
lta = 1.2
da = 0.2

# camino 1
i1 = int(N/2)-5
i2 = int(N/2)-8
plt.plot([xd[i1], xd1[i2]], [yd[i1], yd1[i2]], 'k-')
# flecha camino 1
theta = np.arctan((yd1[i2]-yd[i1])/(xd1[i2]-xd[i1]))
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ru')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
xc = (xd[i1] + xd1[i2]) / 2
yc = (yd[i1] + yd1[i2]) / 2
plt.plot(xext+xc, yext+yc+da, 'k', lw=1)
plt.fill(xt+xc, yt+yc+da, facecolor='k', edgecolor='k')
da2 = 0.7
plt.text(xc, yc+da2, '$L_1$', fontsize=fontsize, ha='center', va='baseline')
# flecha camino 1
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ld')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
xc = (xd[i1] + xd1[i2]) / 2
yc = (yd[i1] + yd1[i2]) / 2
plt.plot(xext+xc, yext+yc-da, 'k', lw=1)
plt.fill(xt+xc, yt+yc-da, facecolor='k', edgecolor='k')

# camino 2
i1 = 190
i2 = 95
plt.plot([xd1[i1], xd2[i2]], [yd1[i1], yd2[i2]], 'k-')
# flecha camino 2
theta = np.arctan((yd2[i2]-yd1[i1])/(xd2[i2]-xd1[i1]))
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ru')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
xc = (xd1[i1] + xd2[i2]) / 2
yc = (yd1[i1] + yd2[i2]) / 2
plt.plot(xext+xc, yext+yc+da, 'k', lw=1)
plt.fill(xt+xc, yt+yc+da, facecolor='k', edgecolor='k')
plt.text(xc, yc+da2, '$L_2$', fontsize=fontsize, ha='center', va='baseline')
# flecha camino 2
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ld')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
plt.plot(xext+xc, yext+yc-da, 'k', lw=1)
plt.fill(xt+xc, yt+yc-da, facecolor='k', edgecolor='k')

# camino 3
i1 = 190
i2 = 193
plt.plot([xd2[i1], xd[i2]], [yd2[i1], yd[i2]], 'k-')
# flecha camino 3
theta = np.arctan((yd[i2]-yd2[i1])/(xd[i2]-xd2[i1]))
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ru')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
xc = (xd2[i1] + xd[i2]) / 2
yc = (yd2[i1] + yd[i2]) / 2
plt.plot(xext+xc, yext+yc+da, 'k', lw=1)
plt.fill(xt+xc, yt+yc+da, facecolor='k', edgecolor='k')
plt.text(xc, yc+da2, '$L_3$', fontsize=fontsize, ha='center', va='baseline')
# flecha camino 3
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ld')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
plt.plot(xext+xc, yext+yc-da, 'k', lw=1)
plt.fill(xt+xc, yt+yc-da, facecolor='k', edgecolor='k')

# camino gamma 1
i = 30
di = 5
xc = (xd[i-di] + xd[i+di]) / 2
yc = (yd[i-di] + yd[i+di]) / 2
theta = np.arctan((yd[i+di]-yd[i-di])/(xd[i+di]-xd[i-di]))
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ld')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
plt.plot(xext+xc, yext+yc-da, 'k', lw=1)
plt.fill(xt+xc, yt+yc-da, facecolor='k', edgecolor='k')
plt.text(xc, yc-da2, '$\Gamma_1$', fontsize=fontsize, ha='center', va='top')

# camino gamma 2
i = 130
di = 5
xc = (xd[i-di] + xd[i+di]) / 2
yc = (yd[i-di] + yd[i+di]) / 2
theta = np.arctan((yd[i+di]-yd[i-di])/(xd[i+di]-xd[i-di]))
xext, yext, xt, yt = arrow_construction(0, 0, lta, 'ru')
xext, yext, xt, yt = arrow_rotation(xext, yext, xt, yt, theta)
plt.plot(xext+xc, yext+yc+da, 'k', lw=1)
plt.fill(xt+xc, yt+yc+da, facecolor='k', edgecolor='k')
plt.text(xc, yc+da2, '$\Gamma_2$', fontsize=fontsize, ha='center', va='baseline')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_goursat_theorem_multiply_connected.pdf', bbox_inches='tight')

plt.show()
