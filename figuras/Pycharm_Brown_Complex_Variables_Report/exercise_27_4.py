from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'ernesto'

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preview'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

mm = 1
xmin = -mm
xmax = mm
ymin = -mm
ymax = mm
xr = np.arange(xmin, xmax, 0.01)
yr = np.arange(ymin, ymax, 0.01)
X, Y = np.meshgrid(xr, yr)
# componente real
U = X / (X**2 + Y**2)
# componente imaginario
V = -Y / (X**2 + Y**2)
# niveles
levels = np.array([-2, -1, -0.75, -0.5, -0.3, -0.1, 0, 0.1, 0.3, 0.5, 0.75, 1, 2])

fontsize = 13

m = 5
levels_surf = np.arange(-5, 5, 0.2)

fig = plt.figure(0, figsize=(10, 7), frameon=False)
ax = plt.subplot2grid((4, 4), (0, 0), rowspan=2, colspan=2, projection='3d')
plt.contour(X, Y, U, levels=levels_surf, cmap=cm.winter)
plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)
ax.text2D(0.5, 1.02, '$u(x,\,y)=\dfrac{x}{x^2+y^2}$', fontsize=fontsize, ha='center', va='baseline', transform=ax.transAxes)
ax.view_init(elev=34, azim=-120)
ax.set_zlim(-m, m)

ax = plt.subplot2grid((4, 4), (0, 2), rowspan=2, colspan=2, projection='3d')
plt.contour(X, Y, V, levels=levels_surf, cmap=cm.autumn)
plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)
ax.text2D(0.5, 1.02, '$v(x,\,y)=-\dfrac{y}{x^2+y^2}$', fontsize=fontsize, ha='center', va='baseline', transform=ax.transAxes)
#ax.view_init(elev=34, azim=50)
ax.view_init(elev=34, azim=-120)
ax.set_zlim(-m, m)

ax = plt.subplot2grid((4, 4), (2, 1), rowspan=2, colspan=2)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.gca().set_aspect('equal')

plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)

CS1 = plt.contour(X, Y, U, levels=levels, cmap=cm.winter)
CS2 = plt.contour(X, Y, V, levels=levels, cmap=cm.autumn)

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


plt.savefig('exercise_27_4.pdf', bbox_inches='tight')

plt.show()
