import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

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

N = 200
thetas = np.linspace(0, 2 * np.pi, N)

# para el contorno C
rx = [0, 0.1, 0.2, 0.3, 0.6, 0.75, 1, 1.1, 1.2, 1.3, 1.6, 1.95, 2]
ry = 0.4 * np.array([3, 2.9, 2.5, 2.0, 2.8, 3.3, 3, 2.9, 3.2, 3.5, 2.8, 3, 3])

f = interpolate.interp1d(rx, ry, kind='cubic')
rxnew = np.linspace(0, 2, N, endpoint=True)
rynew = f(rxnew)
x0 = 0
y0 = 0
xc = x0 + rynew * np.cos(thetas)
yc = y0 + rynew * np.sin(thetas)

zc = xc + 1j * yc
wc = (np.power(zc, 4) + 5) / (np.power(zc, 2) - 3 * np.power(zc, 1) + 1.5)

i1 = 0
i2 = 10

fig = plt.figure(0, figsize=(5, 5), frameon=False)
ax = fig.add_subplot(111)
plt.gca().set_aspect('equal', adjustable='box')

plt.plot(xc, yc, color='k', lw=2)
plt.plot(xc[i1], yc[i1], 'k.', ms=8)
plt.plot(xc[i2], yc[i2], 'k.', ms=8)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

fig = plt.figure(1, figsize=(5, 5), frameon=False)
ax = fig.add_subplot(111)
plt.gca().set_aspect('equal', adjustable='box')

plt.plot(np.real(wc), np.imag(wc), color='k', lw=2)
plt.plot(np.real(wc[i1]), np.imag(wc[i1]), 'k.', ms=8)
plt.plot(np.real(wc[i2]), np.imag(wc[i2]), 'k.', ms=8)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.show()

