import numpy as np
import matplotlib.pyplot as plt

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
a = np.linspace(-1, 1, N)
z = (-1 + np.sqrt(1 - a ** 2)) / a

fig = plt.figure(0, figsize=(5, 5), frameon=False)
ax = fig.add_subplot(111)
plt.gca().set_aspect('equal', adjustable='box')

plt.plot(a, z, color='k', lw=2)
plt.xlabel('a')
plt.ylabel('z')
plt.grid()

plt.show()

