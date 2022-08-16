from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'ernesto'

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preview'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

xmin = -4
xmax = 2
ymin = -3
ymax = 3
xr = np.arange(xmin, xmax, 0.02)
yr = np.arange(ymin, ymax, 0.02)
X, Y = np.meshgrid(xr, yr)
# componente real
U = (X**2 + Y**2 - 1)/ ((X + 1)**2 + Y**2)
# componente imaginario
V = -2 * Y / ((X + 1)**2 + Y**2)
# niveles
levels1 = np.arange(-0.5, 2.75, 0.25)
levels2 = np.arange(-1.5, 1.75, 0.25)

fontsize = 13

m = 5
levels_surf = np.arange(-5, 5, 0.2)

fig = plt.figure(0, figsize=(10, 7), frameon=False)
ax = plt.subplot2grid((4, 4), (0, 0), rowspan=2, colspan=2, projection='3d')
plt.contour(X, Y, U, levels=levels_surf, cmap=cm.winter)
plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)
ax.text2D(0.5, 1.02, '$u(x,\,y)=\dfrac{x^2+y^2-1}{(x+1)^2+y^2}$', fontsize=fontsize, ha='center', va='baseline',
          transform=ax.transAxes)
ax.view_init(elev=35, azim=-134)
ax.set_zlim(-m, m)

ax = plt.subplot2grid((4, 4), (0, 2), rowspan=2, colspan=2, projection='3d')
plt.contour(X, Y, V, levels=levels_surf, cmap=cm.autumn)
plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)
ax.text2D(0.5, 1.02, '$v(x,\,y)=\dfrac{2y}{(x+1)^2+y^2}$', fontsize=fontsize, ha='center', va='baseline',
          transform=ax.transAxes)
ax.view_init(elev=35, azim=-134)
ax.set_zlim(-m, m)

ax = plt.subplot2grid((4, 4), (2, 1), rowspan=2, colspan=2)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.gca().set_aspect('equal')

plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)

CS1 = plt.contour(X, Y, U, levels=levels1, cmap=cm.winter)
CS2 = plt.contour(X, Y, V, levels=levels2, cmap=cm.autumn)

labels1 = [None] * CS1.levels.shape[0]
for i in np.arange(CS1.levels.shape[0]):
    labels1[i] = "${0:g}$".format(CS1.levels[i])
labels2 = [None] * CS2.levels.shape[0]
for i in np.arange(CS2.levels.shape[0]):
    labels2[i] = "${0:g}$".format(CS2.levels[i])

legend1 = plt.legend(CS1.collections, labels1, loc='center', bbox_to_anchor=(-0.5, 0.5), frameon=False)
legend2 = plt.legend(CS2.collections, labels2, loc='center', bbox_to_anchor=(1.5, 0.5), frameon=False)

ax.add_artist(legend1)
ax.add_artist(legend2)

plt.text(-0.5, -0.05, '$u(x,\,y)$', fontsize=fontsize, ha='center', va='baseline', transform=ax.transAxes)
plt.text(1.5, -0.05, '$v(x,\,y)$', fontsize=fontsize, ha='center', va='baseline', transform=ax.transAxes)


plt.savefig('exercise_27_6.pdf', bbox_inches='tight')

plt.show()
