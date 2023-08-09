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
R = 3
rho = 1

# circulo |z|=1
N = 100
thetas = np.linspace(0, math.pi, N)
xR = R * np.cos(thetas)
yR = R * np.sin(thetas)
xrho = rho * np.cos(thetas)
yrho = rho * np.sin(thetas)


# valores maximos y minimos de los ejes
max_ax = 3.5
xmin = -max_ax
xmax = max_ax
ymin = -1.5
ymax = max_ax


# axis parameters
d = 0.5
xmin_ax = xmin - d
xmax_ax = xmax + d
ymin_ax = ymin - d
ymax_ax = ymax + d

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.5
ytm = -0.25
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 3), frameon=False)
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

# contorno
plt.plot(xR, yR, color='k', lw=2)
plt.plot(xrho, yrho, color='k', lw=2)
plt.plot([-R, -rho], [0, 0], color='k', lw=2)
plt.plot([rho, R], [0, 0], color='k', lw=2)

# flechas
idx = 25
plt.annotate("", xytext=(xR[idx - 4], yR[idx - 4]), xycoords='data', xy=(xR[idx], yR[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xR[idx] + 0.35, yR[idx], r'$C_R$', fontsize=fontsize, ha='left', va='center')
idx = 65
plt.annotate("", xytext=(xrho[idx + 10], yrho[idx + 10]), xycoords='data', xy=(xrho[idx], yrho[idx]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xrho[idx] - 0.6, yrho[idx] + 0.2, r'$C_\rho$', fontsize=fontsize, ha='center', va='center')

xa = -(R + rho) / 2 + 0.4
plt.annotate("", xytext=(xa-0.01, 0), xycoords='data', xy=(xa, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xa, 0.2, r'$L_2$', fontsize=fontsize, ha='right', va='bottom')
xa = (R + rho) / 2 + 0.4
plt.annotate("", xytext=(xa-0.01, 0), xycoords='data', xy=(xa, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xa, 0.2, r'$L_1$', fontsize=fontsize, ha='right', va='bottom')

# bordes del camino
ms = 8
plt.plot(-R, 0, 'k.', ms=ms)
plt.plot(-rho, 0, 'k.', ms=ms)
plt.plot(rho, 0, 'k.', ms=ms)
plt.plot(R, 0, 'k.', ms=ms)
i = 1.6
plt.plot(0, i, 'k.', ms=ms)

# punto y corte de rama
ms = 6
plt.plot(0, 0, 'o', markerfacecolor='w', markeredgecolor='r', ms=ms, zorder=10)
plt.plot([0, 0], [0, ymin_ax], 'r-', zorder=5)

# etiquetas de los contornos
plt.text(R, xtm, '$R$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-R, xtm, '$-R$', fontsize=fontsize, ha='center', va='baseline')
plt.text(rho, xtm, r'$\rho$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-rho, xtm, r'$-\rho$', fontsize=fontsize, ha='center', va='baseline')
plt.text(0.17, xtm, '$0$', fontsize=fontsize, ha='left', va='baseline')
plt.text(0.17, i, '$i$', fontsize=fontsize, ha='left', va='center')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

plt.axis('off')



# save as pdf image
plt.savefig('example_90_indented_path_branch_point.pdf', bbox_inches='tight')

plt.show()
