from mayavi import mlab
import numpy as np

# Create a sphere
r = 1.0
pi = np.pi
cos = np.cos
sin = np.sin

# esfera
# mitad superior
phi, theta = np.mgrid[0: pi/2: 101j, 0: 2*pi: 101j]
xu = r*sin(phi)*cos(theta)
yu = r*sin(phi)*sin(theta)
zu = r*cos(phi)
# mitad superior
phi, theta = np.mgrid[pi/2: pi: 101j, 0: 2*pi: 101j]
xl = r*sin(phi)*cos(theta)
yl = r*sin(phi)*sin(theta)
zl = r*cos(phi)

# circulo unidad
phic = np.linspace(0, 2*pi, 101)
xc = r*cos(phic)
yc = r*sin(phic)

# coordenadas de los vertices del plano
xmin = -2
xmax = 2
ymin = -2
ymax = 4
xp, yp = np.mgrid[xmin:xmax:2j, ymin:ymax:2j]
s = np.zeros((2, 2))

# coordenadas del punto z
xz = 1.3
yz = 3

tr = 0.015

mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(800, 600))

# esfera
sphere_u = mlab.mesh(xu, yu, zu, color=(0.5, 0.5, 0.5), opacity=0.8, representation='surface')
sphere_l = mlab.mesh(xl, yl, zl, color=(0.9, 0.9, 0.9), opacity=0.8, representation='surface')
# plano
mlab.surf(xp, yp, s, color=(0.8, 0.8, 0.8), opacity=0.5)
# circulo unidad
mlab.plot3d(xc, yc, np.zeros(xc.shape), color=(0, 0, 0), tube_radius=tr)

# eje x
xr = np.linspace(xmin+0.1, xmax, 2)
zz = np.zeros(xr.shape)
mlab.plot3d(xr, zz, zz, color=(0, 0, 0), tube_radius=tr)
# eje y
yr = np.linspace(ymin, ymax-0.1, 2)
mlab.plot3d(zz, yr, zz, color=(0, 0, 0), tube_radius=tr)
# linea polo norte - punto z
mlab.plot3d(np.linspace(0, xz, 2), np.linspace(0, yz, 2), [1, 0], color=(0, 0, 0), tube_radius=tr)

# polo norte
size = .08
mlab.points3d(0, 0, 1, color=(0, 0, 0), scale_factor=size)
# punto z
mlab.points3d(xz, yz, 0, color=(0, 0, 0), scale_factor=size)
# interseccion con la esfera
t = 2 / (xz ** 2 + yz ** 2 + 1)
xp = t * xz
yp = t * yz
zp = 1 - t
mlab.points3d(xp, yp, zp, color=(0, 0, 0), scale_factor=size)
# origen
mlab.points3d(0, 0, 0, color=(0, 0, 0), scale_factor=size)

# flechas
l = 0.2
w = 0.1
z = 0.001
mlab.triangular_mesh([w, 0, -w], [ymax-l, ymax, ymax-l], [z, z, z], [(0, 1, 2)], color=(0, 0, 0))
mlab.triangular_mesh([xmin+l, xmin, xmin+l], [-w, 0, w], [z, z, z], [(0, 1, 2)], color=(0, 0, 0))

mlab.view(30, 60, distance='auto')

# These parameters, as well as the color, where tweaked through the GUI,
# with the record mode to produce lines of code usable in a script.
sphere_u.actor.property.specular = 0.45
sphere_l.actor.property.specular = 0.45
sphere_u.actor.property.specular_power = 5
sphere_l.actor.property.specular_power = 5
# Backface culling is necessary for more a beautiful transparent
# rendering.
sphere_u.actor.property.backface_culling = True
sphere_l.actor.property.backface_culling = True

mlab.savefig('point_at_infinity_mayavi_v2.png', size=(1400, 1000))
mlab.show()
