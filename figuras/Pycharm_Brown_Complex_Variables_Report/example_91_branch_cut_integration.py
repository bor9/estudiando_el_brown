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


def arrow_construction(xc, yc, len, dir):
    # largo de la punta de la flecha
    f = 0.4
    lpa = 0.4 * f
    # altura de la punta de la flecha
    apa = 0.15 * f
    dd = lpa/2
    if dir=='lu':
        # extremos de la flecha
        p = xc - len / 2
        xext = [p + dd, xc + len / 2]
        yext = [yc, yc]
        # triángulo
        xt = [p, p + lpa, p + lpa]
        yt = [yc, yc, yc + apa]
    elif dir=='ld':
        # extremos de la flecha
        p = xc - len / 2
        xext = [p + dd, xc + len / 2]
        yext = [yc, yc]
        # triángulo
        xt = [p, p + lpa, p + lpa]
        yt = [yc, yc, yc - apa]
    elif dir=='ru':
        # extremos de la flecha
        p = xc + len / 2
        xext = [xc - len / 2, p - dd]
        yext = [yc, yc]
        # triángulo
        xt = [p, p - lpa, p - lpa]
        yt = [yc, yc, yc + apa]
    elif dir=='rd':
        # extremos de la flecha
        p = xc + len / 2
        xext = [xc - len / 2, p - dd]
        yext = [yc, yc]
        # triángulo
        xt = [p, p - lpa, p - lpa]
        yt = [yc, yc, yc - apa]
    elif dir=='ul':
        # extremos de la flecha
        p = yc + len / 2
        xext = [xc, xc]
        yext = [yc - len / 2, p - dd]
        # triángulo
        xt = [xc, xc, xc - apa]
        yt = [p - lpa, p, p - lpa]
    elif dir=='ur':
        # extremos de la flecha
        p = yc + len / 2
        xext = [xc, xc]
        yext = [yc - len / 2, p - dd]
        # triángulo
        xt = [xc, xc, xc + apa]
        yt = [p - lpa, p, p - lpa]
    elif dir=='dl':
        # extremos de la flecha
        p = yc - len / 2
        xext = [xc, xc]
        yext = [p + dd, yc + len / 2]
        # triángulo
        xt = [xc, xc, xc - apa]
        yt = [p, p + lpa, p + lpa]
    elif dir=='dr':
        # extremos de la flecha
        p = yc - len / 2
        xext = [xc, xc]
        yext = [p + dd, yc + len / 2]
        # triángulo
        xt = [xc, xc, xc + apa]
        yt = [p, p + lpa, p + lpa]
    return xext, yext, xt, yt


# parámetros
R = 1.3
rho = 0.6

# circulo |z|=1
N = 200
thetas = np.linspace(0, 2 * math.pi, N)
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
xtm = -0.23
ytm = -0.12
# font size
fontsize = 14

fig = plt.figure(0, figsize=(4, 4), frameon=False)
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
plt.plot([0, xmax_ax-0.15], [0, 0], 'r-', zorder=5)

# flechas de los contornos
nc = 70
dn = 3
plt.annotate("", xy=(xR[nc], yR[nc]), xycoords='data', xytext=(xR[nc - dn], yR[nc - dn]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
plt.text(xR[nc] + 0.1, yR[nc], r'$C_R$', fontsize=fontsize, ha='left', va='top')
nc = 85
dn = 10
plt.annotate("", xy=(xrho[nc - dn], yrho[nc - dn]), xycoords='data', xytext=(xrho[nc], yrho[nc]), textcoords='data',
             arrowprops=dict(width=0.1, headwidth=5, headlength=10, facecolor='k', edgecolor='k', shrink=0.002),
             zorder=-1)
# etiqueta del contorno
plt.text(xrho[nc], yrho[nc] + 0.1, r'$C_\rho$', fontsize=fontsize, ha='right', va='bottom')

da = 0.06
xext, yext, xt, yt = arrow_construction((rho + R) / 2, -da, (rho + R) / 5, 'ld')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
plt.text((rho + R) / 2, -0.17, '$L_2$', fontsize=fontsize, ha='center', va='top')
xext, yext, xt, yt = arrow_construction((rho + R) / 2, da, (rho + R) / 5, 'ru')
plt.plot(xext, yext, 'k', lw=1)
plt.fill(xt, yt, facecolor='k', edgecolor='k')
plt.text((rho + R) / 2, 0.15, '$L_1$', fontsize=fontsize, ha='center', va='bottom')

# etiquetas de los ejes
plt.text(xmax_ax, xtm, '$x$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$y$', fontsize=fontsize, ha='left', va='center')

# circle labels
plt.text(R + 0.05, xtm, '$R$', fontsize=fontsize, ha='left', va='baseline')
plt.text(rho + 0.05, xtm, r'$\rho$', fontsize=fontsize, ha='left', va='baseline')
plt.text(-0.07, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')
plt.text(-1, xtm, '$-1$', fontsize=fontsize, ha='center', va='baseline')

plt.axis('off')

# save as pdf image
plt.savefig('example_91_branch_cut_integration.pdf', bbox_inches='tight')

plt.show()
