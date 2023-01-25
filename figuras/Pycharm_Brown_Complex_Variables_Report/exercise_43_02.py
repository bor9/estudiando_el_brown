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
theta = 37 * math.pi / 180
r = 2

# circulo |z=2|
N = 100
thetas = np.linspace(-math.pi/2, math.pi/2, N)
xc = r * np.cos(thetas)
yc = r * np.sin(thetas)
# x e y del punto en C
zy = 2 * math.sin(theta)
zx = math.sqrt(r**2 - zy**2)


# valores maximos y minimos de los ejes
xmin = 0
xmax = 2.4
ymin = -xmax
ymax = xmax


# axis parameters
dx = 0.15
xmin_ax = xmin - dx
xmax_ax = xmax
dy = 0.15
ymin_ax = ymin
ymax_ax = ymax

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.2
ytm = -0.1
# font size
fontsize = 14

fig = plt.figure(0, figsize=(5, 6), frameon=False)
ax = fig.add_subplot(111)

#plt.axis('equal')
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

# circulo |z|=2
plt.plot(xc, yc, color='k', lw=2)
# triángulo
plt.plot([0, zx], [0, 0], color='k', lw=2)
plt.plot([zx, zx], [0, zy], color='k', lw=2)
plt.plot([0, zx], [0, zy], color='k', lw=2)
# punto z
ms = 9
plt.plot(zx, zy, 'k.', ms=ms)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# labels
plt.text(zx / 2, -0.25, r'$x=\sqrt{4-y^2}$', fontsize=fontsize, ha='center', va='baseline')
plt.text(zx + 0.075, zy / 2, '$y$', fontsize=fontsize, ha='left', va='center')
plt.text(zx /2 - 0.03, zy / 2 + 0.03, '${0:d}$'.format(r), fontsize=fontsize, ha='right', va='bottom')
plt.text(zx + 0.05, zy + 0.03, '$z$', fontsize=fontsize, ha='left', va='bottom')

# angulo theta
rr = 0.35
tt = np.linspace(0, theta, 40)
plt.plot(rr * np.cos(tt), rr * np.sin(tt), color='k', lw=1)
rr2 = rr + 0.07
plt.text(rr2 * np.cos(theta / 2), rr2 * np.sin(theta / 2), r'$\theta$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(r + 0.07, xtm, '${0:d}$'.format(r), fontsize=fontsize, ha='left', va='baseline')
plt.text(ytm, r, '${0:d}$'.format(r), fontsize=fontsize, ha='right', va='center')
plt.text(ytm, -r, '${0:d}$'.format(-r), fontsize=fontsize, ha='right', va='center')

plt.axis('off')

# save as pdf image
plt.savefig('exercise_43_02.pdf', bbox_inches='tight')

plt.show()
