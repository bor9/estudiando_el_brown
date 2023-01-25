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



N = 200
thetas = np.linspace(0, 2*math.pi, N)

# CONTORNO C_1
yd = [7.5, 4.5, 3.8, 5.2, 6.5, 4.5, 4.5, 7.5, 7.5]
Nd = len(yd)
xd = np.linspace(0, 1, Nd, endpoint=True)
f = interpolate.interp1d(xd, yd, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xd = dynew * np.cos(thetas)
yd = dynew * np.sin(thetas)


# CONTORNO C_2
yd2 = [3.5, 2.5, 1.5, 2, 3.5, 3.2, 2.5, 3.1, 3.5]
Nd2 = len(yd2)
xd2 = np.linspace(0, 1, Nd2, endpoint=True)
f = interpolate.interp1d(xd2, yd2, kind='cubic')
dxnew = np.linspace(0, 1, N, endpoint=True)
dynew = f(dxnew)
xd2 = 1 * dynew * np.cos(thetas)
yd2 = 1 * dynew * np.sin(thetas)


# traslación de la curva
x0 = 8
y0 = 6
xd = xd + x0
yd = yd + y0
x02 = 8.5
y02 = 6
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
plt.plot(xd, yd, color='k', lw=2, zorder=3)
plt.plot(xd2, yd2, color='k', lw=2, zorder=3)

vert = np.vstack((xd, yd))
p1 = Polygon(vert.T, fc=(0.9, 0.9, 0.9), alpha=1, zorder=1)
ax.add_artist(p1)
vert = np.vstack((xd2, yd2))
p2 = Polygon(vert.T, fc="white", alpha=1, zorder=2)
ax.add_artist(p2)

# flechas del contorno C_2
a1 = 57
plt.annotate("", xytext=(xd[a1], yd[a1]), xycoords='data', xy=(xd[a1+4], yd[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xd[a1], yd[a1]+0.4, r'$C_2$', fontsize=fontsize, ha='right', va='bottom')
a1 = 66 + int(N/2)
plt.annotate("", xytext=(xd[a1], yd[a1]), xycoords='data', xy=(xd[a1+4], yd[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)


# flechas del contorno C_2
a1 = 68
plt.annotate("", xytext=(xd2[a1], yd2[a1]), xycoords='data', xy=(xd2[a1+4], yd2[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
plt.text(xd2[a1], yd2[a1]-0.4, r'$C_1$', fontsize=fontsize, ha='center', va='top')
a1 = 62 + int(N/2)
plt.annotate("", xytext=(xd2[a1], yd2[a1]), xycoords='data', xy=(xd2[a1+4], yd2[a1+4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)


# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_goursat_deformation_principle.pdf', bbox_inches='tight')

plt.show()
