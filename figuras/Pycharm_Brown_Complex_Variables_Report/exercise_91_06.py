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


# parámetros
R = 1.3
rho = 0.6
theta0 = 3 * np.pi / 2 - np.pi / 6

# circulo |z|=1
N = 200
thetas = np.linspace(0, theta0, N)
# contorno
xrho = rho * np.cos(thetas)
yrho = rho * np.sin(thetas)
# dominio
xR = R * np.cos(thetas)
yR = R * np.sin(thetas)

# valores maximos y minimos de los ejes
max_ax = 1.8
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
xtm = -0.24
ytm = -0.12
# font size
fontsize = 14

fig = plt.figure(0, figsize=(8, 4), frameon=False)
ax = plt.subplot2grid((4, 8), (0, 0), rowspan=4, colspan=4)

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
plt.plot(xrho, yrho, color='k', lw=2)
# dominio
plt.plot(xR, yR, color='k', lw=2)
# puntos
ms = 9
# polo
plt.plot(-1, 0, 'k.', ms=ms)
plt.plot(rho, 0, 'k.', ms=ms, zorder=10)
plt.plot(R, 0, 'k.', ms=ms, zorder=10)

# punto y corte de rama
ms = 6
plt.plot(0, 0, 'o', markerfacecolor='w', markeredgecolor='r', ms=ms, zorder=10)
plt.plot([0, 0], [0, ymin_ax-0.15], 'r-', zorder=5)

# L
idx = -1
plt.plot([xR[idx], xrho[idx]], [yR[idx], yrho[idx]], color='k', lw=2)
xf = (xR[idx] + xrho[idx]) / 1.9
yf = (yR[idx] + yrho[idx]) / 1.9
m = (yR[idx] - yrho[idx]) / (xR[idx] - xrho[idx])
n = yR[idx] - m * xR[idx]
dx = 0.1
plt.annotate("", xytext=(xf, yf), xycoords='data', xy=(xf + dx, m * (xf + dx) + n), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xf + dx - 0.15, yf + dx + 0.05, '$L$', fontsize=fontsize, ha='right', va='center')

plt.plot([rho, R], [0, 0], color='k', lw=2)
xf = (rho + R) / 1.9
plt.annotate("", xytext=(xf, 0), xycoords='data', xy=(xf + dx, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)


# flechas de los contornos
nc = 110
dn = 3
plt.annotate("", xy=(xR[nc], yR[nc]), xycoords='data', xytext=(xR[nc - dn], yR[nc - dn]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xR[nc], yR[nc] + 0.3, r'$\Gamma_R$', fontsize=fontsize, ha='center', va='center')
nc = 100
dn = 10
plt.annotate("", xy=(xrho[nc - dn], yrho[nc - dn]), xycoords='data', xytext=(xrho[nc], yrho[nc]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
# etiqueta del contorno
plt.text(xrho[nc], yrho[nc] + 0.1, r'$\Gamma_\rho$', fontsize=fontsize, ha='right', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(R, xtm, '$R$', fontsize=fontsize, ha='center', va='baseline')
plt.text(rho, xtm, r'$\rho$', fontsize=fontsize, ha='center', va='baseline')
plt.text(0.07, xtm, '$0$', fontsize=fontsize, ha='left', va='baseline')
plt.text(-1, xtm, '$-1$', fontsize=fontsize, ha='center', va='baseline')

plt.plot([0, xrho[-1]], [0, yrho[-1]], 'k--', lw=1)
# angle
r = 0.18
xr = r * np.cos(thetas)
yr = r * np.sin(thetas)
plt.plot(xr, yr, 'k--', lw=1)
plt.text(-0.2 * np.cos(np.pi/4), 0.2 * np.cos(np.pi/4), r'$\theta_0$', fontsize=fontsize, ha='right', va='bottom')

plt.axis('off')

############################################################################
############################################################################
############################################################################

N = 100
thetas = np.linspace(theta0, 2 * np.pi, N)
# contorno
xrho = rho * np.cos(thetas)
yrho = rho * np.sin(thetas)
# dominio
xR = R * np.cos(thetas)
yR = R * np.sin(thetas)

ax = plt.subplot2grid((4, 8), (0, 4), rowspan=4, colspan=4)

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
plt.plot(xrho, yrho, color='k', lw=2)
# dominio
plt.plot(xR, yR, color='k', lw=2)
# puntos
ms = 9
# polo
plt.plot(rho, 0, 'k.', ms=ms, zorder=10)
plt.plot(R, 0, 'k.', ms=ms, zorder=10)

# punto y corte de rama
ms = 6
plt.plot(0, 0, 'o', markerfacecolor='w', markeredgecolor='r', ms=ms, zorder=10)
plt.plot([0, 0], [0, ymax_ax-0.15], 'r-', zorder=5)

# L
idx = 0
plt.plot([xR[idx], xrho[idx]], [yR[idx], yrho[idx]], color='k', lw=2)
xf = (xR[idx] + xrho[idx]) / 1.8
yf = (yR[idx] + yrho[idx]) / 1.8
m = (yR[idx] - yrho[idx]) / (xR[idx] - xrho[idx])
n = yR[idx] - m * xR[idx]
dx = 0.1
plt.annotate("", xy=(xf, yf), xycoords='data', xytext=(xf + dx, m * (xf + dx) + n), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xf + dx - 0.15, yf + dx + 0.05, '$-L$', fontsize=fontsize, ha='right', va='center')

plt.plot([rho, R], [0, 0], color='k', lw=2)
xf = (rho + R) / 2.2
plt.annotate("", xy=(xf, 0), xycoords='data', xytext=(xf + dx, 0), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)


# flechas de los contornos
nc = 60
dn = 3
plt.annotate("", xy=(xR[nc], yR[nc]), xycoords='data', xytext=(xR[nc - dn], yR[nc - dn]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xR[nc] + 0.1, yR[nc] - 0.2, r'$\gamma_R$', fontsize=fontsize, ha='center', va='center')
nc = 60
dn = 10
plt.annotate("", xy=(xrho[nc - dn], yrho[nc - dn]), xycoords='data', xytext=(xrho[nc], yrho[nc]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
# etiqueta del contorno
plt.text(xrho[nc] + 0.15, yrho[nc] - 0.15, r'$\gamma_\rho$', fontsize=fontsize, ha='center', va='center')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
xtm2 = 0.15
plt.text(R, xtm2, '$R$', fontsize=fontsize, ha='center', va='baseline')
plt.text(rho, xtm2, r'$\rho$', fontsize=fontsize, ha='center', va='baseline')
plt.text(0.07, xtm, '$0$', fontsize=fontsize, ha='left', va='baseline')

# angle
plt.plot([0, xrho[0]], [0, yrho[0]], 'k--', lw=1)
thetas = np.linspace(0, theta0, N)
r = 0.18
xr = r * np.cos(thetas)
yr = r * np.sin(thetas)
plt.plot(xr, yr, 'k--', lw=1)
plt.text(-0.2 * np.cos(np.pi/4), 0.2 * np.cos(np.pi/4), r'$\theta_0$', fontsize=fontsize, ha='right', va='bottom')


plt.axis('off')


# save as pdf image
plt.savefig('exercise_91_06.pdf', bbox_inches='tight')

plt.show()
