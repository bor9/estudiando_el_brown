import numpy as np
import matplotlib.pyplot as plt

__author__ = 'ernesto'

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preview'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

xmin_ax = -2
xmax_ax = 4
ymin_ax = -1.5
ymax_ax = 1.5

# círculo
# mitad superior
phi = np.linspace(0, np.pi, 100)
r = 1
xc_sup = r * np.cos(phi)
yc_sup = r * np.sin(phi)
xc_inf = r * np.cos(-phi)
yc_inf = r * np.sin(-phi)

# elipse
a = r
b = 0.5
xe_inf = a * np.cos(-phi)
ye_inf = b * np.sin(-phi)
xe_sup = a * np.cos(phi)
ye_sup = b * np.sin(phi)

# coordenadas del plano
xp_ii = -0.8
yp_ii = -1.4
xp_is = xmin_ax
yp_is = -yp_ii
xp_ds = xmax_ax - (xp_ii - xp_is)
yp_ds = -yp_ii
xp_di = xmax_ax
yp_di = yp_ii

# pendiente del borde del plano
m = (yp_ds - yp_di) / (xp_ds - xp_di)
# coordenadas de la intersección del eje y con el círculo
x1 = -r / np.sqrt(1 + m ** 2)
y1 = m * x1
# coordenadas de la intersección del eje y con la elipse
x2 = a * b / np.sqrt((a ** 2) * (m ** 2) + b ** 2)
y2 = m * x2

# parámetros de la figura
fontsize = 14
lw = 1.5

fig = plt.figure(0, figsize=(9, 4.5), frameon=False)

ax = plt.subplot2grid((4, 8), (0, 0), rowspan=4, colspan=8)

plt.axis('equal')
plt.xlim(xmin_ax, xmax_ax)
plt.ylim(ymin_ax, ymax_ax)

# ejes de coordenadas
# punta de la flecha del eje y
xap = -(xp_ii - xp_is) / 2
yap = yp_is
dy1 = 0.09
dx1 = 0.04
ya = yap - dy1
xa = ya / m
xay = [xap, xa - dx1, xa + dx1]
yay = [yap, ya, ya]
ax.fill(xay, yay, facecolor='k', edgecolor='k')
# eje y
plt.plot([x1, xa], [y1, ya], 'k-', lw=lw)
plt.plot([x2, x1], [y2, y1], 'k--', lw=lw)
plt.plot([x2, (xp_ii - xp_is) / 2], [y2, yp_ii], 'k-', lw=lw)
plt.text(xap-0.05, yap, '$y$', fontsize=fontsize, ha='right', va='top')

# punta de la flecha del eje x
dy2 = dx1 * np.sin(np.arctan(-m))
dx2 = dx1 * dy1 / dy2
xap = xmax_ax - (xp_ii - xp_is) / 2
yap = 0
xa = xap - dx2
ya = 0
n = ya - m * xa
xax = [xap, (ya + dy2 - n) / m, (ya - dy2 - n) / m]
yax = [yap, ya + dy2, ya - dy2]
ax.fill(xax, yax, facecolor='k', edgecolor='k')
# eje x
plt.plot([r, xa], [0, 0], 'k-', lw=lw)
plt.plot([-r, r], [0, 0], 'k--', lw=lw)
plt.plot([xmin_ax + (xp_ii - xp_is) / 2, -r], [0, 0], 'k-', lw=lw)
plt.text(xap, yap - 0.04, '$x$', fontsize=fontsize, ha='right', va='top')


# círculo
plt. plot(xc_sup, yc_sup, 'k-', lw=lw)
plt. plot(xc_inf, yc_inf, 'k--', lw=lw)
# elipse
plt. plot(xe_inf, ye_inf, 'k-', lw=lw)
plt. plot(xe_sup, ye_sup, 'k--', lw=lw)
# plano
plt.plot([xp_ii, xp_is], [yp_ii, yp_is], 'k-', lw=lw)
plt.plot([xp_is, xp_ds], [yp_is, yp_ds], 'k-', lw=lw)
plt.plot([xp_ds, xp_di], [yp_ds, yp_di], 'k-', lw=lw)
plt.plot([xp_di, xp_ii], [yp_di, yp_ii], 'k-', lw=lw)

# polo norte
markersize = 10
xn = 0
yn = 0.9
plt.plot(xn, yn, 'k.', markersize=markersize)
#plt.text(xn, yn + 0.04, '$N$', fontsize=fontsize, ha='center', va='bottom')
plt.text(xn - 0.04, yn - 0.04, '$N$', fontsize=fontsize, ha='right', va='top')
# punto z
xz = 3
yz = -0.5
plt.plot(xz, yz, 'k.', markersize=markersize)
plt.text(xz + 0.04, yz - 0.04, '$z$', fontsize=fontsize, ha='left', va='top')
# parámetros de la recta que une los puntos
m2 = (yz - yn) / (xz - xn)
n2 = yn - m * xn
# punto de intersección
xp = 0.4
yp = m2 * xp + n2
plt.plot([xn, xp], [yn, yp], 'k--', lw=lw)
plt.plot([xp, xz], [yp, yz], 'k-', lw=lw)
plt.plot(xp, yp, 'k.', markersize=markersize)
plt.text(xp - 0.04, yp - 0.04, '$P$', fontsize=fontsize, ha='right', va='top')
# origen
plt.plot(0, 0, 'k.', markersize=markersize)
plt.text(-0.04, -0.04, '$O$', fontsize=fontsize, ha='right', va='top')

plt.axis('off')

plt.savefig('point_at_infinity.pdf', bbox_inches='tight')

plt.show()

