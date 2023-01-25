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


# CONTORNO: eight curve
rx = [0, 0.1, 0.2, 0.3, 0.6, 0.75, 1, 1.1, 1.2, 1.3, 1.6, 1.95, 2]
ry = [4, 3.4, 3.1, 3.5, 3.8, 4.3, 3, 3.9, 4.2, 4.5, 3.8, 4.3, 4]

N = 100
f = interpolate.interp1d(rx, ry, kind='cubic')
rxnew = np.linspace(0, 2, N, endpoint=True)
rynew = f(rxnew)

thetas = np.linspace(0, 2*math.pi, N)
xc = rynew * np.sin(thetas)
yc = rynew * np.sin(thetas) * np.cos(thetas)

# rotación del eje
r_ang = np.pi/4
xcr = xc * np.cos(r_ang) + yc * np.cos(r_ang)
ycr = -xc * np.sin(r_ang) + yc * np.cos(r_ang)

# traslación de las curvas
x0 = 6.5
y0 = 6
xcr = xcr + x0
ycr = ycr + y0

# valores maximos y minimos de los ejes
max_ax = 12
xmin = 0
xmax = max_ax
ymin = 0
ymax = max_ax

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

fig = plt.figure(0)
ax = fig.add_subplot(111)
plt.plot(rx, ry, 'k.', ms=8)
plt.plot(rxnew, rynew, 'k-')

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

# contorno
plt.plot(xcr, ycr, color='k', lw=2)

# flechas
a1 = 60
plt.annotate("", xytext=(xcr[a1-2], ycr[a1-2]), xycoords='data', xy=(xcr[a1], ycr[a1]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xcr[0]-1.5, ycr[0]+1.5, r'$C_1$', fontsize=fontsize, ha='center', va='center')
a3 = 92
plt.annotate("", xytext=(xcr[a3-2], ycr[a3-2]), xycoords='data', xy=(xcr[a3], ycr[a3]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

a2 = 14
plt.annotate("", xytext=(xcr[a2-2], ycr[a2-2]), xycoords='data', xy=(xcr[a2], ycr[a2]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xcr[0]+1.5, ycr[0]-1.5, r'$C_2$', fontsize=fontsize, ha='center', va='center')
a2 = 44
plt.annotate("", xytext=(xcr[a2-2], ycr[a2-2]), xycoords='data', xy=(xcr[a2], ycr[a2]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)

plt.text(xcr[0]+0.6, ycr[0]+0.6, r'$C$', fontsize=fontsize, ha='center', va='center')

# etiquetas de los ejes
id = 35
#plt.text(xd[id]-0.1, yd[id]+0.1, r'$D$', fontsize=fontsize, ha='right', va='bottom')
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('cauchy_goursat_theorem_not_simple_extension.pdf', bbox_inches='tight')

plt.show()
