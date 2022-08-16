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

# parámetros
c1 = 1
c2 = 2
N = 300

#####################
# END OF PARAMETERS #
#####################

xmax = 2.5
xmin = -0.3
ymax = 2.5
ymin = -0.3

# axis parameters
dx = 0.2
xmax_ax = xmax + dx
xmin_ax = xmin
ymax_ax = ymax + dx
ymin_ax = ymin

y = np.linspace(ymin, ymax, N)
# hiperbolas
h1 = np.sqrt(np.square(y) + c1)
h2 = np.sqrt(np.square(y) + c2)
h1[h1 > xmax] = math.nan
h2[h2 > xmax] = math.nan

x = np.linspace(0.1, xmax, N)
h3 = c1 / (2 * x)
h4 = c2 / (2 * x)
h3[h3 > ymax] = math.nan
h4[h4 > ymax] = math.nan

# para el relleno de la región
cs = [c1, c2]
xs = np.zeros((len(cs) ** 2,))
idx = 0
for i in np.arange(len(cs)):
    for j in np.arange(len(cs)):
        a = cs[i]
        b = cs[j]
        r = np.sort(np.roots([4, -4 * a, -b ** 2]))
        xs[idx] = math.sqrt(r[1])
        idx += 1
xs = np.sort(xs)
n = 100
xx = np.linspace(xs[0], xs[-1], n)
yy1 = np.zeros((n, ))
yy2 = np.zeros((n, ))
idx = xx.searchsorted(xs[1], 'right')
yy2[0: idx] = np.sqrt(np.square(xx[0: idx]) - c1)
yy2[idx: n] = c2 / (2 * xx[idx: n])
idx = xx.searchsorted(xs[2], 'right')
yy1[0: idx] = c1 / (2 * xx[0: idx])
yy1[idx: n] = np.sqrt(np.square(xx[idx: n]) - c2)


# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.2
ytm = -0.1
# font size
fontsize = 14
# colors from coolwarm
cNorm = colors.Normalize(vmin=0, vmax=1)
scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cm.coolwarm)
col10 = scalarMap.to_rgba(0)
col11 = scalarMap.to_rgba(0.2)
col20 = scalarMap.to_rgba(1)
col21 = scalarMap.to_rgba(0.8)
col0 = scalarMap.to_rgba(0.5)


###############################################
###############################################

f0 = plt.figure(0, figsize=(8, 4), frameon=False)
ax = plt.subplot2grid((4, 8), (0, 0), rowspan=4, colspan=4)

plt.axis('equal')
plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

f0.canvas.draw()
ymin_ax, ymax_ax = ax.get_ylim()
xmin_ax, xmax_ax = ax.get_xlim()


# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

ax.fill_between(xx, yy1, yy2, color=col0)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)

# hipérbolas
plt.plot(h1, y, lw=2, color=col10)
plt.plot(h2, y, lw=2, color=col11)

plt.plot(x, h3, lw=2, color=col20)
plt.plot(x, h4, lw=2, color=col21)

# flechas
y0 = 1.5
idx = np.nanargmin(np.abs(h3 - y0))
plt.annotate("", xytext=(x[idx - 1], h3[idx - 1]), xycoords='data', xy=(x[idx], h3[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col20, edgecolor=col20, shrink=0.002),
             zorder=-1)
idx = np.nanargmin(np.abs(h4 - y0))
plt.annotate("", xytext=(x[idx - 1], h4[idx - 1]), xycoords='data', xy=(x[idx], h4[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col21, edgecolor=col21, shrink=0.002),
             zorder=-1)
idx = np.nanargmin(np.abs(y - y0))
plt.annotate("", xytext=(h1[idx - 1], y[idx - 1]), xycoords='data', xy=(h1[idx], y[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col10, edgecolor=col10, shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(h2[idx - 1], y[idx - 1]), xycoords='data', xy=(h2[idx], y[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col11, edgecolor=col11, shrink=0.002),
             zorder=-1)

# labels
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, ymax_ax, '$y$', fontsize=fontsize, ha='right', va='center')

plt.plot([math.sqrt(c1), math.sqrt(c1)], [0, xtl], 'k-', lw=1)
plt.plot([math.sqrt(c2), math.sqrt(c2)], [0, xtl], 'k-', lw=1)
plt.text(math.sqrt(c1)-0.03, xtm, '$1$', fontsize=fontsize, ha='right', va='baseline')
plt.text(math.sqrt(c2)-0.03, xtm, '$\sqrt{{{0:d}}}$'.format(c2), fontsize=fontsize, ha='right', va='baseline')
x0 = math.sqrt(c1/2)
ytm2 = -0.15
plt.plot([x0, x0], [0, c1 / (2 * x0)], 'k--', lw=1)
plt.text(ytm2, x0, '$\\frac{1}{\sqrt{2}}$', fontsize=fontsize, ha='center', va='center')
plt.plot([0, c1 / (2 * x0)], [x0, x0], 'k--', lw=1)
plt.text(x0, xtm, '$\\frac{1}{\sqrt{2}}$', fontsize=fontsize, ha='center', va='baseline')
x0 = math.sqrt(c2/2)
plt.plot([x0, x0], [0, c2 / (2 * x0)], 'k--', lw=1)
plt.plot([0, c2 / (2 * x0)], [x0, x0], 'k--', lw=1)
plt.text(ytm2, x0, '$1$', fontsize=fontsize, ha='center', va='center')


plt.axis('off')

################################

f0 = plt.figure(0, figsize=(8, 4), frameon=False)
ax = plt.subplot2grid((4, 8), (0, 4), rowspan=4, colspan=4)

plt.axis('equal')
plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

f0.canvas.draw()
ymin_ax, ymax_ax = ax.get_ylim()
xmin_ax, xmax_ax = ax.get_xlim()


# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002), zorder=-1)

# imagen de las hipérbolas
plt.plot([c1, c1], [ymin_ax, ymax], lw=2, color=col10)
plt.plot([c2, c2], [ymin_ax, ymax], lw=2, color=col11)
plt.plot([xmin_ax, xmax], [c1, c1], lw=2, color=col20)
plt.plot([xmin_ax, xmax], [c2, c2], lw=2, color=col21)
ax.fill_between([c1, c2], [c1, c1], [c2, c2], color=col0)

# flechas
x0 = 0.5
dx = 0.01
plt.annotate("", xytext=(x0 - dx, c1), xycoords='data', xy=(x0, c1), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col20, edgecolor=col20, shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(x0 - dx, c2), xycoords='data', xy=(x0, c2), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col21, edgecolor=col21, shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(c1, x0 - dx), xycoords='data', xy=(c1, x0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col10, edgecolor=col10, shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(c2, x0 - dx), xycoords='data', xy=(c2, x0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor=col11, edgecolor=col11, shrink=0.002),
             zorder=-1)


# labels
plt.text(xmax_ax, xtm, '$u$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, ymax_ax, '$v$', fontsize=fontsize, ha='right', va='center')

plt.text(c1-0.03, xtm, '${:d}$'.format(c1), fontsize=fontsize, ha='right', va='baseline')
plt.text(c2-0.03, xtm, '${:d}$'.format(c2), fontsize=fontsize, ha='right', va='baseline')

plt.text(ytm, c1, '${:d}$'.format(c1), fontsize=fontsize, ha='right', va='bottom')
plt.text(ytm, c2, '${:d}$'.format(c2), fontsize=fontsize, ha='right', va='bottom')

# xticks
plt.plot([c1, c1], [0, xtl], 'k-', lw=1)
plt.plot([c2, c2], [0, xtl], 'k-', lw=1)
# yticks
plt.plot([0, ytl], [c1, c1], 'k-', lw=1)
plt.plot([0, ytl], [c2, c2], 'k-', lw=1)


plt.axis('off')


# save as pdf image
plt.savefig('exercise_14_05.pdf', bbox_inches='tight')


plt.show()
