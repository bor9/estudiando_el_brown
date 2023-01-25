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
alpha = 0.2
beta = 2
a = 0.3
b = 1
n = -0.5

# función de la forma t = A * \tau^n + B
A = (a - b) / (alpha ** n - beta ** n)
B = a - A * alpha ** n

N = 100
tau = np.linspace(alpha, beta, N)
t = A * tau ** n + B

# valores maximos y minimos de los ejes
xmin = 0
xmax = 2.4
ymin = 0
ymax = 1.4


# axis parameters
dx = 0.15
xmin_ax = xmin - dx
xmax_ax = xmax
dy = 0.15
ymin_ax = ymin - dy
ymax_ax = ymax

# length of the ticks for all subplot (6 pixels)
display_length = 6  # in pixels
# x ticks labels margin
xtm = -0.15
ytm = -0.075
# font size
fontsize = 14

fig = plt.figure(0, figsize=(5, 3), frameon=False)
ax = fig.add_subplot(111)

#plt.axis('equal')
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

# z = x + ix
plt.plot(tau, t, color='k', lw=2)
# puntos en los extremos
ms = 9
plt.plot(alpha, a, 'k.', ms=ms)
plt.plot(beta, b, 'k.', ms=ms)

# etiquetas de los ejes
plt.text(xmax_ax, xtm, r'$\tau$', fontsize=fontsize, ha='center', va='baseline')
plt.text(-ytm, ymax_ax, '$t$', fontsize=fontsize, ha='left', va='center')

# lineas punteadas
dashed = (6, 3)
plt.plot([alpha, alpha], [0, a], 'k--', lw=1, dashes=dashed)
plt.plot([beta, beta], [0, b], 'k--', lw=1, dashes=dashed)
plt.plot([0, alpha], [a, a], 'k--', lw=1, dashes=dashed)
plt.plot([0, beta], [b, b], 'k--', lw=1, dashes=dashed)
# ticks labels
plt.text(alpha, xtm, r'$\alpha$', fontsize=fontsize, ha='center', va='baseline')
plt.text(beta, xtm, r'$\beta$', fontsize=fontsize, ha='center', va='baseline')
plt.text(ytm, a, '$a$', fontsize=fontsize, ha='right', va='center')
plt.text(ytm, b, '$b$', fontsize=fontsize, ha='right', va='center')
plt.text(ytm, xtm, '$0$', fontsize=fontsize, ha='right', va='baseline')

da = 0.075
plt.text(alpha + da, a, r'$(\alpha,\,a)$', fontsize=fontsize, ha='left', va='center')
plt.text(beta + da, b, r'$(\beta,\,b)$', fontsize=fontsize, ha='left', va='center')

plt.axis('off')

# save as pdf image
plt.savefig('contours_parameter_transformation.pdf', bbox_inches='tight')

plt.show()

