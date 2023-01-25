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


# parámetros
a = 3
b = 1.5

# valores maximos y minimos de los ejes
max_ax = 3.5
xmin = -max_ax
xmax = max_ax
ymin = 0
ymax = 2


# axis parameters
d = 1
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.55
ytm = -0.3
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 2), frameon=False)
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

# camino rectangular
plt.plot([-a, a], [0, 0], color='k', lw=2)
plt.plot([-a, a], [b, b], color='k', lw=2)
plt.plot([a, a], [0, b], color='k', lw=2)
plt.plot([-a, -a], [0, b], color='k', lw=2)

# flechas
da = 0.3
dd = 0.01
ar = a/2+da
plt.annotate("", xytext=(ar-dd, 0), xycoords='data', xy=(ar, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
ar = b/2+da
plt.annotate("", xytext=(a, ar-dd), xycoords='data', xy=(a, ar), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
ar = -a/2-da
plt.annotate("", xytext=(ar+dd, b), xycoords='data', xy=(ar, b), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)
ar = b/2-da
plt.annotate("", xytext=(-a, ar+dd), xycoords='data', xy=(-a, ar), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=10)

# vértices
ms = 7
plt.plot(a, 0, 'k.', ms=ms)
plt.plot(-a, 0, 'k.', ms=ms)
plt.plot(a, b, 'k.', ms=ms)
plt.plot(-a, b, 'k.', ms=ms)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='center', va='baseline')


plt.text(a, xtm, '$a$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-a, xtm, '$-a$', fontsize=fontsize, ha='center', va='baseline')
plt.text(a, b+0.3, '$a+ib$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-a, b+0.3, '$-a+ib$', fontsize=fontsize, ha='center', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_53_04.pdf', bbox_inches='tight')

plt.show()
