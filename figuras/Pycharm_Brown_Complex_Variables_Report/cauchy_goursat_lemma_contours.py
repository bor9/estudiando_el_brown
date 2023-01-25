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


N = 200
thetas = np.linspace(0, 2*math.pi, N)

# CONTORNO
Nd = 8
dx = np.linspace(0, 1, Nd + 1, endpoint=True)
dy = [5.5, 5.2, 5.9, 4.9, 6.4, 5.1, 5.4, 6.4, 5.5]
f = interpolate.interp1d(dx, dy, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xd = dynew * np.cos(thetas)
yd = dynew * np.sin(thetas)

# traslación de la curva
x0 = 8
y0 = 7
xd = xd + x0
yd = yd + y0

# valores maximos y minimos de los ejes
max_ax = 15
xmin = 0
xmax = 16
ymin = 0
ymax = 14

# axis parameters
d = 2
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.9
ytm = -0.5
# font size
fontsize = 14

fig = plt.figure(0, figsize=(5, 5), frameon=False)
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
plt.plot(xd, yd, color='k', lw=2)

# flechas del contorno
a1 = 51
plt.annotate("", xytext=(xd[a1], yd[a1]), xycoords='data', xy=(xd[a1+4], yd[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xd[a1]-0.3, yd[a1]+0.4, r'$C$', fontsize=fontsize, ha='right', va='center')
a1 = 46 + int(N/2)
plt.annotate("", xytext=(xd[a1], yd[a1]), xycoords='data', xy=(xd[a1+4], yd[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

# grilla
# lado de los cuadrados iniciales
ls = 2.8
# coordenadas x y y mínimas y máximas del contorno
xmi = np.min(xd)
xma = np.max(xd)
ymi = np.min(yd)
yma = np.max(yd)
xsi = xmi + ls / 1.5
xs = np.arange(xsi, xma, ls)
xs_y = np.zeros((2, xs.shape[0]))
for i, xss in enumerate(xs):
    xs_y[0, i] = yd[int(N / 2) + (np.abs(xd[int(N / 2): N] - xss)).argmin()]
    xs_y[1, i] = yd[(np.abs(xd[0: int(N / 2)] - xss)).argmin()]
# plt.plot([xs, xs], xs_y, 'k-', lw=1)

ysi = ymi + 0.75 * ls
ys = np.arange(ysi, yma, ls)
ys_x = np.zeros((2, ys.shape[0]))
for i, yss in enumerate(ys):
    ys_x[0, i] = xd[int(N / 4) + (np.abs(yd[int(N / 4): int(3 * N / 4)] - yss)).argmin()]
    idx = (np.abs(np.concatenate((yd[int(3 * N / 4):-1], yd[:int(N / 4)])) - yss)).argmin()
    if idx < N/4:
        shift = int(3 * N / 4)
    else:
        shift = -int(N / 4) + 1
    ys_x[1, i] = xd[shift + idx]
# plt.plot(ys_x, [ys, ys], 'k-', lw=1)

# construcción de subgrilla
dg = 0.3
i = 1
plt.plot([xs[i], xs[i]], [xs_y[0, i], ys[1] + dg], 'k-', lw=1)
i = 2
plt.plot([xs[i], xs[i]], [xs_y[0, i], ys[2] + dg], 'k-', lw=1)
i = 3
plt.plot([xs[i], xs[i]], [xs_y[0, i], ys[2] + dg], 'k-', lw=1)
i = 0
plt.plot([xs[1] - dg, xs[3] + dg], [ys[i], ys[i]], 'k-', lw=1)
i = 1
plt.plot([xs[1] - dg, xs[3] + dg], [ys[i], ys[i]], 'k-', lw=1)
i = 2
plt.plot([xs[2] - dg, xs[3] + dg], [ys[i], ys[i]], 'k-', lw=1)

# flechas
# largo total de la flecha
lta = 1.2
da = 0.2

xext, yext, xt, yt = arrow_construction((xs[1] + xs[2]) / 2, ys[0] + da, lta, 'ru')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction((xs[1] + xs[2]) / 2, ys[0] - da, lta, 'ld')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[1] + da, (xs_y[0, 1] + ys[0]) / 2, 0.6, 'dr')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[1] - da, (xs_y[0, 1] + ys[0]) / 2, 0.6, 'ul')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[2] - da, (xs_y[0, 2] + ys[0]) / 2, lta, 'ul')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[2] + da, (xs_y[0, 2] + ys[0]) / 2, lta, 'dr')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[2] - da, (ys[0] + ys[1]) / 2, lta, 'ul')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[2] + da, (ys[0] + ys[1]) / 2, lta, 'dr')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction((xs[2] + xs[3]) / 2, ys[1] - da, lta, 'ld')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[2] + ls/4, ys[1] + da, 1, 'ru')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
xext, yext, xt, yt = arrow_construction(xs[2] + 3*ls/4, ys[1] + da, 1, 'ru')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')


# subdivision de un cuadrado
# indices del cuadrado a subdividir
nx = 2
ny = 1
# division vertical
xv = (xs[nx] + xs[nx+1]) / 2
plt.plot([xv, xv], [ys[ny], ys[ny+1]], 'k-', lw=1)
# division horizontal
yh = (ys[ny] + ys[ny+1]) / 2
plt.plot([xs[nx], xs[nx+1]], [yh, yh], 'k-', lw=1)


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.text(2, 7, '$R$', fontsize=fontsize, ha='left', va='center')

# circle labels
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

# cuadrado que contiene a la región
x1 = 0.8
y1 = 0.5
S = 14.5
plt.plot([x1, x1 + S], [y1, y1], 'k', lw=1)
plt.plot([x1, x1 + S], [y1 + S, y1 + S], 'k', lw=1)
plt.plot([x1, x1], [y1, y1 + S], 'k', lw=1)
plt.plot([x1 + S, x1 + S], [y1, y1 + S], 'k', lw=1)
xs = 16.5
dx = 0.5
plt.text(xs, (y1 + y1 + S) / 2, '$S$', fontsize=fontsize, ha='center', va='center')
plt.plot([xs-dx, xs+dx], [y1, y1], 'k', lw=1)
plt.plot([xs-dx, xs+dx], [y1 + S, y1 + S], 'k', lw=1)
plt.annotate("", xytext=(xs, y1 + S / 2 + 0.7), xycoords='data', xy=(xs, y1 + S), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=7, facecolor='black', shrink=0.002))
plt.annotate("", xytext=(xs, y1 + S / 2 - 0.7), xycoords='data', xy=(xs, y1), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=4, headlength=7, facecolor='black', shrink=0.002))

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_goursat_lemma_contours.pdf', bbox_inches='tight')

plt.show()
