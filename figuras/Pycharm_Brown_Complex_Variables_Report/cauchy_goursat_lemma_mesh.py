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
plt.plot([xs, xs], xs_y, 'k-', lw=1)
ysi = ymi + 0.75 * ls
ys = np.arange(ysi, yma, ls)
print(ys)
ys_x = np.zeros((2, ys.shape[0]))
for i, yss in enumerate(ys):
    ys_x[0, i] = xd[int(N / 4) + (np.abs(yd[int(N / 4): int(3 * N / 4)] - yss)).argmin()]
    idx = (np.abs(np.concatenate((yd[int(3 * N / 4):-1], yd[:int(N / 4)])) - yss)).argmin()
    if idx < N/4:
        shift = int(3 * N / 4)
    else:
        shift = -int(N / 4) + 1
    ys_x[1, i] = xd[shift + idx]
plt.plot(ys_x, [ys, ys], 'k-', lw=1)

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

# resaltado del cuadrado sigma_0
plt.plot([xs[nx], xs[nx]], [ys[ny], ys[ny+1]], color='r', lw=1, zorder=2)
plt.plot([xs[nx+1], xs[nx+1]], [ys[ny], ys[ny+1]], color='r', lw=1, zorder=2)
plt.plot([xs[nx], xs[nx+1]], [ys[ny], ys[ny]], color='r', lw=1, zorder=2)
plt.plot([xs[nx], xs[nx+1]], [ys[ny+1], ys[ny+1]], color='r', lw=1, zorder=2)

# etiquetas de los cuadrados
plt.annotate("", xytext=(15, 12), xycoords='data', xy=(xs[nx]+ls/4, ys[ny+1]), textcoords='data',
             arrowprops=dict(width=0, headwidth=4, headlength=7, facecolor='r', edgecolor='r',  shrink=0.01, lw=1,
                             connectionstyle="angle3,angleA=180,angleB=70"))
plt.text(15.3, 12, r'$\sigma_0$', fontsize=fontsize, ha='left', va='center', color='r')
plt.annotate("", xytext=(15, 7.5), xycoords='data', xy=(xs[nx+1]-ls/4, ys[ny+1]-ls/4), textcoords='data',
             arrowprops=dict(width=0, headwidth=4, headlength=7, facecolor='k', edgecolor='k',  shrink=0.01, lw=1,
                             connectionstyle="angle3,angleA=180,angleB=-40"))
plt.text(15.3, 7.5, r'$\sigma_1$', fontsize=fontsize, ha='left', va='center')


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_goursat_lemma_mesh.pdf', bbox_inches='tight')

plt.show()
