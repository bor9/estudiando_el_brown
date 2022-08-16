import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
import math

from matplotlib import cm

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


#####################################
# PARAMETERS - This can be modified #
#####################################

# parámetros de la elipse
a1 = 1
a2 = 1.8

#####################
# END OF PARAMETERS #
#####################

xmax = 4
xmin = -xmax
ymax = 4
ymin = -ymax

# axis parameters
dx = 0.7
xmax_ax = xmax + dx
xmin_ax = xmin - dx
ymax_ax = ymax + dx
ymin_ax = ymin - dx

# hiperbola
dx = 1.4
x1 = np.linspace(xmin, xmax, 200)
# ramas superior e inferior
yu1 = np.sqrt(np.square(x1) + a1**2)
yd1 = -np.sqrt(np.square(x1) + a1**2)

# hiperbola rotada
dx = 1.4
y2 = np.linspace(ymin + dx, ymax - dx, 200)
xd2 = np.sqrt(np.square(y2) + a2**2)
xi2 = -np.sqrt(np.square(y2) + a2**2)
# matriz de rotación
phi = 3 * math.pi / 4
rmatrix = np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])
# ramas superior e inferior
ub = np.dot(rmatrix, [xd2, y2])
db = np.dot(rmatrix, [xi2, y2])

c1 = -(a1 ** 2)
c2 = -(a2 ** 2)


# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.55
# font size
fontsize = 14
# colors from coolwarm
cNorm = colors.Normalize(vmin=0, vmax=1)
scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cm.coolwarm)
col10 = scalarMap.to_rgba(0.1)
col20 = scalarMap.to_rgba(1)


f1 = plt.figure(1, figsize=(8, 4), frameon=False)
ax = plt.subplot2grid((4, 8), (0, 0), rowspan=4, colspan=4)

plt.axis('equal')
plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

f1.canvas.draw()
ymin_ax, ymax_ax = ax.get_ylim()
xmin_ax, xmax_ax = ax.get_xlim()


# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)

# hipérbolas
plt.plot(x1, yu1, 'k-', lw=2)
plt.plot(x1, yd1, 'k-', lw=2)

plt.plot(ub[0, :], ub[1, :], 'r-', lw=2)
plt.plot(db[0, :], db[1, :], 'r-', lw=2)

# flechas
x0 = -2.7
idx = (np.abs(x1 - x0)).argmin()
plt.annotate("", xytext=(x1[idx - 1], yu1[idx - 1]), xycoords='data', xy=(x1[idx], yu1[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='black', shrink=0.002), zorder=-1)
x0 = 2.7
idx = (np.abs(x1 - x0)).argmin()
plt.annotate("", xytext=(x1[idx + 1], yd1[idx + 1]), xycoords='data', xy=(x1[idx], yd1[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='black', shrink=0.002), zorder=-1)
y0 = 2.7
idx = (np.abs(ub[1, :] - y0)).argmin()
plt.annotate("", xytext=(ub[0, idx - 1], ub[1, idx - 1]), xycoords='data', xy=(ub[0, idx], ub[1, idx]),
             textcoords='data', arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='r',
                                                edgecolor='r', shrink=0.002), zorder=-1)
y0 = -2.7
idx = (np.abs(db[1, :] - y0)).argmin()
plt.annotate("", xytext=(db[0, idx + 1], db[1, idx + 1]), xycoords='data', xy=(db[0, idx], db[1, idx]),
             textcoords='data', arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='r',
                                                edgecolor='r', shrink=0.002), zorder=-1)

# labels
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-0.3, ymax_ax, '$y$', fontsize=fontsize, ha='right', va='center')

plt.text(0.1, math.sqrt(-c1)-0.4, '$\sqrt{-c_1}$', fontsize=fontsize, ha='left', va='center')
plt.plot([0, ytl], [math.sqrt(-c1), math.sqrt(-c1)], 'k-', lw=1)


plt.axis('off')

#####################################

f2 = plt.figure(1, figsize=(8, 4), frameon=False)
ax = plt.subplot2grid((4, 8), (0, 4), rowspan=4, colspan=4)

plt.axis('equal')
plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

f1.canvas.draw()
ymin_ax, ymax_ax = ax.get_ylim()
xmin_ax, xmax_ax = ax.get_xlim()

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)

# imagen de las hipérbolas
plt.plot([c1, c1], [ymin, ymax], 'k-', lw=2)
plt.plot([xmin, xmax], [c2, c2], 'r-', lw=2)

# flechas
v0 = 2.5
d = 0.05
plt.annotate("", xytext=(c1, v0-d), xycoords='data', xy=(c1, v0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='black', shrink=0.002), zorder=-1)
u0 = 2.5
plt.annotate("", xytext=(u0 - d, c2), xycoords='data', xy=(u0, c2),
             textcoords='data', arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='r',
                                                edgecolor='r', shrink=0.002), zorder=-1)

# labels
plt.text(xmax_ax, xtm, '$u$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-0.3, ymax_ax, '$v$', fontsize=fontsize, ha='right', va='center')

plt.text(c1 - 0.15, xtm, '$c_1$', fontsize=fontsize, ha='right', va='baseline')
plt.text(0.15, c2 + 0.1, '$c_2$', fontsize=fontsize, ha='left', va='bottom')

plt.axis('off')


# save as pdf image
plt.savefig('exercise_14_06.pdf', bbox_inches='tight')


plt.show()
