import matplotlib.pyplot as plt
import numpy as np
import math

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
r = 1

# circulo |z|=1
N = 200
thetas = np.linspace(0, 2 * math.pi, N)
xc = r * np.cos(thetas)
yc = r * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 5
xmin = -max_ax
xmax = max_ax
ymin = -max_ax
ymax = max_ax

dx = 0.5
# axis parameters
xmin_ax = xmin - dx
xmax_ax = xmax + dx
ymin_ax = ymin - dx
ymax_ax = ymax + dx

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.9
ytm = -0.5
# font size
fontsize = 12

fig = plt.figure(0, figsize=(6, 6), frameon=False)
#######
# (c) #
#######
ax = plt.subplot2grid((8, 8), (0, 0), rowspan=4, colspan=4)

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

# circulo |z|=1
plt.plot(xc, yc, color='k', lw=2)

# puntos z = -1+i y z = -1-i
ms = 7
g = (0.7, 0.7, 0.7)
plt.plot(-1, 1, 'k.', ms=ms, zorder=5)
plt.plot(-1, -1, 'k.', ms=ms, zorder=5)
plt.plot([-1, 0], [1, 1], color=g, ls='--', lw=1)
plt.plot([-1, 0], [-1, -1], color=g, ls='--', lw=1)
plt.plot([-1, -1], [0, 1], color=g, ls='--', lw=1)
plt.plot([-1, -1], [0, -1], color=g, ls='--', lw=1)

# etiquetas de los contornos
theta = math.pi / 4 * 0.9
r3 = 1.1
xl = r3 * math.cos(theta)
yl = r3 * math.sin(theta)
plt.text(xl, yl, r'$C$', fontsize=fontsize, ha='left', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(1.1, xtm, '$1$', fontsize=fontsize, ha='left', va='baseline')

plt.text(-1.1, 1.1, '$-1+i$', fontsize=fontsize, ha='right', va='bottom')
plt.text(-1.1, -1.1, '$-1-i$', fontsize=fontsize, ha='right', va='top')

plt.text(xmin_ax, ymax_ax, '$(c)$', fontsize=fontsize, ha='left', va='top')

plt.axis('off')

#######
# (d) #
#######
ax = plt.subplot2grid((8, 8), (0, 4), rowspan=4, colspan=4)

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

# circulo |z|=1
plt.plot(xc, yc, color='k', lw=2)

# puntos z = -1+i y z = -1-i
ms = 7
plt.plot(0, np.pi/2, 'k.', ms=ms, zorder=5)
plt.plot(0, 3 * np.pi/2, 'k.', ms=ms, zorder=5)
plt.plot(0, -np.pi/2, 'k.', ms=ms, zorder=5)
plt.plot(0, -3 * np.pi/2, 'k.', ms=ms, zorder=5)


# etiquetas de los contornos
theta = math.pi / 4 * 0.9
r3 = 1.1
xl = r3 * math.cos(theta)
yl = r3 * math.sin(theta)
plt.text(xl, yl, r'$C$', fontsize=fontsize, ha='left', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(1.1, xtm, '$1$', fontsize=fontsize, ha='left', va='baseline')

plt.text(-0.4, np.pi/2, '$i\pi/2$', fontsize=fontsize, ha='right', va='center')
plt.text(-0.4, 3*np.pi/2, '$i3\pi/2$', fontsize=fontsize, ha='right', va='center')
plt.text(-0.4, -np.pi/2, '$-i\pi/2$', fontsize=fontsize, ha='right', va='center')
plt.text(-0.4, -3*np.pi/2, '$-i3\pi/2$', fontsize=fontsize, ha='right', va='center')


plt.text(xmin_ax, ymax_ax, '$(d)$', fontsize=fontsize, ha='left', va='top')

plt.axis('off')

#######
# (e) #
#######
ax = plt.subplot2grid((8, 8), (4, 0), rowspan=4, colspan=4)

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

# circulo |z|=1
plt.plot(xc, yc, color='k', lw=2)

# puntos z = -1+i y z = -1-i
ms = 7
plt.plot(np.pi/2, 0, 'k.', ms=ms, zorder=5)
plt.plot(3 * np.pi/2, 0, 'k.', ms=ms, zorder=5)
plt.plot(-np.pi/2, 0, 'k.', ms=ms, zorder=5)
plt.plot(-3 * np.pi/2, 0, 'k.', ms=ms, zorder=5)

# etiquetas de los contornos
theta = math.pi / 4 * 0.9
r3 = 1.1
xl = r3 * math.cos(theta)
yl = r3 * math.sin(theta)
plt.text(xl, yl, r'$C$', fontsize=fontsize, ha='left', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.text(np.pi/2+0.2, xtm, '$\pi/2$', fontsize=fontsize, ha='center', va='baseline')
plt.text(3*np.pi/2-0.7, xtm, '$3\pi/2$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-np.pi/2-0.5, xtm, '$-\pi/2$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-3*np.pi/2, xtm, '$-3\pi/2$', fontsize=fontsize, ha='center', va='baseline')

plt.text(xmin_ax, ymax_ax, '$(e)$', fontsize=fontsize, ha='left', va='top')

plt.axis('off')


#######
# (f) #
#######
ax = plt.subplot2grid((8, 8), (4, 4), rowspan=4, colspan=4)

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

# circulo |z|=1
plt.plot(xc, yc, color='k', lw=2)

ms = 6
plt.plot(-2, 0, 'o', markerfacecolor='w', markeredgecolor='r', ms=ms, zorder=10)
plt.plot([xmin_ax, -2], [0, 0], 'r', ms=ms, zorder=9)


# etiquetas de los contornos
theta = math.pi / 4 * 0.9
r3 = 1.1
xl = r3 * math.cos(theta)
yl = r3 * math.sin(theta)
plt.text(xl, yl, r'$C$', fontsize=fontsize, ha='left', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(1.1, xtm, '$1$', fontsize=fontsize, ha='left', va='baseline')
plt.text(-2, xtm, '$-2$', fontsize=fontsize, ha='center', va='baseline')


plt.plot([1, 1], [0, xtl], 'k', lw=1)

plt.text(xmin_ax, ymax_ax, '$(f)$', fontsize=fontsize, ha='left', va='top')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_53_01_f.pdf', bbox_inches='tight')

plt.show()
