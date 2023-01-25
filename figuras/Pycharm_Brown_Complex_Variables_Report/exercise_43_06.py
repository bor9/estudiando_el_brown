import numpy as np
import matplotlib.pyplot as plt

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


N = 400
x = np.linspace(0, 1, N)
y = np.power(x, 3) * np.sin(np.pi/x)

# valores maximos y minimos de los ejes
xmin = 0
xmax = 1.1
ymin = -0.4
ymax = 0.15


# axis parameters
dx = 0.05
xmin_ax = xmin - dx
xmax_ax = xmax
dy = 0
ymin_ax = ymin - dy
ymax_ax = ymax + dy

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.055
ytm = -0.04
# font size
fontsize = 14

fig = plt.figure(0, figsize=(5, 3), frameon=False)
ax = fig.add_subplot(111)

#plt.axis('equal')
plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

# horizontal and vertical ticks length
xtl, ytl = convert_display_to_data_coordinates(ax.transData, length=display_length)

# axis arrows
plt.annotate("", xytext=(xmin_ax, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))
plt.annotate("", xytext=(0, ymin_ax), xycoords='data', xy=(0, ymax_ax), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=6, headlength=8, facecolor='black', shrink=0.002))

plt.plot(x, y, color='k', lw=2)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# ticks
plt.plot([1, 1], [0, xtl], 'k', lw=1)
plt.plot([1/2, 1/2], [0, xtl], 'k', lw=1)
plt.plot([1/3, 1/3], [0, xtl], 'k', lw=1)
plt.plot([1/4, 1/4], [0, xtl], 'k', lw=1)
plt.plot([1/5, 1/5], [0, xtl], 'k', lw=1)
# ticks labels
dx = 0.01
plt.text(1+dx, xtm, '$1$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-0.02, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(1/2, xtm, r'$\frac{1}{2}$', fontsize=fontsize, ha='center', va='baseline')
plt.text(1/3+dx, xtm, r'$\frac{1}{3}$', fontsize=fontsize, ha='center', va='baseline')
plt.text(1/4, xtm, r'$\frac{1}{4}$', fontsize=fontsize, ha='center', va='baseline')
plt.text(1/5, xtm, r'$\frac{1}{5}$', fontsize=fontsize, ha='center', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_43_06.pdf', bbox_inches='tight')

plt.show()

