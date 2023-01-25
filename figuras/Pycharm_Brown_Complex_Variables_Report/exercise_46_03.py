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


# valores maximos y minimos de los ejes
xmin = 0
xmax = 1.4
ymin = 0
ymax = 1.4


# axis parameters
dx = 0.2
xmin_ax = xmin - dx
xmax_ax = xmax
dy = 0.2
ymin_ax = ymin - dy
ymax_ax = ymax

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.15
ytm = -0.075
# font size
fontsize = 14

fig = plt.figure(0, figsize=(3, 3), frameon=False)
ax = fig.add_subplot(111)

plt.axis('equal')
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

# z = x
plt.plot([0, 0], [1, 0], color='k', lw=2)
# z = 1 + iy
plt.plot([1, 0], [1, 1], color='k', lw=2)
# z = x + i
plt.plot([1, 1], [0, 1], color='k', lw=2)
# z = iy
plt.plot([0, 1], [0, 0], color='k', lw=2)

# flechas
x_arr = 0.5
dxa = 0.01
plt.annotate("", xytext=(x_arr - dxa, 0), xycoords='data', xy=(x_arr, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(1, x_arr - dxa), xycoords='data', xy=(1, x_arr), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(x_arr - dxa, 1), xycoords='data', xy=(x_arr, 1), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.annotate("", xytext=(0, x_arr - dxa), xycoords='data', xy=(0, x_arr), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
# puntos en los extremos
ms = 9
plt.plot(0, 0, 'k.', ms=ms)
plt.plot(1, 0, 'k.', ms=ms)
plt.plot(1, 1, 'k.', ms=ms)
plt.plot(0, 1, 'k.', ms=ms)

# etiquetas de los contornos
mm = 0.08
plt.text(x_arr, -mm, '$C_1$', fontsize=fontsize, ha='right', va='top')
plt.text(1 + mm, x_arr, '$C_2$', fontsize=fontsize, ha='left', va='top')
plt.text(x_arr, 1 + mm, '$C_3$', fontsize=fontsize, ha='right', va='bottom')
plt.text(-mm, x_arr, '$C_4$', fontsize=fontsize, ha='right', va='top')


# etiquetas de los puntos
h = 0.1
plt.text(1, 1 + h, '$1+i$', fontsize=fontsize, ha='center', va='baseline')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# ticks
plt.plot([0, ytl], [1, 1], 'k', lw=1)
plt.plot([1, 1], [0, xtl], 'k', lw=1)
plt.plot([2, 2], [0, xtl], 'k', lw=1)
# ticks labels
plt.text(1, xtm, '$1$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, 1, '$i$', fontsize=fontsize, ha='right', va='center')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')


plt.axis('off')

# save as pdf image
plt.savefig('exercise_46_03.pdf', bbox_inches='tight')

plt.show()

