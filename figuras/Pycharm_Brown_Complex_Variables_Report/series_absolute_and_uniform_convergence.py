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
xz0 = 6
yz0 = 3.5
R1 = 3
R = 5
xz = 4.6
yz = 5

N = 100
thetas = np.linspace(0, 2*math.pi, N)

# region
xR1 = xz0 + R1 * np.cos(thetas)
yR1 = yz0 + R1 * np.sin(thetas)
xR2 = xz0 + R * np.cos(thetas)
yR2 = yz0 + R * np.sin(thetas)

# valores maximos y minimos de los ejes
xmin = -2
xmax = 12
ymin = xmin
ymax = 10

# axis parameters
d = 0.5
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.76
ytm = -0.4
# font size
fontsize = 12

############# Convergencia uniforme #############
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

# dominio
plt.plot(xR1, yR1, 'k--', lw=1)

# puntos R1 y R2
ms = 7
plt.plot(xz, yz, 'k.', ms=ms)
plt.plot(xz0, yz0, 'k.', ms=ms)

idx = 5
plt.plot([xz0, xR1[idx]], [yz0, yR1[idx]], 'k', lw=1)
plt.plot(xR1[idx], yR1[idx], 'k.', ms=ms)
plt.text(xR1[idx] + 0.65, yR1[idx] + 0.2, '$z_1$', fontsize=fontsize, ha='center', va='center')
plt.text((xR1[idx] + xz0) / 2 - 0.35, (yR1[idx] + yz0) / 2 + 0.5, '$R_1$', fontsize=fontsize, ha='center', va='center')

# etiquetas
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.text(xz+0.4, yz+0.4, '$z$', fontsize=fontsize, ha='center', va='center')
plt.text(xz0, yz0-0.2, '$z_0$', fontsize=fontsize, ha='center', va='top')

plt.axis('off')

# save as pdf image
plt.savefig('series_absolute_convergence.pdf', bbox_inches='tight')


############# Convergencia uniforme #############
fig = plt.figure(2, figsize=(4, 4), frameon=False)
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

# dominio
plt.plot(xR1, yR1, 'k', lw=1)
plt.plot(xR2, yR2, 'k--', lw=1)

# puntos R1 y R2
ms = 7
plt.plot(xz, yz, 'k.', ms=ms)
plt.plot(xz0, yz0, 'k.', ms=ms)

idx = 5
plt.plot([xz0, xR1[idx]], [yz0, yR1[idx]], 'k', lw=1)
plt.plot(xR1[idx], yR1[idx], 'k.', ms=ms)
plt.text(xR1[idx] + 0.65, yR1[idx] + 0.2, '$z_1$', fontsize=fontsize, ha='center', va='center')
plt.text((xR1[idx] + xz0) / 2 - 0.35, (yR1[idx] + yz0) / 2 + 0.5, '$R_1$', fontsize=fontsize, ha='center', va='center')
idx = 90
plt.plot([xz0, xR2[idx]], [yz0, yR2[idx]], 'k', lw=1)
k = 0.8
plt.text(xz0*(1 - k) + k * xR2[idx], yz0 * (1 - k) + k * yR2[idx], '$R$', fontsize=fontsize, ha='left', va='bottom')


# etiquetas
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.text(xz+0.4, yz+0.4, '$z$', fontsize=fontsize, ha='center', va='center')
plt.text(xz0, yz0-0.2, '$z_0$', fontsize=fontsize, ha='center', va='top')

plt.axis('off')

# save as pdf image
plt.savefig('series_uniform_convergence.pdf', bbox_inches='tight')

plt.show()
