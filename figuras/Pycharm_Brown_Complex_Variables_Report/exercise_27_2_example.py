from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'ernesto'

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preview'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

xmin = -1
xmax = 1
ymin = -1
ymax = 1
xr = np.arange(xmin, xmax, 0.01)
yr = np.arange(ymin, ymax, 0.01)
X, Y = np.meshgrid(xr, yr)
# componente real
U = X**2 - Y**2
# componente imaginario
V = 2*X*Y
# niveles
levels = np.array([-1, -0.75, -0.5, -0.3, -0.1, 0, 0.1, 0.3, 0.5, 0.75, 1])

umin = np.min(U)
umax = np.max(U)
vmin = np.min(V)
vmax = np.max(V)

fontsize = 13

fig = plt.figure(0, figsize=(10, 7), frameon=False)
ax = plt.subplot2grid((4, 4), (0, 0), rowspan=2, colspan=2, projection='3d')
S1 = ax.plot_surface(X, Y, U, cmap=cm.winter, alpha=1, rstride=5, cstride=5)
plt.contour(X, Y, U, levels=levels, cmap=cm.winter, offset=umin)
plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)
plt.title('$u(x,\,y)=x^2-y^2$', fontsize=fontsize)

ax = plt.subplot2grid((4, 4), (0, 2), rowspan=2, colspan=2, projection='3d')
S1 = ax.plot_surface(X, Y, V, cmap=cm.autumn, alpha=1, rstride=1, cstride=1)
plt.contour(X, Y, V, levels=levels, cmap=cm.autumn, offset=vmin)
plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)
plt.title('$v(x,\,y)=2xy$', fontsize=fontsize)


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

plt.text(-0.5, 0, '$u(x,\,y)$', fontsize=fontsize, ha='center', va='baseline', transform=ax.transAxes)
plt.text(1.5, 0, '$v(x,\,y)$', fontsize=fontsize, ha='center', va='baseline', transform=ax.transAxes)


plt.savefig('exercise_27_2_example.pdf', bbox_inches='tight')

plt.show()
