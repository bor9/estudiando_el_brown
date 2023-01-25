import matplotlib.pyplot as plt
import math
import numpy as np

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


# valores maximos y minimos de los ejes
xmin = 0
xmax = 3.2
ymin = -1
ymax = 3


# axis parameters
d = 0.2
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.4
ytm = -0.1
# font size
fontsize = 14


N = 100
x = np.linspace(0, math.pi, N)
f1 = np.cos(x)
y = np.linspace(0, 1, N)
f2 = np.exp(y)

fig = plt.figure(1, figsize=(7, 3), frameon=False)
ax = plt.subplot2grid((4, 6), (0, 2), rowspan=4, colspan=4)

plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))

plt.plot(x, f1, 'k-', lw=1.5)

xtm2 = 0.25
# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$y$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$\operatorname{cos}y$', fontsize=fontsize, ha='left', va='center')
plt.text(-0.07, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(-0.07, 1, '$1$', fontsize=fontsize, ha='right', va='center')
plt.text(-0.07, -1, '$-1$', fontsize=fontsize, ha='right', va='center')
plt.text(math.pi, xtm2, '$\pi$', fontsize=fontsize, ha='center', va='baseline')
plt.text(math.pi/2, xtm2, '$\pi/2$', fontsize=fontsize, ha='center', va='baseline')

plt.plot([math.pi, math.pi], [-1, 0], 'k--', lw=1)
plt.plot([0, math.pi], [-1, -1], 'k--', lw=1)

plt.plot([math.pi, math.pi], [0, xtl], 'k-', lw=1)

plt.axis('off')


xmax_ax = 1.3
ax = plt.subplot2grid((4, 6), (0, 0), rowspan=4, colspan=2)

plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))

plt.plot(y, f2, 'k-', lw=1.5)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$e^x$', fontsize=fontsize, ha='left', va='center')
plt.text(-0.06, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(-0.06, 1, '$1$', fontsize=fontsize, ha='right', va='center')
plt.text(-0.06, np.exp(1), '$e$', fontsize=fontsize, ha='right', va='center')
plt.text(1, xtm, '$1$', fontsize=fontsize, ha='center', va='baseline')

plt.plot([1, 1], [0, np.exp(1)], 'k--', lw=1)
plt.plot([0, 1], np.exp([1, 1]), 'k--', lw=1)

plt.plot([0, ytl], [1, 1], 'k-', lw=1)

plt.axis('off')

plt.savefig('exercise_59_06_graphs.pdf', bbox_inches='tight')

plt.show()
