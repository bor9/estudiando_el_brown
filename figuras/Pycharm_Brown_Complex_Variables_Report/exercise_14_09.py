import numpy as np
import matplotlib.pyplot as plt

__author__ = 'ernesto'

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preview'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']


xmin = -4
xmax = 4
ymin = -4
ymax = 4
N = 11

x, y = np.meshgrid(np.linspace(xmin, xmax, N), np.linspace(ymin, ymax, N))

# w = iz
u1 = -y
v1 = x
# w = z/|z|
u2 = x / np.sqrt(np.square(x) + np.square(y))
v2 = y / np.sqrt(np.square(x) + np.square(y))

fontsize = 14
xticks = np.arange(xmin, xmax + 1)
yticks = np.arange(ymin, ymax + 1)
xticklabels = ['0' if x==0 else '' for x in xticks]
yticklabels = ['0' if x==0 else '' for x in xticks]

fig = plt.figure(0, figsize=(9, 4), frameon=False)

ax = plt.subplot2grid((4, 8), (0, 0), rowspan=4, colspan=4)

plt.axis('equal')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

plt.quiver(x, y, u1, v1)

plt.xticks(xticks)
plt.yticks(yticks)
ax.set_xticklabels(xticklabels)
ax.set_yticklabels(yticklabels)
plt.xlabel('$x$', fontsize=fontsize)
plt.ylabel('$y$', fontsize=fontsize)
plt.title('$w=iz$', fontsize=fontsize)

ax = plt.subplot2grid((4, 8), (0, 4), rowspan=4, colspan=4)

plt.axis('equal')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

plt.quiver(x, y, u2, v2)

plt.xticks(xticks)
plt.yticks(yticks)
ax.set_xticklabels(xticklabels)
ax.set_yticklabels([])
plt.xlabel('$x$', fontsize=fontsize)
plt.title('$w=z/|z|$', fontsize=fontsize)

plt.savefig('exercise_14_09.pdf', bbox_inches='tight')

plt.show()
