from mayavi import mlab
import numpy as np

# Create a sphere
r = 1.0
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0: pi: 101j, 0: 2*pi: 101j]

x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

phic = np.linspace(0, 2*pi, 101)
xc = r*cos(phic)
yc = r*sin(phic)

xmin = -2
xmax = 2
ymin = -2
ymax = 4

xp, yp = np.mgrid[xmin:xmax:2j, ymin:ymax:2j]
s = np.zeros((2, 2))

lw = 2

mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(800, 600))

# esfera
sphere = mlab.mesh(x, y, z, color=(0.5, 0.5, 0.5), opacity=0.8, representation='surface')
#sphere = mlab.mesh(x, y, z, opacity=0.99, representation='surface')
# plano
mlab.surf(xp, yp, s, color=(0.8, 0.8, 0.8), opacity=0.5)
# circulo unidad
mlab.plot3d(xc, yc, np.zeros(xc.shape), color=(0, 0, 0), line_width=lw)


# eje x
xr = np.linspace(xmin, xmax, 2)
zz = np.zeros(xr.shape)
mlab.plot3d(xr, zz, zz, color=(0, 0, 0), line_width=lw)
# eje y
yr = np.linspace(ymin, ymax, 2)
mlab.plot3d(zz, yr, zz, color=(0, 0, 0), line_width=lw)

# mlab.savefig('test_pdf.pdf')

mlab.view(20, 50)

# These parameters, as well as the color, where tweaked through the GUI,
# with the record mode to produce lines of code usable in a script.
sphere.actor.property.specular = 0.45
sphere.actor.property.specular_power = 5
# Backface culling is necessary for more a beautiful transparent
# rendering.
sphere.actor.property.backface_culling = True

mlab.show()