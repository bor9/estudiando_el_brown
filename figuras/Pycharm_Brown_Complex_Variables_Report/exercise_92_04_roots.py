import matplotlib.pyplot as plt
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


N = 300
a = np.linspace(-1, 1, N)
z = (-1 + np.sqrt(1 - a ** 2)) / a

# valores maximos y minimos de los ejes
max_ax = 1.3
xmin = -max_ax
xmax = max_ax
ymin = -max_ax
ymax = max_ax


# axis parameters
xmin_ax = xmin
xmax_ax = xmax
ymin_ax = ymin
ymax_ax = ymax

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.25
ytm = -0.1
# font size
fontsize = 14

fig = plt.figure(0, figsize=(5, 3), frameon=False)
ax = fig.add_subplot(111)

plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))

plt.plot(a, z, color='k', lw=2)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$a$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$z_1$', fontsize=fontsize, ha='left', va='center')

# etiquetas de los ejes
plt.text(ytm/2, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(1, xtm, '$1$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-1, xtm, '$-1$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm/2, -1, '$-1$', fontsize=fontsize, ha='right', va='center')
plt.text(ytm/2, 1, '$1$', fontsize=fontsize, ha='right', va='center')

# ticks
plt.plot([1, 1], [0, xtl], 'k-', lw=1)
plt.plot([-1, -1], [0, xtl], 'k-', lw=1)
plt.plot([0, ytl], [1, 1], 'k-', lw=1)
plt.plot([0, ytl], [-1, -1], 'k-', lw=1)

plt.axis('off')

# save as pdf image
plt.savefig('exercise_92_04_roots.pdf', bbox_inches='tight')

plt.show()
