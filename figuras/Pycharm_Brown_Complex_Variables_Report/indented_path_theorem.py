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
xz0 = 7.5
yz0 = 0
rho = 4
R2 = 5.5
rho0 = 5

N = 100
thetas = np.linspace(0, 2*math.pi, N)
thetas_h = np.linspace(0, math.pi, N)

# region
xrho = xz0 + rho * np.cos(thetas_h)
yrho = yz0 + rho * np.sin(thetas_h)
xR2 = xz0 + R2 * np.cos(thetas)
yR2 = yz0 + R2 * np.sin(thetas)
xrho0 = xz0 + rho0 * np.cos(thetas)
yrho0 = yz0 + rho0 * np.sin(thetas)

# valores maximos y minimos de los ejes
xmin = -1
xmax = 15
ymin = -6
ymax = 6

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
fontsize = 14

fig = plt.figure(1, figsize=(5, 4), frameon=False)
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
plt.plot(xrho, yrho, 'k', lw=2)
plt.plot(xR2, yR2, 'k--', lw=1)
plt.plot(xrho0, yrho0, 'k', lw=1)

# punto z
ms = 6
plt.plot(xz0, yz0, 'o', markerfacecolor='w', markeredgecolor='k', ms=ms, zorder=10)

idx = 25
plt.plot([xz0, xrho[idx]], [yz0, yrho[idx]], 'k', lw=1)
plt.text((xrho[idx] + xz0) / 2 + 0.35, (yrho[idx] + yz0) / 2 - 0.2, r'$\rho$', fontsize=fontsize, ha='center',
         va='center')
# flecha
idx= 75
plt.annotate("", xytext=(xrho[idx], yrho[idx]), xycoords='data', xy=(xrho[idx-4], yrho[idx-4]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xrho[idx] + 0.7, yrho[idx] - 0.6, r'$C_\rho$', fontsize=fontsize, ha='center', va='center')

idx = 90
plt.plot([xz0, xR2[idx]], [yz0, yR2[idx]], 'k', lw=1)
k = 0.45
plt.text(xz0*(1 - k) + k * xR2[idx], yz0 * (1 - k) + k * yR2[idx] - 0.15, '$R_2$', fontsize=fontsize, ha='right',
         va='top')
idx = 55
plt.plot([xz0, xrho0[idx]], [yz0, yrho0[idx]], 'k', lw=1)
k = 0.45
plt.text(xz0*(1 - k) + k * xrho0[idx], yz0 * (1 - k) + k * yrho0[idx] - 0.5, r'$\rho_0$', fontsize=fontsize, ha='center',
         va='center')

# etiquetas
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')
dx = 0.2
plt.text(-dx, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

plt.text(xz0, yz0 - 0.2, '$x_0$', fontsize=fontsize, ha='center', va='top')

plt.axis('off')

# save as pdf image
plt.savefig('indented_path_theorem.pdf', bbox_inches='tight')

plt.show()
